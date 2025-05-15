class Order:
    """Represents a customer order consisting of multiple Drink items."""

    TAX_RATE = 0.0725  # 7.25%

    def __init__(self):
        self._items = []

    def add_item(self, item):
        """Add a Drink or Food item to the order."""
        self._items.append(item)

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
        subtotal = sum([item.get_total() for item in self._items])
        tax = subtotal * Order.TAX_RATE
        total = subtotal + tax
        return round(total, 2)

    def get_receipt(self):
        """Generate a receipt showing each drink and food item with full price breakdown."""
        lines = []
        subtotal = 0

        for i, item in enumerate(self._items):
            if hasattr(item, 'get_base'):  # it's a Drink
                base = item.get_base().value if item.get_base() else "No base"
                size = item.get_size().value.capitalize()
                flavors = ", ".join([f.value for f in item.get_flavors()]) or "No flavors"
                cost = item.get_total()
                lines.append(f"{i+1}. {size} {base} | Flavors: {flavors} | ${cost:.2f}")
            elif hasattr(item, 'get_type'):  # it's a Food
                food_type = item.get_type().value
                toppings = ", ".join([t.value for t in item.get_toppings()]) or "No toppings"
                cost = item.get_total()
                lines.append(f"{i+1}. {food_type} | Toppings: {toppings} | ${cost:.2f}")
            elif hasattr(item, 'get_flavors') and hasattr(item, 'get_base') and not hasattr(item, 'get_size') and not hasattr(item, 'get_type'):
                base = item.get_base().value
                mixins = ", ".join([m.value for m in item.get_flavors()]) or "No mix-ins"
                cost = item.get_total()
                lines.append(f"{i+1}. Ice Storm | Base: {base} | Mix-ins: {mixins} | ${cost:.2f}")
            else:
                lines.append(f"{i+1}. Unknown item type.")

            subtotal += item.get_total()

        tax = subtotal * Order.TAX_RATE
        total = subtotal + tax
        lines.append(f"Subtotal: ${subtotal:.2f}")
        lines.append(f"Tax (7.25%): ${tax:.2f}")
        lines.append(f"Total: ${total:.2f}")
        return "\n".join(lines)