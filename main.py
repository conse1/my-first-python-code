lux_inventory = []
step = 0

while step < 3:
    item = input("Enter item name: ")
    if item == "dota":
        print("scam")
    else:
        lux_inventory.append(item)
        print("approved")

    step = step + 1

print(lux_inventory)