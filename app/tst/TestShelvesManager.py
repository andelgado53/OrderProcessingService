from app.src.shelf.Shelf import Shelf
from app.src.order.InternalOrderFactory import InternalOrderFactory
from app.src.order.InternalOrder import InternalOrder
from app.src.shelf.ShelvesManager import ShelvesManager
import unittest
import time

external_test_order_1 =  {
      "id": "a8cfcb76-7f24-4420-a5ba-d46dd77bdffd",
      "name": "Banana Split",
      "temp": "hot",
      "shelfLife": 20,
      "decayRate": 0.63
    }

external_test_order_2 = {
    "id": "2ec069e3-576f-48eb-869f-74a540ef840c",
    "name": "Acai Bowl",
    "temp": "cold",
    "shelfLife": 249,
    "decayRate": 0.3
  }

shelves = {
    'hot': Shelf(10, 'hot', 'Hot Shelve'),
    'cold': Shelf(10, 'cold', 'Cold Shelve'),
    'frozen': Shelf(10, 'frozen', 'Frozen Shelve'),
    'overflow': Shelf(10, 'Any', 'Overflow Shelve')
    }

orders  = [external_test_order_1, external_test_order_2]

order_factory = InternalOrderFactory()
internal_orders = [order_factory.create(order) for order in orders]
shelves_manager = ShelvesManager()

class TestShelvesManager(unittest.TestCase):

    def test_store_order_when_shelf_has_room(self):
        test_order = internal_orders[0]
        shelves.get("hot").items[0] = 0
        order_id, shelve_temp = shelves_manager.store_order(test_order, shelves)
        self.assertEqual(order_id, test_order.get_order_id())
        self.assertEqual(shelve_temp, test_order.get_temp())
    
    def test_store_order_when_shelf_has_no_room_but_overflow_shelf_does(self):
        test_order = internal_orders[0]
        shelves.get("hot").items[0] = 10
        order_id, shelve_temp = shelves_manager.store_order(test_order, shelves)
        self.assertEqual(order_id, test_order.get_order_id())
        self.assertEqual(shelve_temp, 'overflow')
        shelves.get("hot").items[0] = 0
        shelves.get("overflow").orders.clear()
        shelves.get("hot").orders.clear()
    
    def test_store_order_when_shelf_has_no_room_and_overflow_shelf_does_not_either(self):
        curr_time = time.time() + 15
        test_order = internal_orders[0]
        test_order_1 = internal_orders[1]
        test_order.set_cooked_time(curr_time)
        test_order_1.set_cooked_time(curr_time)
        shelves.get("hot").items[0] = 10
        shelves.get("overflow").store_order(test_order_1)
        shelves.get("overflow").items[0] = 10
        order_id, shelve_temp = shelves_manager.store_order(test_order, shelves)
        self.assertEqual(order_id, test_order.get_order_id())
        self.assertEqual(shelve_temp, 'overflow')
        shelves.get("hot").items[0] = 0
        shelves.get("overflow").items[0] = 0
        shelves.get("overflow").orders.clear()
        shelves.get("hot").orders.clear()
    
    def test_store_order_when_all_shelves_are_full(self):
        curr_time = time.time() + 15
        test_order = internal_orders[0]
        test_order_1 = internal_orders[1]
        test_order.set_cooked_time(curr_time)
        test_order_1.set_cooked_time(curr_time - 10)
        shelves.get("hot").items[0] = 10
        shelves.get("cold").items[0] = 10
        shelves.get("overflow").store_order(test_order_1)
        shelves.get("overflow").items[0] = 10
        order_id, shelve_temp = shelves_manager.store_order(test_order, shelves)
        self.assertEqual(order_id, test_order.get_order_id())
        self.assertEqual(shelve_temp, 'overflow')
        shelves.get("hot").items[0] = 0
        shelves.get("overflow").items[0] = 0
        shelves.get("overflow").orders.clear()
        shelves.get("hot").orders.clear()
        shelves.get("cold").orders.clear()

if __name__ == '__main__':
    unittest.main()