from app.src.shelf.Shelf import Shelf
from app.src.order.InternalOrderFactory import InternalOrderFactory
from app.src.order.InternalOrder import InternalOrder
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
    "temp": "hot",
    "shelfLife": 249,
    "decayRate": 0.3
  }

external_test_order_3 = {
    "id": "74e0893f-8544-4298-b507-9cf5ab847d83",
    "name": "Pad See Ew",
    "temp": "hot",
    "shelfLife": 210,
    "decayRate": 0.72
  }

orders  = [external_test_order_1, external_test_order_2, external_test_order_3]

order_factory = InternalOrderFactory()
shelf = Shelf(10, "hot", "Hot shelf")
internal_orders = [order_factory.create(order) for order in orders]

class TestShelf(unittest.TestCase):

    def test_store_order_when_shelf_has_room(self):
        order = internal_orders[0]
        shelf.store_order(order)
        self.assertEqual(shelf.orders[order.get_order_id()],  order)
        self.assertEqual(shelf.items[0], 1)
        shelf.orders.clear()
        shelf.items[0] = 0

    def test_store_order_when_shelf_is_full(self):
        shelf.items[0] = 10
        order = internal_orders[0]
        self.assertRaises(ValueError, shelf.store_order, order)
        shelf.items[0] = 0
    
    def test_has_room_when_there_is_room(self):
        self.assertTrue(shelf.has_room())
    
    def test_has_room_when_there_is_no_room(self):
        shelf.items[0] = 10
        self.assertFalse(shelf.has_room())
        shelf.items[0] = 0
    
    def test_get_item_closer_to_expiration_where_there_is_items(self):
        curr_time = time.time()
        for order in internal_orders:
            order.set_cooked_time(curr_time)
            shelf.store_order(order)
        expected_order = internal_orders[0]
        self.assertEqual(shelf.get_item_closer_to_expiration(curr_time + 15), expected_order)
        shelf.orders.clear()
        shelf.items[0] = 0
    
    def test_remove_order_from_shelf(self):
        order = internal_orders[0]
        shelf.store_order(order)
        self.assertEqual(shelf.remove_order_from_shelf(order.get_order_id()), order)
        shelf.items[0] = 0
        shelf.orders.clear()
        
if __name__ == '__main__':
    unittest.main()