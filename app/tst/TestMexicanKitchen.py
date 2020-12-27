from app.src.order.InternalOrder import InternalOrder
from app.src.order.InternalOrderFactory import InternalOrderFactory
from app.src.kitchen.MexicanKitchen import MexicanKitchen
import unittest
import time

external_test_order =  {
      "id": "a8cfcb76-7f24-4420-a5ba-d46dd77bdffd",
      "name": "Banana Split",
      "temp": "frozen",
      "shelfLife": 20,
      "decayRate": 0.63
    }

internal_order_factory = InternalOrderFactory()
order_factory = InternalOrderFactory()
test_order = order_factory.create(external_test_order)
mexican_kitchen = MexicanKitchen("Mexican Kitchen")

class TestMexicanKitchen(unittest.TestCase):
    def test_prepare_meal(self):
        current_time = time.time()
        mexican_kitchen.prepare_meal(test_order, current_time).print()
        self.assertEqual(test_order.get_order_id(), "a8cfcb76-7f24-4420-a5ba-d46dd77bdffd")


if __name__ == '__main__':
    unittest.main()