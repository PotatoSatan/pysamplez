import GridtoPrint

print('Enter a number')

while True:
    try:
        number = int(input())
        break
    except ValueError:
     print('Not an integer')

while number != 1:
    number = number // 2
    print(number)

print('You reached 1.')

