class Order:
    def __init__(self):
        self._items = []

    def add_item(self, drink):
        self._items.append(drink)

    def remove_item(self, index):
        if 0 <= index < len(self._items):
            del self._items[index]

    def get_items(self):
        return self._items

    def get_num_items(self):
        return len(self._items)

    def get_total(self):
        return round(len(self._items) * 2.50, 2)

    def get_receipt(self):
        receipt = []
        for i, drink in enumerate(self._items):
            base = drink.get_base() or "No base"
            flavors = ", ".join(drink.get_flavors()) or "No flavors"
            receipt.append(f"{i+1}. Base: {base} | Flavors: {flavors}")
        receipt.append(f"Total: ${self.get_total():.2f}")
        return "\n".join(receipt)