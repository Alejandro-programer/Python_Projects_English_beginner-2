# Ask for a number to calculate its factorial.
number = int(input('Enter a number\n to calculate its factorial: '))
counter = number
factorial = 1

# Display the factorial process step by step.
print('Calculating {}! = '.format(number), end=' ')
while counter > 0:
    print('{}'.format(counter), end=' ')
    print(' X ' if counter > 1 else ' = ', end=' ')
    factorial *= counter
    counter -= 1

print('{}'.format(factorial))