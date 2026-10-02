LINE = "------------------------------------------------"


def find_product(inventory, product_id):
    for product in inventory:
        if product["id"] == product_id:
            return product
    return None


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


def format_product(product):
    return ("ID: " + product["id"]
            + " | Name: " + product["name"]
            + " | Price: $" + format(product["price"], ".2f")
            + " | Stock: " + str(product["stock"]))


def display_all(inventory):
    print("\nCurrent Inventory")
    print(LINE)
    if not inventory:
        print("No products in inventory.")
    for product in inventory:
        print(format_product(product))
    print(LINE)


def add_product(inventory):
    print("\nAdd New Product")
    product_id = input("Product ID: ").strip().upper()
    if not product_id:
        print("\nERROR: Product ID cannot be empty.")
        return
    if find_product(inventory, product_id) is not None:
        print("\nERROR: Product ID already exists.")
        return
    name = input("Product Name: ").strip()
    price = get_float("Price: ")
    stock = get_int("Stock Quantity: ")
    inventory.append({"id": product_id, "name": name, "price": price, "stock": stock})
    print("\nProduct added successfully!")


def update_stock(inventory):
    print("\nUpdate Stock")
    product_id = input("Enter Product ID: ").strip().upper()
    product = find_product(inventory, product_id)
    if product is None:
        print("\nProduct not found.")
        return
    print("\nProduct Found:")
    print("Name: " + product["name"])
    print("Current Stock: " + str(product["stock"]))
    product["stock"] = get_int("\nNew Stock Quantity: ")
    print("\nStock updated successfully!")


def search_product(inventory):
    print("\nSearch Product")
    product_id = input("Enter Product ID: ").strip().upper()
    product = find_product(inventory, product_id)
    if product is None:
        print("\nProduct not found.")
        return
    print("\nProduct Found")
    print(LINE)
    print("ID: " + product["id"])
    print("Name: " + product["name"])
    print("Price: $" + format(product["price"], ".2f"))
    print("Stock: " + str(product["stock"]))
    print(LINE)


def show_menu():
    print("\n----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("6. Exit")
    print("----------------------------")


print("========================================")
print("INVENTORY MANAGEMENT SYSTEM")
print("========================================\n")

inventory = [
    {"id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15},
    {"id": "P002", "name": "Mouse", "price": 25.50, "stock": 40},
    {"id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25},
]
show_menu()

while True:
    option = input("\nEnter option: ").strip()

    if option == "1":
        display_all(inventory)
    elif option == "2":
        add_product(inventory)
    elif option == "3":
        update_stock(inventory)
    elif option == "4":
        search_product(inventory)
    elif option == "6":
        print("\nThank you for using Inventory Management System.")
        print("Program terminated.")
        break
    else:
        print("Invalid option. Please enter 1 to 4 or 6.")
