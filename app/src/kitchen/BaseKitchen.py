import abc

class BaseKitchen:
    @abc.abstractmethod
    def prepare_meal(self, internal_order, current_time):
        "Cooks an order and returns the meal with the time at which it was made"