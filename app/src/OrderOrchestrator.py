
class OrderOrchestrator:

    def __init__(self, shelves, kitchens_manager, shelves_manager, currier_manager):
        self.shelves = shelves
        self.kitchens_manager = kitchens_manager
        self.shelves_manager = shelves_manager
        self.currier_manager = currier_manager
    
    def handle_order(self, internal_order):
        """Goes to the steps needed to handle an order"""
        print("[+] Orchestrator is working on order id: {order_id}.".format(order_id=internal_order.get_order_id()))
        cooked_order = self.kitchens_manager.handle(internal_order)
        shelved_order = self.shelves_manager.store_order(cooked_order, self.shelves)
        self.currier_manager.distpatch_orders(shelved_order, self.shelves)