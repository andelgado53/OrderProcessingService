from app.src.order.InternalOrder import InternalOrder

class InternalOrderFactory:
    def create(self, external_order):
        """Takes an external order and creates an internal representation of an order that can be handled by the system
        """
        return InternalOrder(
            external_order['id'], 
            external_order['name'], 
            external_order['temp'], 
            external_order['shelfLife'], 
            external_order['decayRate']
            )