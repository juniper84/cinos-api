


from enum import Enum

class IceCreamFlavor(Enum):
    MINT_CHOCOLATE_CHIP = "Mint Chocolate Chip"
    CHOCOLATE = "Chocolate"
    VANILLA_BEAN = "Vanilla Bean"
    BANANA = "Banana"
    BUTTER_PECAN = "Butter Pecan"
    SMORE = "S'more"

class MixIn(Enum):
    CHERRY = "Cherry"
    WHIPPED_CREAM = "Whipped Cream"
    CARAMEL_SAUCE = "Caramel Sauce"
    CHOCOLATE_SAUCE = "Chocolate Sauce"
    STORIOS = "Storios"
    DIG_DOGS = "Dig Dogs"
    TTS = "T&T’s"
    COOKIE_DOUGH = "Cookie Dough"
    PECANS = "Pecans"

FLAVOR_PRICES = {
    IceCreamFlavor.MINT_CHOCOLATE_CHIP: 4.00,
    IceCreamFlavor.CHOCOLATE: 3.00,
    IceCreamFlavor.VANILLA_BEAN: 3.00,
    IceCreamFlavor.BANANA: 3.50,
    IceCreamFlavor.BUTTER_PECAN: 3.50,
    IceCreamFlavor.SMORE: 4.00,
}

MIXIN_PRICES = {
    MixIn.CHERRY: 0.00,
    MixIn.WHIPPED_CREAM: 0.00,
    MixIn.CARAMEL_SAUCE: 0.50,
    MixIn.CHOCOLATE_SAUCE: 0.50,
    MixIn.STORIOS: 1.00,
    MixIn.DIG_DOGS: 1.00,
    MixIn.TTS: 1.00,
    MixIn.COOKIE_DOUGH: 1.00,
    MixIn.PECANS: 0.50,
}

class IceStorm:
    """Represents an Ice Storm dessert with base flavor and mix-ins."""

    def __init__(self, base_flavor: IceCreamFlavor):
        self._base = base_flavor
        self._mixins = []

    def get_base(self):
        return self._base

    def get_flavors(self):
        return list(self._mixins)

    def add_flavor(self, mixin: MixIn):
        if isinstance(mixin, MixIn) and mixin not in self._mixins:
            self._mixins.append(mixin)

    def get_num_flavors(self):
        return len(self._mixins)

    def get_total(self):
        base_price = FLAVOR_PRICES.get(self._base, 0)
        mixin_price = sum([MIXIN_PRICES.get(m, 0) for m in self._mixins])
        return round(base_price + mixin_price, 2)

    def __str__(self):
        mixins_str = ", ".join([m.value for m in self._mixins]) if self._mixins else "No mix-ins"
        return f"IceStorm - {self._base.value} with {mixins_str} (${self.get_total():.2f})"