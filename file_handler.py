import json
import os

from inventory import Inventory
from product import Product

FILENAME = "inventory.json"


def load_inventory():
    inventory = Inventory()
    if not os.path.exists(FILENAME):
        print(FILENAME + " not found. Starting with an empty inventory.")
        return inventory
    print(FILENAME + " found.")
    try:
        with open(FILENAME, "r") as f:
            data = json.load(f)
        for item in data:
            inventory.add_product(Product(item["id"], item["name"], item["price"], item["stock"]))
        print("Inventory loaded successfully.")
    except (json.JSONDecodeError, ValueError, KeyError, TypeError):
        print("ERROR: " + FILENAME + " is corrupted. Starting with an empty inventory.")
        return Inventory()
    return inventory


def save_inventory(inventory):
    data = []
    for product in inventory.get_products():
        data.append({"id": product.get_product_id(),
                     "name": product.get_name(),
                     "price": product.get_price(),
                     "stock": product.get_stock()})
    with open(FILENAME, "w") as f:
        json.dump(data, f, indent=4)
