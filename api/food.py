

from enum import Enum

class FoodType(Enum):
    HOTDOG = "Hotdog"
    CORNDOG = "Corndog"
    ICE_CREAM = "Ice Cream"
    ONION_RINGS = "Onion Rings"
    FRENCH_FRIES = "French Fries"
    TATER_TOTS = "Tater Tots"
    NACHO_CHIPS = "Nacho Chips"

class Topping(Enum):
    CHERRY = "Cherry"
    WHIPPED_CREAM = "Whipped Cream"
    CARAMEL_SAUCE = "Caramel Sauce"
    CHOCOLATE_SAUCE = "Chocolate Sauce"
    NACHO_CHEESE = "Nacho Cheese"
    CHILI = "Chili"
    BACON_BITS = "Bacon Bits"
    KETCHUP = "Ketchup"
    MUSTARD = "Mustard"

FOOD_PRICES = {
    FoodType.HOTDOG: 2.30,
    FoodType.CORNDOG: 2.00,
    FoodType.ICE_CREAM: 3.00,
    FoodType.ONION_RINGS: 1.75,
    FoodType.FRENCH_FRIES: 1.50,
    FoodType.TATER_TOTS: 1.70,
    FoodType.NACHO_CHIPS: 1.90
}

TOPPING_PRICES = {
    Topping.CHERRY: 0.00,
    Topping.WHIPPED_CREAM: 0.00,
    Topping.CARAMEL_SAUCE: 0.50,
    Topping.CHOCOLATE_SAUCE: 0.50,
    Topping.NACHO_CHEESE: 0.30,
    Topping.CHILI: 0.60,
    Topping.BACON_BITS: 0.30,
    Topping.KETCHUP: 0.00,
    Topping.MUSTARD: 0.00
}

class Food:
    """Represents a food item with optional toppings."""

    def __init__(self, food_type: FoodType):
        self._type = food_type
        self._toppings = []

    def get_type(self):
        return self._type

    def set_type(self, food_type: FoodType):
        if isinstance(food_type, FoodType):
            self._type = food_type

    def add_topping(self, topping: Topping):
        if isinstance(topping, Topping) and topping not in self._toppings:
            self._toppings.append(topping)

    def get_toppings(self):
        return list(self._toppings)

    def get_num_toppings(self):
        return len(self._toppings)

    def get_total(self):
        base_price = FOOD_PRICES.get(self._type, 0)
        topping_price = sum([TOPPING_PRICES.get(t, 0) for t in self._toppings])
        return round(base_price + topping_price, 2)

    def __str__(self):
        toppings_str = ", ".join([t.value for t in self._toppings]) if self._toppings else "No toppings"
        return f"{self._type.value} with {toppings_str} - ${self.get_total():.2f}"