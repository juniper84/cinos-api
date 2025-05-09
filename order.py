class Order:
    """Represents a customer order consisting of multiple Drink items."""

    TAX_RATE = 0.0725  # 7.25%

    def __init__(self):
        self._items = []

    def add_item(self, drink):
        """Add a Drink to the order."""
        self._items.append(drink)

    def remove_item(self, index):
        """Remove a drink from the order by index."""
        if 0 <= index < len(self._items):
            del self._items[index]

    def get_items(self):
        """Return all drinks in the order."""
        return self._items

    def get_num_items(self):
        """Return number of drinks in the order."""
        return len(self._items)

    def get_total(self):
        """Return the total order cost including tax."""
        subtotal = sum([drink.get_total() for drink in self._items])
        tax = subtotal * Order.TAX_RATE
        total = subtotal + tax
        return round(total, 2)

    def get_receipt(self):
        """Generate a receipt showing each drink and the full price breakdown."""
        lines = []
        subtotal = 0

        for i, drink in enumerate(self._items):
            base = drink.get_base().value if drink.get_base() else "No base"
            size = drink.get_size().value.capitalize()
            flavors = ", ".join([f.value for f in drink.get_flavors()]) or "No flavors"
            cost = drink.get_total()
            subtotal += cost
            lines.append(f"{i+1}. {size} {base} | Flavors: {flavors} | ${cost:.2f}")

        tax = subtotal * Order.TAX_RATE
        total = subtotal + tax
        lines.append(f"Subtotal: ${subtotal:.2f}")
        lines.append(f"Tax (7.25%): ${tax:.2f}")
        lines.append(f"Total: ${total:.2f}")
        return "\n".join(lines)