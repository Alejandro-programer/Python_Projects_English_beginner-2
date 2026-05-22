from time import sleep

# Read the initial values.
first_number = int(input('Enter the first value: '))
second_number = int(input('Enter the second value: '))
exit_program = False

while not exit_program:
    # Show the menu on every loop.
    print('=-=' * 10)
    print('[ 1 ] add')
    print('[ 2 ] multiply')
    print('[ 3 ] greater value')
    print('[ 4 ] new numbers')
    print('[ 5 ] exit the program')
    option = int(input('Choose: '))
    print('=-=' * 10)
    sleep(1)

    # Execute the selected option.
    if option == 1:
        print('{} + {} = {}'.format(first_number, second_number, first_number + second_number))
    elif option == 2:
        print('{} X {} = {}'.format(first_number, second_number, first_number * second_number))
    elif option == 3:
        greater_number = max(first_number, second_number)
        print('The greater number between {} and {} is {}'.format(first_number, second_number, greater_number))
    elif option == 4:
        print('Enter the numbers again:')
        first_number = int(input('Enter the first value: '))
        second_number = int(input('Enter the second value: '))
    elif option == 5:
        exit_program = True
    else:
        print('Invalid option. Try again:')

print('See you later!!!')