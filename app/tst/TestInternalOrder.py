from app.src.order.InternalOrder import InternalOrder
from app.src.order.InternalOrderFactory import InternalOrderFactory
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

class TestInternalOrder(unittest.TestCase):
  def test_get_order_id(self):
    self.assertEqual(test_order.get_order_id(), "a8cfcb76-7f24-4420-a5ba-d46dd77bdffd", "Should be a8cfcb76-7f24-4420-a5ba-d46dd77bdffd")

  def test_get_order_name(self):
    self.assertEqual(test_order.get_order_name(), "Banana Split", "Should be Banana Split")

  def test_get_order_temp(self):
    self.assertEqual(test_order.get_temp(), "frozen", "Should be frozen")

  def test_get_order_decay(self):
      self.assertEqual(test_order.get_decay_rate(), 0.63, "Should be 0.63")

  def test_get_shelf_life(self):
      self.assertEqual(test_order.get_shelf_life(), 20, "Should be 20")
  
  def test_get_cooked_time_when_order_is_not_cooked_yet(self):
      self.assertEqual(test_order.get_order_cooked_time(), 0)
  
  def test_set_cooked_time_when_order_is_cooked(self):
    cooked_time = time.time()
    test_order.set_cooked_time(cooked_time)
    self.assertEqual(test_order.get_order_cooked_time(), cooked_time)
  
  def test_get_order_age_in_secs(self):
    cooked_time = time.time()
    test_order.set_cooked_time(cooked_time)
    self.assertEqual(test_order.get_order_age_in_secs(cooked_time + 3), 3)
  
  def test_get_time_before_expiration_when_order_is_not_cooked_yet(self):
    current_time = time.time()
    test_order.set_cooked_time(0)
    self.assertRaises(ValueError, test_order.get_time_before_expiration, current_time, "Cold shelf")

  def test_get_time_before_expiration_when_order_is_cooked(self):
      cooked_time = time.time()
      current_time = cooked_time + 10
      test_order.set_cooked_time(cooked_time)
      expected_value = 0.685
      rounded_return_value = round(test_order.get_time_before_expiration(current_time, "Cold shelf"), 4)
      self.assertEqual(rounded_return_value, expected_value)

if __name__ == '__main__':
    unittest.main()
