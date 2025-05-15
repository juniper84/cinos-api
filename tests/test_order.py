import unittest
from api.order import Order
from api.drink import Drink, Size, Base, Flavor
from api.food import Food, FoodType, Topping

class TestOrder(unittest.TestCase):

    def test_add_and_count_items(self):
        o = Order()
        d = Drink(Size.MEDIUM)
        o.add_item(d)
        self.assertEqual(o.get_num_items(), 1)

    def test_remove_item(self):
        o = Order()
        d1, d2 = Drink(Size.SMALL), Drink(Size.LARGE)
        o.add_item(d1)
        o.add_item(d2)
        o.remove_item(0)
        self.assertEqual(o.get_num_items(), 1)

    def test_order_total_with_tax(self):
        o = Order()
        d = Drink(Size.SMALL)
        d.add_flavor(Flavor.LEMON)
        o.add_item(d)
        total = o.get_total()
        expected_subtotal = d.get_total()
        expected_total = round(expected_subtotal + expected_subtotal * 0.0725, 2)
        self.assertAlmostEqual(total, expected_total, places=2)

    def test_receipt_format(self):
        d = Drink(Size.LARGE)
        d.set_base(Base.HILLFOG)
        d.add_flavor(Flavor.LIME)
        o = Order()
        o.add_item(d)
        receipt = o.get_receipt()
        self.assertIn("Large hill fog", receipt)
        self.assertIn("Flavors: lime", receipt)
        self.assertIn("Tax", receipt)
        self.assertIn("Total", receipt)

    def test_add_food_item(self):
        o = Order()
        f = Food(FoodType.HOTDOG)
        f.add_topping(Topping.CHILI)
        o.add_item(f)
        self.assertEqual(o.get_num_items(), 1)
        self.assertAlmostEqual(o.get_total(), round(f.get_total() + f.get_total() * 0.0725, 2))

    def test_receipt_includes_food(self):
        o = Order()
        f = Food(FoodType.NACHO_CHIPS)
        f.add_topping(Topping.NACHO_CHEESE)
        o.add_item(f)
        receipt = o.get_receipt()
        self.assertIn("Nacho Chips", receipt)
        self.assertIn("Toppings: Nacho Cheese", receipt)
        self.assertIn("Total", receipt)