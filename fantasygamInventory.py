import sys

charInventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def inventorycall(inventory):
    print('Inventory')
    item_total = 0
    for item, quantity in inventory.items():
        print(f"{quantity} {item}")
        item_total += quantity

    print(f"Total number of items : {item_total}")


inventorycall(charInventory)

while True:
    newEntry = input("Want to add another entry? Yes or No \n")
    if newEntry == 'No':
        inventorycall(charInventory)
        sys.exit()
    elif newEntry == 'Yes':
        print('Enter the item and its quantity :')
        try:
            item1 = input("Item : ")
            quantity1 = int(input("Quantity : "))
        except ValueError:
            print('Not a valid quantity, try again')
            continue
        charInventory[item1] = quantity1
    inventorycall(charInventory)
