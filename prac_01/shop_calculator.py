num_of_items = int(input("Number of items: "))
total_price = 0

while num_of_items < 0:
    print("Invalid number of items")
    num_of_items = int(input("Number of items: "))

else:
    for i in range(num_of_items):
        price = float(input(f"Price of item {i + 1}: "))
        if price < 0:
            print("Invalid price!")
        total_price += price

if total_price > 100:
    total_price *= 0.9

print(f"Total price for {num_of_items} items is ${total_price:.2f}")