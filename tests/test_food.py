

import unittest
from api.food import Food, FoodType, Topping

class TestFood(unittest.TestCase):

    def test_set_and_get_type(self):
        f = Food(FoodType.CORNDOG)
        self.assertEqual(f.get_type(), FoodType.CORNDOG)
        f.set_type(FoodType.ICE_CREAM)
        self.assertEqual(f.get_type(), FoodType.ICE_CREAM)

    def test_add_valid_topping(self):
        f = Food(FoodType.HOTDOG)
        f.add_topping(Topping.CHILI)
        self.assertIn(Topping.CHILI, f.get_toppings())

    def test_add_duplicate_topping(self):
        f = Food(FoodType.FRENCH_FRIES)
        f.add_topping(Topping.KETCHUP)
        f.add_topping(Topping.KETCHUP)
        self.assertEqual(len(f.get_toppings()), 1)

    def test_get_num_toppings(self):
        f = Food(FoodType.NACHO_CHIPS)
        f.add_topping(Topping.NACHO_CHEESE)
        f.add_topping(Topping.BACON_BITS)
        self.assertEqual(f.get_num_toppings(), 2)

    def test_total_price_with_toppings(self):
        f = Food(FoodType.TATER_TOTS)
        f.add_topping(Topping.CHILI)
        f.add_topping(Topping.BACON_BITS)
        expected_total = 1.70 + 0.60 + 0.30
        self.assertAlmostEqual(f.get_total(), round(expected_total, 2))

    def test_str_output(self):
        f = Food(FoodType.ONION_RINGS)
        f.add_topping(Topping.KETCHUP)
        result = str(f)
        self.assertIn("Onion Rings", result)
        self.assertIn("Ketchup", result)
        self.assertIn("$", result)