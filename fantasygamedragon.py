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

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)