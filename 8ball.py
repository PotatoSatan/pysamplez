import Ballfunction
import random


messages = []


while True:
    print('Enter any message : ', ' enter 0 for Magic 8-Ball, 1 to view your list')
    message = input()

    if message == '0':
        ballfuncs.call(messages)
    elif message == '1':
        ballfuncs.viewm(messages)
    else:
        messages.append(message)

