charInventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def inventoryCall(inventory):
    print('Inventory')
    item_total = 0
    for item, quantity in inventory.items():
        print(f"{quantity} {item}")
        item_total += quantity

    print(f"Total number of items : {item_total}")


inventoryCall(charInventory)