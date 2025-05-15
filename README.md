# Cinos API Backend

This is the backend logic for the Cinos drink ordering system, developed during Sprint 1 and Sprint 2 of my Test-Driven Development class.

## Sprint 2 Features

- **Drink sizes**: Supports `small`, `medium`, `large`, and `mega`, each with different base prices.
- **Flavor pricing**: Each added flavor increases the drink cost by $0.15.
- **Order totals with tax**: Calculates 7.25% tax on the subtotal of all drinks in an order.
- **Receipt generation**: Provides a formatted receipt with item breakdown, subtotal, tax, and total.
- **Improved test coverage**: Unit tests cover all getters and accessors, including new features added in Sprint 2.
- **Docstrings and comments**: All classes and methods are now documented according to PEP 257.

## Sprint 3 Features

- **Food class**: A new `Food` class supports multiple food types like Hotdog, Corndog, and Ice Cream.
- **Toppings**: Foods can have multiple toppings like Chili, Bacon Bits, or Whipped Cream.
- **Pricing logic**: Each food type has a base cost, and some toppings add extra cost.
- **Receipt update**: The order receipt now includes food items and their toppings alongside drinks.
- **Tax calculation**: Tax is applied to the total of both food and drink items.
- **Unit tests for food**: Full test coverage was added in `test_food.py` to verify food functionality.

## Sprint 4 Features

- **Ice Storm class**: Introduced a new `IceStorm` class representing frozen dessert items with customizable base flavors and mix-ins.
- **Base flavor support**: Allows selection of base flavors like Mint Chocolate Chip, Chocolate, and Butter Pecan, each with their own pricing.
- **Mix-in/topping support**: Ice Storms support additional toppings like Storios, Cookie Dough, and Caramel Sauce, each affecting the price.
- **Pricing logic**: Combines base flavor price and mix-in costs into a final total.
- **Receipt update**: The receipt now includes Ice Storms with their selected flavors and mix-ins listed.
- **Unit tests for Ice Storm**: All functionality tested in `test_ice_storm.py` as part of TDD workflow.

## Run Tests

Make sure you're in the project folder, then run:

```bash
python3 -m unittest test_drink.py
python3 -m unittest test_order.py
python3 -m unittest test_food.py
python3 -m unittest test_ice_storm.py
```

## Developer Notes

This project applies Test-Driven Development principles and clean coding practices. All logic was built incrementally with unit tests written for each feature and accessor method before implementation.