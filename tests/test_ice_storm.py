


import unittest
from api.ice_storm import IceStorm, IceCreamFlavor, MixIn

class TestIceStorm(unittest.TestCase):

    def test_base_flavor_initialization(self):
        storm = IceStorm(IceCreamFlavor.CHOCOLATE)
        self.assertEqual(storm.get_base(), IceCreamFlavor.CHOCOLATE)

    def test_add_and_get_mixins(self):
        storm = IceStorm(IceCreamFlavor.VANILLA_BEAN)
        storm.add_flavor(MixIn.STORIOS)
        storm.add_flavor(MixIn.CHOCOLATE_SAUCE)
        self.assertIn(MixIn.STORIOS, storm.get_flavors())
        self.assertIn(MixIn.CHOCOLATE_SAUCE, storm.get_flavors())
        self.assertEqual(len(storm.get_flavors()), 2)

    def test_prevent_duplicate_mixins(self):
        storm = IceStorm(IceCreamFlavor.SMORE)
        storm.add_flavor(MixIn.CARAMEL_SAUCE)
        storm.add_flavor(MixIn.CARAMEL_SAUCE)
        self.assertEqual(storm.get_num_flavors(), 1)

    def test_get_total_price(self):
        storm = IceStorm(IceCreamFlavor.BANANA)
        storm.add_flavor(MixIn.STORIOS)
        storm.add_flavor(MixIn.COOKIE_DOUGH)
        expected_total = 3.50 + 1.00 + 1.00
        self.assertAlmostEqual(storm.get_total(), round(expected_total, 2))

    def test_str_representation(self):
        storm = IceStorm(IceCreamFlavor.BUTTER_PECAN)
        storm.add_flavor(MixIn.PECANS)
        desc = str(storm)
        self.assertIn("Butter Pecan", desc)
        self.assertIn("Pecans", desc)
        self.assertIn("$", desc)

if __name__ == "__main__":
    unittest.main()