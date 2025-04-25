import unittest
from order import Order
from drink import Drink

class TestOrder(unittest.TestCase):

    def test_add_and_count_items(self):
        o = Order()
        d = Drink()
        o.add_item(d)
        self.assertEqual(o.get_num_items(), 1)

    def test_remove_item(self):
        o = Order()
        d1, d2 = Drink(), Drink()
        o.add_item(d1)
        o.add_item(d2)
        o.remove_item(0)
        self.assertEqual(o.get_num_items(), 1)

    def test_total_price(self):
        o = Order()
        for _ in range(3):
            o.add_item(Drink())
        self.assertEqual(o.get_total(), 7.50)

    def test_get_receipt_format(self):
        d = Drink()
        d.set_base("water")
        d.add_flavor("lemon")
        o = Order()
        o.add_item(d)
        receipt = o.get_receipt()
        self.assertIn("Base: water", receipt)
        self.assertIn("Flavors: lemon", receipt)
        self.assertIn("Total: $2.50", receipt)