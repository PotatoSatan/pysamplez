supplies = []

while True:
        print('Enter a supply : ' + str(len(supplies) + 1) +' or enter 0 to stop')
        supply = input()

        if supply == '0':
            break
        supplies = supplies + [supply]
print ('Here are the total number of supplies : ' + str(len(supplies)))
print ('Name of supplies are the following')
for supply in range(len(supplies)):
    print('Count of ' + str(supply + 1) + ' supply: ' + supplies[supply])


print('Check if your supply exists? Y or N')
yesorno = input()
if yesorno  == 'Y':
    while True:
        print ('Enter supply name or exit to exit')
        supplyName = input()
        if supplyName in supplies:
            print ('Supply ' +supplyName +' is in the table')
        elif supplyName.lower() == 'exit':
            continue
        else:
            print (supplyName +' does not exist.')
else:
    exit()