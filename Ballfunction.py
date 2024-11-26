import random

def viewm(messages):
    if messages:
        print('Your list contains ' + str(len(messages)) +' messages' +' If you wish to delete a message, enter its corresponding digit or the message to remove.')
        print('Enter back to go back.')
    while True:
        index = 0
        for i in messages:
            print('List '+ str(index) + ' ' + (i))
            index += 1
        yourInput = input()
        if yourInput in messages:
            messages.remove(yourInput)
            print ('Message ' +str(yourInput) + ' removed from the list.')
        elif yourInput.isdigit():
            index = int(yourInput)
            if 0 <= index < len(messages):
                removed_message = messages.pop(index)
                print (f"Message '{removed_message}', has been removed.")
        elif yourInput.lower() == 'back':
            return
    else:
        print('No message to load')

def call(messages):
    print("Enter 'y' to generate a random message,'n' to go back, '0' to exit.")
    while True:
        y = input()
        if y == 'y':
            print(random.choice(messages))
        elif y == 'n':
            return
        elif y == '0':
            exit()
        else:
            print ('Invalid input.')