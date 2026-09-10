print("====================================")
print("Smart Inventory Auditor")
print("Enter a stock quantity, or type 'quit' to stop.")
print("====================================")

total_inventory = 0
rejected_entries = 0

while True:
    entry = input("Enter stock quantity: ")

    if entry == "quit":
        break
    elif entry.startswith("-") and entry[1:].isdigit():
        print("ERROR: Negative stock is not allowed. Entry rejected.")
        rejected_entries += 1
    elif not entry.isdigit():
        print("ERROR: Please enter a whole number. Entry rejected.")
        rejected_entries += 1
    else:
        stock = int(entry)
        total_inventory += stock
        print("Accepted:", stock, "units. Total inventory:", total_inventory)

        if total_inventory > 500:
            print("ALERT: Overstock! Inventory exceeds 500 units.")
            break

print("\nAudit Report")
print("=====================")
print("Total Units Processed:", total_inventory)
print("Number of Failed/Rejected Entries:", rejected_entries)
