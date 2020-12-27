from app.src.shelf.Shelf import Shelf
from app.src.order.InternalOrderFactory import InternalOrderFactory
from app.src.order.InternalOrder import InternalOrder
from app.src.kitchen.KitchensManager import KitchensManager
from app.src.kitchen.MexicanKitchen import MexicanKitchen
import unittest
import time

external_test_order_1 =  {
      "id": "a8cfcb76-7f24-4420-a5ba-d46dd77bdffd",
      "name": "Banana Split",
      "temp": "hot",
      "shelfLife": 20,
      "decayRate": 0.63
    }

order_factory = InternalOrderFactory()
internal_order = order_factory.create(external_test_order_1)
mexican_kitchen = MexicanKitchen("Mexican Food")
kitchen_manager = KitchensManager([mexican_kitchen])

class TestKitchensManager(unittest.TestCase):

    def test_handle(self):
        cooked_order = kitchen_manager.handle(internal_order)
        self.assertEqual(cooked_order, internal_order)
        self.assertIsNot(cooked_order.get_order_cooked_time(), 0)

if __name__ == '__main__':
    unittest.main()