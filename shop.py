items = {"Coke": "2", "Pepsi": "3", "Sprite": "4", "Fanta": "5"}
total_price = 0
cheque = []
for key, value in items.items():
    print(f"{key}-{value}")
while True:
    chosen_item = input("Which item you want to buy (or type 'done' to finish): ")

    if chosen_item.lower() == 'done':
        break

    if chosen_item in items:
        item_price = float(items[chosen_item])
        total_price += item_price
        print(f"Price of {chosen_item} is {item_price}")
        # Add the item to the cheque
        cheque.append((chosen_item, item_price))
    else:
        print("Your item is not in the shop. Please choose a valid item.")

# Display cheque
print("\n--- Cheque ---")
for item, price in cheque:
    print(f"{item}: ${price:.2f}")

print(f"\nTotal Price: ${total_price:.2f}")
