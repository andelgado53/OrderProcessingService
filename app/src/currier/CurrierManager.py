import time 
import random
import threading

class CurrierManager:

    def distpatch_orders(self, shelved_order, shelves):
        """Takes and order that has been plced in a shelf and the shelves 
            and dispatches a driver to pick it up
        """
        print("[+] Shelves before pick up:\n")
        for shelf in shelves:
            print(shelves[shelf].print(time.time()))
        
        # TODO: Create a pool of available drivers
        t = threading.Thread(target=self._dispatch_driver, args=(shelved_order, shelves))
        t.start()

    def _dispatch_driver(self, shelved_order, shelves):
        order_id, shelve_name = shelved_order
        #This simulates the time that it takes a driver to pick up the order
        drive_time = random.randint(2,6)
        time.sleep(drive_time)
        pick_up_time = time.time()
        order  = shelves[shelve_name].remove_order_from_shelf(order_id)
        order.set_pick_up_time(pick_up_time)
        # pull order from shelve and check expiration time
        order_time_to_live_perct = order.get_time_before_expiration(pick_up_time ,shelve_name)
        print("\n[+] Driver for order {order} has arrived.".format(order=order.print()))
        print("[+] Order age is {order_age} seconds.".format(order_age=order.get_order_age_in_secs(pick_up_time)))
        print("[+] Order has {time_to_live} of shelf life left".format(time_to_live=order_time_to_live_perct))
        # If order has run out of shelf life, it gets discarded
        if order_time_to_live_perct > 0:
            print("[+] Driver has left with {order}.".format(order=order.print()))
        else:
            print("[+] Order has expired and it has been discarded. Driver is not too happy =(")
        
        print("[+] Shelves after pick up or discard:\n")
        for shelf in shelves:
            print(shelves[shelf].print(pick_up_time))

    

