allguestItems = {'Fruits': {'Bananas':'5','Warlord':'55'}, 'Appliances': {}, 'Mobile Phones': {}}

print ('Here are the available category you can choose from, choose one \n'
       'quit to exit.')
for k in allguestItems.keys():
    print(k)

def itemValues(itsValues, valuez):

        return valuez if valuez else 'none'


def itemKeys(itsKeys):
    item_list = ''
    for item, quantity in itsKeys.items():
        item_list += f"{item} {quantity}\n"
    return item_list

while True:
    category = input("\nEnter a category: ").strip()
    if category.lower() == 'quit':
        print("Exiting. Goodbye!")
        break

    if category in allguestItems:
        print(f"You selected {category} with items \n" + str(itemKeys(allguestItems[category]) ))


    else:
        allguestItems[category] = {}
        itemVal = input('Enter a nested key and its value: '.strip())
        itemKey = input()
        allguestItems[category][itemVal] = itemKey
        print(f"Added! {category}, {itemVal}, {itemKey}")
        print(allguestItems)
