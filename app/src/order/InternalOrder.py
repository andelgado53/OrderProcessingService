import time

class InternalOrder:
    def __init__(self, order_id, name, temp, shelf_life, decay_rate):
        self.id = order_id
        self.name = name
        self.temp = temp
        self.shelf_life = shelf_life
        self.decay_rate = decay_rate
        self.cooked_at_time = 0
        self.pick_up_time = 0
        self.decay_modifier = {
            'Cold shelf': 1,
            'Hot shelf': 1,
            'Frozen shelf': 1,
            'Overflow shefl': 2
        }

    def get_order_id(self):
        return self.id

    def get_order_name(self):
        return self.name
    
    def get_temp(self):
        return self.temp
    
    def get_shelf_life(self):
        return self.shelf_life
    
    def get_decay_rate(self):
        return self.decay_rate
    
    def get_order_cooked_time(self):
        """Returns the time in epocs that the order was prepared at, or zero if 
            it has not been made yet.
        """
        return self.cooked_at_time
    
    def set_cooked_time(self, time_in_epocs):
        self.cooked_at_time = time_in_epocs
    
    # PAssing current time as a parameter for testing. 
    def get_order_age_in_secs(self, current_time_in_epocs=time.time()):
        return current_time_in_epocs - self.get_order_cooked_time()
    
    def get_pick_up_time(self):
        """Returns time in epocs an order was picked up for delivery, 
            or zero if it has not been picked up yet.
        """
        return self.pick_up_time
    
    def set_pick_up_time(self, pick_up_time):
        """Sets the time in epocs an order was picked up by currier
        """
        self.pick_up_time = pick_up_time
    
    def get_time_before_expiration(self, curr_time=time.time(), shelf_type="Overflow shelf"):
        """Returns the percentage of shelf life that the items has"""
        if self.get_order_cooked_time() == 0:
            raise ValueError('Order has not been prepared yet.')
        decay_value = self.get_decay_rate() * self.get_order_age_in_secs(curr_time) * self.decay_modifier.get(shelf_type, 2)
        time_left = (self.get_shelf_life() - decay_value ) / self.get_shelf_life()
        if time_left <= 0:
            return 0
        return time_left

    def is_expired(self, curr_time, shelf_type="Overflow shelf"):
        return self.get_time_before_expiration(curr_time, shelf_type) <= 0
    
    def print(self):
        return "[** Internal Order ** id: {id}, name: {name}, temp: {temp}, shelfLife: {shelf_life}, decayRate: {decay_rate}, cooked_at_time: {cooked_at}, picked up at: {picked_up_time}]".format(id=self.get_order_id(), name=self.get_order_name(), temp=self.get_temp(), 
        shelf_life=self.get_shelf_life(), decay_rate=self.get_decay_rate(),
        cooked_at=self.get_order_cooked_time(), picked_up_time=self.get_pick_up_time())
    
    def __str__(self):
        return self.print()