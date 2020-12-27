import time 

class KitchensManager:
    def __init__(self, list_of_kitchens):
        self.list_of_kitchens = list_of_kitchens
    
    def handle(self, internal_order):
        """Selects proper kitchen and returns a prepared meal by delegating to that kitchen to make the order"""

        # Business logic to decide proper kitchen to be implemented in the future.

        # To simplify testing ad since requirements call for making the meal right away, 
        # I am setting the cooked time here. In the future, the cooked time should be set by the kitchen since they could have a backlog or orders
        current_time = time.time()
        print("[+] Kitchen manager has order id {order_id} and it is selecting the kitchen to make it.".format(order_id=internal_order.get_order_id()))
        return self.list_of_kitchens[0].prepare_meal(internal_order, current_time)
