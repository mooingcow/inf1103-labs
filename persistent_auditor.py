def get_valid_input():
    name = input("Enter Product Name: ")

    if name == "quit":
        return "quit"

    entry = input("Enter Quantity: ")

    if entry.startswith("-") and entry[1:].isdigit():
        print("ERROR: Negative stock is not allowed. Entry rejected.")
        return None
    elif not entry.isdigit():
        print("ERROR: Please enter a whole number. Entry rejected.")
        return None
    else:
        return name, int(entry)


def process_delivery(current_total, new_value):
    return current_total + new_value


def calculate_tax(amount):
    return amount * 0.10


def load_inventory():
    total = 0
    history = []
    try:
        with open("inventory.txt", "r") as f:
            lines = f.read().splitlines()
        total = int(lines[0])
        for line in lines[1:]:
            order_id, name, qty = line.split(",")
            history.append((int(order_id), name, int(qty)))
    except (FileNotFoundError, ValueError, IndexError):
        pass
    return total, history


def generate_report(total_units, failed_attempts):
    print("\nAudit Report")
    print("=====================")
    print("Total Deliveries Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)


print("====================================")
print("Smart Inventory Auditor")
print("Enter a product name, or type 'quit' to stop.")
print("====================================")

total_inventory, history = load_inventory()
deliveries_processed = 0
rejected_entries = 0

print("\nCurrent Orders:\n")
for order_id, name, qty in history:
    print(str(order_id) + ", " + name + ", " + str(qty))
print("Total inventory:", total_inventory)
print()

while True:
    value = get_valid_input()

    if value == "quit":
        break
    elif value is None:
        rejected_entries += 1
    else:
        name, qty = value
        order_id = history[-1][0] + 1 if history else 1001
        history.append((order_id, name, qty))
        total_inventory = process_delivery(total_inventory, qty)
        deliveries_processed += 1
        print("\nNew Order Added:")
        print(str(order_id) + "," + name + "," + str(qty))
        print("Accepted:", qty, "units. Total inventory:", total_inventory)
        print("Tax for this delivery:", calculate_tax(qty))
        print()

generate_report(deliveries_processed, rejected_entries)
