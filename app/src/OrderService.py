import argparse
import json
import time
from app.src.OrderOrchestrator import OrderOrchestrator
from app.src.currier.CurrierManager import CurrierManager
from app.src.shelf.ShelvesManager import ShelvesManager
from app.src.shelf.Shelf import Shelf
from app.src.order.ExternalOrdersQueue import OrderQueue
from app.src.order.InternalOrderFactory import InternalOrderFactory
from app.src.kitchen.MexicanKitchen import MexicanKitchen
from app.src.kitchen.KitchensManager import KitchensManager
   
def main(tps, files_with_orders):

    # Hard coding the shelves here, but they could be created at run time by using a configuration. 
    # That would allow to increase capacity or add remove.
    # They could also be its own object or database connection.
    # For simplicity I am creating them here.
    shelves = {
        "hot": Shelf(10, "hot", "Hot Shelve"),
        "cold": Shelf(10, "cold", "Cold Shelve"),
        "frozen": Shelf(10, "frozen", "Frozen Shelve"),
        "overflow": Shelf(10, "Any", "Overflow Shelve")
    }
    
    with open(files_with_orders) as json_orders:
        list_of_all_orders = json.load(json_orders)

    internal_order_factory = InternalOrderFactory()
    mexican_restaurant = MexicanKitchen("Mexican Kitchen")
    currier_manager = CurrierManager()
    shelves_manager = ShelvesManager()
    kitchens_manager = KitchensManager([mexican_restaurant])
    order_orchestrator = OrderOrchestrator(shelves, kitchens_manager, shelves_manager, currier_manager)
    
    order_queue = OrderQueue(list_of_all_orders)
    print("[+] Starting to proccess {num_of_orders} orders".format(num_of_orders=order_queue.size()))
    while order_queue.has_items():
        external_orders = order_queue.get_orders(tps)
        for external_order in external_orders:
            try:
                internal_order = internal_order_factory.create(external_order)
                print("[+] Order {order} received.\n[+] Passing the order to orchestrator to get it ready for delivery.".format(order=internal_order.print()))
                order_orchestrator.handle_order(internal_order)
                print("******************************************************************************************************")
            except Exception as e:
                # Catches any the order that can not be processed. TODO: handle different type of exceptions.
                print("[+] Failed to process order {external_order}".format(external_order=external_order))
                print(e)
        # Sleeping for one sec to simulate TPS. 
        time.sleep(1)
    
    print("[+] Finished processing all orders." )
    print("[+] Program is termininating now.")

def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tps", help="orders per second", default=2, type=int)
    parser.add_argument("--orders", help="path to file containing the orders to process", required=True)
    args = parser.parse_args()
    main(args.tps, args.orders)

if __name__ == "__main__":
    run()