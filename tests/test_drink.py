import unittest
from api.drink import Drink, Size, Base, Flavor

class TestDrink(unittest.TestCase):

    def test_add_valid_flavor(self):
        d = Drink(Size.MEDIUM)
        d.add_flavor(Flavor.LEMON)
        self.assertIn(Flavor.LEMON, d.get_flavors())

    def test_add_duplicate_flavor(self):
        d = Drink(Size.MEDIUM)
        d.add_flavor(Flavor.LEMON)
        d.add_flavor(Flavor.LEMON)
        self.assertEqual(len(d.get_flavors()), 1)

    def test_set_invalid_flavors_ignored(self):
        d = Drink(Size.MEDIUM)
        d.set_flavors([Flavor.LEMON, "invalid", Flavor.MINT])
        self.assertEqual(d.get_flavors(), [Flavor.LEMON, Flavor.MINT])

    def test_set_valid_base(self):
        d = Drink(Size.SMALL)
        d.set_base(Base.POKECOLA)
        self.assertEqual(d.get_base(), Base.POKECOLA)

    def test_invalid_size_defaults_to_medium(self):
        d = Drink("gigantic")  # Invalid string should default to MEDIUM
        self.assertEqual(d.get_size(), Size.MEDIUM)

    def test_flavor_price_addition(self):
        d = Drink(Size.SMALL)
        d.add_flavor(Flavor.LEMON)
        d.add_flavor(Flavor.MINT)
        total = d.get_total()
        self.assertAlmostEqual(total, 1.50 + 0.30, places=2)

    def test_set_size(self):
        d = Drink(Size.SMALL)
        d.set_size(Size.MEGA)
        self.assertEqual(d.get_size(), Size.MEGA)