birthdays = {'Alice': 'Mar 04', 'Ben': 'Dec 20'}

while True:
    print(f"Enter a name and we'll check if it exists. (blank to exit)")
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of' + name)
    else:
        print(f"" + name + ' does not exist on the database. Enter his/her birthday so I can have it added.')
        birth = input()
        birthdays[name] = birth
        print(name + ' is now added.')
