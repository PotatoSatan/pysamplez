allguestItems = {'Fruits': {'Bananas':'5'}, 'Appliances': {}, 'Mobile Phones': {}}

print ('Here are the available category you can choose from, choose one \n'
       'quit to exit.')
for k in allguestItems.keys():
    print(k)

def itemValues(itsValues):
    valuez = ', '.join(itsValues.values())
    return valuez if valuez else 'none'

def itemKeys(itsKeys):
    keys = ','.join(itsKeys.keys())
    return keys if keys else 'none'

while True:
    category = input("\nEnter a category: ").strip()
    if category.lower() == 'quit':
        print("Exiting. Goodbye!")
        break

    if category in allguestItems:
        print(f"You selected {category}")
        keys = itemKeys(allguestItems[category])
        valuez = itemValues(allguestItems[category])
        print(f"{keys},{valuez}")