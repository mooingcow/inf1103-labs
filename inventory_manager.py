from file_handler import FILENAME, load_inventory, save_inventory
from inventory import LINE
from product import Product


def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("ERROR: Value cannot be negative.")
            else:
                return value
        except ValueError:
            print("ERROR: Please enter a valid number.")


def get_int(prompt):
    while True:
        entry = input(prompt)
        if entry.isdigit():
            return int(entry)
        print("ERROR: Please enter a non-negative whole number.")


def add_product(inventory):
    print("\nAdd New Product")
    product_id = input("Product ID: ").strip().upper()
    if not product_id:
        print("\nERROR: Product ID cannot be empty.")
        return
    if inventory.search_product(product_id) is not None:
        print("\nERROR: Product ID already exists.")
        return
    name = input("Product Name: ").strip()
    price = get_float("Price: ")
    stock = get_int("Stock Quantity: ")
    inventory.add_product(Product(product_id, name, price, stock))
    print("\nProduct added successfully!")


def update_stock(inventory):
    print("\nUpdate Stock")
    product_id = input("Enter Product ID: ").strip().upper()
    product = inventory.search_product(product_id)
    if product is None:
        print("\nProduct not found.")
        return
    print("\nProduct Found:")
    print("Name: " + product.get_name())
    print("Current Stock: " + str(product.get_stock()))
    if product.update_stock(get_int("\nNew Stock Quantity: ")):
        print("\nStock updated successfully!")


def search_product(inventory):
    print("\nSearch Product")
    product_id = input("Enter Product ID: ").strip().upper()
    product = inventory.search_product(product_id)
    if product is None:
        print("\nProduct not found.")
        return
    print("\nProduct Found")
    print(LINE)
    print("ID: " + product.get_product_id())
    print("Name: " + product.get_name())
    print("Price: $" + format(product.get_price(), ".2f"))
    print("Stock: " + str(product.get_stock()))
    print(LINE)


def show_menu():
    print("\n----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")


print("========================================")
print("INVENTORY MANAGEMENT SYSTEM")
print("========================================\n")

inventory = load_inventory()
show_menu()

while True:
    option = input("\nEnter option: ").strip()

    if option == "1":
        inventory.display_all()
    elif option == "2":
        add_product(inventory)
    elif option == "3":
        update_stock(inventory)
    elif option == "4":
        search_product(inventory)
    elif option == "5":
        print("\nSaving inventory...")
        save_inventory(inventory)
        print("Inventory saved successfully to " + FILENAME + ".")
    elif option == "6":
        print("\nSaving inventory before exit...")
        save_inventory(inventory)
        print("Inventory saved successfully.")
        print("\nThank you for using Inventory Management System.")
        print("Program terminated.")
        break
    else:
        print("Invalid option. Please enter 1 to 6.")
