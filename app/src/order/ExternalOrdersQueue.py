
class OrderQueue:

    def __init__(self, orders):
        self.orders = orders
    
    def has_items(self):
        return len(self.orders) > 0
    
    def size(self):
        return len(self.orders)
        
    def push_order(self, order):
        self.orders.append(order)
    
    def get_orders(self, num_of_orders):
        orders = self.orders[0:num_of_orders]
        self.orders = self.orders[num_of_orders:]
        return orders