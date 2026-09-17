def get_valid_input():
    entry = input("Enter stock quantity: ")

    if entry == "quit":
        return "quit"
    elif entry.startswith("-") and entry[1:].isdigit():
        print("ERROR: Negative stock is not allowed. Entry rejected.")
        return None
    elif not entry.isdigit():
        print("ERROR: Please enter a whole number. Entry rejected.")
        return None
    else:
        return int(entry)


def process_delivery(current_total, new_value):
    return current_total + new_value


def calculate_tax(amount):
    return amount * 0.10


def generate_report(total_units, failed_attempts):
    print("\nAudit Report")
    print("=====================")
    print("Total Deliveries Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)


print("====================================")
print("Smart Inventory Auditor")
print("Enter a stock quantity, or type 'quit' to stop.")
print("====================================")

total_inventory = 0
deliveries_processed = 0
rejected_entries = 0

while True:
    value = get_valid_input()

    if value == "quit":
        break
    elif value is None:
        rejected_entries += 1
    else:
        total_inventory = process_delivery(total_inventory, value)
        deliveries_processed += 1
        tax = calculate_tax(value)
        print("Accepted:", value, "units. Total inventory:", total_inventory)
        print("Tax for this delivery:", tax)

generate_report(deliveries_processed, rejected_entries)
