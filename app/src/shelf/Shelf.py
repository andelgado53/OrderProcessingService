
class Shelf:
    def __init__(self, capacity, temperature, name):
        self.capacity = capacity
        self.temperature = temperature
        self.name = name
        self.orders = {}
        self.items = [0]
    
    def get_shelf_name(self):
        return self.name
    
    def get_shelf_temperature(self):
        return self.temperature
    
    def store_order(self, internal_order):
        """Places an order in the shelf if it has space otherwise it throws and exception"""
        if self.has_room():
            self.orders[internal_order.get_order_id()] = internal_order
            self.items[0] = self.items[0] + 1
        else:
            raise ValueError("Shelf is full")
        
    def has_room(self):
        """Returns true is there is available space in the shelf to store one more item"""
        return self.items[0] < self.capacity
    
    def get_item_closer_to_expiration(self, curr_time):
        """Returns the olderst item in the shelf according to shelf live or None if shelf is empty"""
        if self.items[0] > 0:
            return self._get_items_by_expiration(curr_time)[0]
        return None
    
    def _get_items_by_expiration(self, curr_time):
        """Returns a list of items in the shelf ordered asc by expiration time,
            or an empty list if shelf is empty
        """
        if self.items[0] > 0:
            items_in_shelf = [order for order in self.orders.values()]
            sorted_items_in_shelf = sorted(items_in_shelf, key=lambda x: x.get_time_before_expiration(curr_time, self.name))
            return sorted_items_in_shelf
        return []
    
    def peak_order_from_shelf(self, order_id):
        """Returns an order from the shelf if it exists without removing it from the shelf, or None"""
        return self.orders.get(order_id, None)
    
    def remove_order_from_shelf(self, order_id):
        """Returns an order from the shelf if it exists and removes it from the shelf, or None"""
        self.items[0] = self.items[0] - 1
        return self.orders.pop(order_id, None)

    def print_orders(self, curr_time):
        orders = []
        for internal_order in self.orders.values():
            orders.append("{order_id}, {order_name}, cooked at {cooked_time}, percentage of shelf life left {decay_left}".format(order_id=internal_order.get_order_id(),
            order_name=internal_order.get_order_name(), cooked_time=internal_order.get_order_cooked_time(), 
            decay_left=internal_order.get_time_before_expiration(curr_time=curr_time, shelf_type=self.get_shelf_name())))
        return orders


    def print(self, curr_time):
        return "\n[+][+] Shelf name: {name}, temperature: {temp}, capacity: {capacity}, items: {items}, orders waiting pick up: {orders}".format(name=self.get_shelf_name(),
        temp=self.get_shelf_temperature(), capacity=self.capacity, items=self.items[0], orders=self.print_orders(curr_time))
