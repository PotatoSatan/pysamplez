import sys
def addToInventory(inventory, addedItems):
    for items in addedItems:
        if items in inventory:
            inventory[items] += 1
        else:
            inventory[items] = 1
    return inventory

def displayInventory(inventory):
    print('Inventory')
    item_total = 0
    for items, quantity in inventory.items():
        print(f"{quantity} {items}")
        item_total += quantity
    print(f"Your total items :{item_total}")

def addItem(inventory, addition, quantity):
    for items in addition:
        if items in inventory:
            inventory[items] += quantity
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
displayInventory(inv)
newValue = input('Add a new entry? Y or N \n')
if newValue == 'N':
    sys.exit()
elif newValue == 'Y':
    enterValue = input('Enter the item \n')
    enterValueQuantity = input('Enter is quantity, leave blank if 0 \n')
    if enterValueQuantity == '0':
        inv = addItem(inv, enterValue, enterValueQuantity)
        displayInventory(inv)
    else:
        inv = addItem(inv, enterValue, enterValueQuantity)
        displayInventory(inv)

