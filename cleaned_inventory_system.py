"""
Inventory Management System.

This module manages inventory operations including adding, removing,
saving, and loading items with a JSON-based backend.
"""
import json
import ast

# Global inventory storage
stock_data = {}


def add_item(product_name, quantity, logs=None):
    """
    Add an item with specified quantity to the inventory.

    Args:
        product_name: Name of the item to add
        quantity: Quantity of the item
        logs: Optional list to log operations
    """
    if logs is None:
        logs = []
    stock_data[product_name] = quantity
    logs.append(f"Added: {product_name} - Qty: {quantity}")


def remove_item(product_name):
    """
    Remove an item from the inventory.

    Args:
        product_name: Name of the item to remove
    """
    try:
        del stock_data[product_name]
    except KeyError:
        print(f"Item '{product_name}' not found in inventory")


def get_qty(product_name):
    """
    Get the quantity of a specific item.

    Args:
        product_name: Name of the item

    Returns:
        Quantity of the item or 0 if not found
    """
    return stock_data.get(product_name, 0)


def load_data(file_path):
    """
    Load inventory data from a JSON file.

    Args:
        file_path: Path to the JSON file
    """
    global stock_data
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            stock_data = json.load(file)
    except FileNotFoundError:
        print(f"File '{file_path}' not found")
    except json.JSONDecodeError:
        print(f"Invalid JSON format in '{file_path}'")


def save_data(file_path):
    """
    Save inventory data to a JSON file.

    Args:
        file_path: Path to save the JSON file
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(stock_data, file, indent=4)
    except IOError as err:
        print(f"Error saving file: {err}")


def print_data():
    """
    Print all items in the inventory.
    """
    if not stock_data:
        print("Inventory is empty")
    else:
        print("Current Inventory:")
        for product_name, quantity in stock_data.items():
            print(f"  {product_name}: {quantity}")


def check_low_items(min_threshold):
    """
    Check and print items below a quantity threshold.

    Args:
        min_threshold: Minimum quantity threshold
    """
    low_items = {
        prod_name: prod_qty
        for prod_name, prod_qty in stock_data.items()
        if prod_qty < min_threshold
    }
    if low_items:
        print(f"Items below threshold ({min_threshold}):")
        for prod_name, prod_qty in low_items.items():
            print(f"  {prod_name}: {prod_qty}")
    else:
        print(f"No items below threshold ({min_threshold})")


def safe_literal_eval(expression):
    """
    Safely evaluate simple literals and expressions.

    Args:
        expression: String representation to evaluate

    Returns:
        Evaluated result or None if evaluation fails
    """
    try:
        return ast.literal_eval(expression)
    except (ValueError, SyntaxError):
        print("Invalid expression passed to safe_literal_eval")
        return None


def main():
    """
    Main function demonstrating inventory operations.
    """
    # Demo operations
    add_item("Apple", 50)
    add_item("Banana", 30)
    add_item("Orange", 5)
    print_data()
    check_low_items(10)

    # Example of safe evaluation
    result = safe_literal_eval("[1, 2, 3]")
    if result:
        print(f"Safely evaluated: {result}")

    print("Inventory system demo completed")


if __name__ == "__main__":
    main()
