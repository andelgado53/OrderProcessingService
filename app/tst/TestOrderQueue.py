from app.src.order.ExternalOrdersQueue import OrderQueue
import unittest

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

external_orders = [external_test_order_1, external_test_order_2, external_test_order_3]
q = OrderQueue(external_orders)

class TestOrderQueue(unittest.TestCase):
    def test_has_items_when_queue_has_items(self):
        q = OrderQueue(external_orders)
        self.assertTrue(q.has_items())
        q.orders.clear()
    
    def test_has_items_when_queue_has_no_items(self):
        q = OrderQueue(external_orders)
        q.get_orders(3)
        self.assertFalse(q.has_items())
        q.orders.clear()
    
    def test_push_order(self):
        q.orders.clear()
        self.assertFalse(q.has_items())
        q.push_order(external_test_order_1)
        self.assertEqual(len(q.orders), 1)
        q.orders.clear()
    
    def test_get_orders_when_there_are_orders(self):
        q.orders.clear()
        q.push_order(external_test_order_1)
        q.push_order(external_test_order_2)
        q.push_order(external_test_order_3)
        self.assertEqual(len(q.get_orders(2)), 2)
        self.assertEqual(len(q.get_orders(2)), 1)
        self.assertEqual(len(q.get_orders(2)), 0)
        q.orders.clear()


if __name__ == '__main__':
    unittest.main()