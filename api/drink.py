from enum import Enum

class Size(Enum):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"
    MEGA = "mega"

class Base(Enum):
    WATER = "water"
    SBRITE = "sbrite"
    POKECOLA = "pokeacola"
    MRSALT = "Mr. Salt"
    HILLFOG = "hill fog"
    LEAFWINE = "leaf wine"

class Flavor(Enum):
    LEMON = "lemon"
    CHERRY = "cherry"
    STRAWBERRY = "strawberry"
    MINT = "mint"
    BLUEBERRY = "blueberry"
    LIME = "lime"

class Drink:
    """Represents a beverage with a base, flavors, and size-based pricing."""

    SIZE_PRICES = {
        Size.SMALL: 1.50,
        Size.MEDIUM: 1.75,
        Size.LARGE: 2.05,
        Size.MEGA: 2.15
    }
    FLAVOR_PRICE = 0.15

    def __init__(self, size: Size):
        """Initialize a drink with a given size."""
        self._base = None
        self._flavors = []
        self._size = size if isinstance(size, Size) else Size.MEDIUM

    def get_base(self):
        """Return the base of the drink."""
        return self._base

    def set_base(self, base: Base):
        """Set the base if it's a valid Base enum."""
        if isinstance(base, Base):
            self._base = base

    def get_flavors(self):
        """Return a list of the drink's flavors."""
        return list(self._flavors)

    def get_num_flavors(self):
        """Return the number of flavors added."""
        return len(self._flavors)

    def set_flavors(self, flavors):
        """Set multiple flavors, ignoring duplicates and invalid ones."""
        unique_valid_flavors = []
        seen = set()
        for f in flavors:
            if isinstance(f, Flavor) and f not in seen:
                seen.add(f)
                unique_valid_flavors.append(f)
        self._flavors = unique_valid_flavors

    def add_flavor(self, flavor: Flavor):
        """Add a flavor if it's valid and not already added."""
        if isinstance(flavor, Flavor) and flavor not in self._flavors:
            self._flavors.append(flavor)

    def get_size(self):
        """Return the size of the drink."""
        return self._size

    def set_size(self, size: Size):
        """Set the drink size if valid."""
        if isinstance(size, Size):
            self._size = size

    def get_total(self):
        """Calculate total cost: base price + $0.15 per flavor."""
        base_price = Drink.SIZE_PRICES.get(self._size, 1.75)
        flavor_cost = len(self._flavors) * Drink.FLAVOR_PRICE
        return round(base_price + flavor_cost, 2)

    @property
    def cost(self):
        """Live-calculated cost property."""
        return self.get_total()

    def __str__(self):
        base_str = self._base.value if self._base else "No base"
        flavors_str = ", ".join([f.value for f in self._flavors]) if self._flavors else "No flavors"
        return f"{self._size.value.capitalize()} {base_str} with {flavors_str} - ${self.get_total():.2f}"