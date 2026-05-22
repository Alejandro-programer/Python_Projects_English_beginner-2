# Read an integer and let the user choose the conversion base.
number = int(input('Enter an integer: '))
print(
    'Choose one of the bases for conversion:\n'
    ' [1] Convert to BINARY\n'
    ' [2] Convert to OCTAL\n'
    ' [3] Convert to HEXADECIMAL'
)
option = int(input('Your option: '))

# Convert the number according to the chosen option.
print('{} converted to BINARY is {}'.format(number, bin(number)[2:]) if option == 1 else '')
print('{} converted to OCTAL is {}'.format(number, oct(number)[2:]) if option == 2 else '')
print('{} converted to HEXADECIMAL is {}'.format(number, hex(number)[2:]) if option == 3 else '')