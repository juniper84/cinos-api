# Cinos API Backend

This is the backend logic for the Cinos drink ordering system.

## Features

- Drink class with support for bases and non-duplicate flavors.
- Order class to hold drink items, track totals, and generate receipts.

## Run Tests


```bash
python3 -m unittest test_drink.py
python3 -m unittest test_order.py
# Cinos API Backend

This is the backend logic for the Cinos drink ordering system, developed during Sprint 1 and Sprint 2 of my Test-Driven Development class.

## Sprint 2 Features

- **Drink sizes**: Supports `small`, `medium`, `large`, and `mega`, each with different base prices.
- **Flavor pricing**: Each added flavor increases the drink cost by $0.15.
- **Order totals with tax**: Calculates 7.25% tax on the subtotal of all drinks in an order.
- **Receipt generation**: Provides a formatted receipt with item breakdown, subtotal, tax, and total.
- **Improved test coverage**: Unit tests cover all getters and accessors, including new features added in Sprint 2.
- **Docstrings and comments**: All classes and methods are now documented according to PEP 257.

## Run Tests

Make sure you're in the project folder, then run:

```bash
python3 -m unittest test_drink.py
python3 -m unittest test_order.py
```

## Developer Notes

This project applies Test-Driven Development principles and clean coding practices. All logic was built incrementally with unit tests written for each feature and accessor method before implementation.