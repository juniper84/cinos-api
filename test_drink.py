import unittest
from drink import Drink

class TestDrink(unittest.TestCase):

    def test_add_valid_flavor(self):
        d = Drink()
        d.add_flavor("lemon")
        self.assertIn("lemon", d.get_flavors())

    def test_add_duplicate_flavor(self):
        d = Drink()
        d.add_flavor("lemon")
        d.add_flavor("lemon")
        self.assertEqual(len(d.get_flavors()), 1)

    def test_set_flavors(self):
        d = Drink()
        d.set_flavors(["lemon", "mint", "lemon", "invalid"])
        self.assertEqual(d.get_flavors(), ["lemon", "mint"])

    def test_set_base(self):
        d = Drink()
        d.set_base("water")
        self.assertEqual(d.get_base(), "water")