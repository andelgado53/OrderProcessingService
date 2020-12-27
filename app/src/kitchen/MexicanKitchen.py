from app.src.kitchen.BaseKitchen import BaseKitchen

class MexicanKitchen(BaseKitchen):

    def __init__(self, kitchen_name):
        self.kitchen_name = kitchen_name

    def prepare_meal(self, internal_order, curr_time):
        """Takes an internal order and time in epocs and returns a 'cooked' meal"""
        
        internal_order.set_cooked_time(curr_time)
        print("[+] {kitchen_name} just prepared order {order_id} at time {cooked_time}.".format(kitchen_name=self.kitchen_name, 
        order_id=internal_order.get_order_id(), cooked_time=internal_order.get_order_cooked_time()))
        return internal_order