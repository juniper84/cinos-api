class Drink:
    VALID_BASES = ["water", "sbrite", "pokeacola", "Mr. Salt", "hill fog", "leaf wine"]
    VALID_FLAVORS = ["lemon", "cherry", "strawberry", "mint", "blueberry", "lime"]

    def __init__(self):
        self._base = None
        self._flavors = []

    def get_base(self):
        return self._base

    def get_flavors(self):
        return list(self._flavors)

    def get_num_flavors(self):
        return len(self._flavors)

    def set_flavors(self, flavors):
        self._flavors = list(dict.fromkeys([f for f in flavors if f in Drink.VALID_FLAVORS]))

    def add_flavor(self, flavor):
        if flavor in Drink.VALID_FLAVORS and flavor not in self._flavors:
            self._flavors.append(flavor)

    def set_base(self, base):
        if base in Drink.VALID_BASES:
            self._base = base