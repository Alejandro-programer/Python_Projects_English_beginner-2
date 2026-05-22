# Read two numbers and compare them.
number_1 = int(input('First number: '))
number_2 = int(input('Second number: '))

print(
    'The FIRST number is greater!'
    if number_1 > number_2
    else 'Both numbers are equal!'
    if number_1 == number_2
    else 'The SECOND number is greater!'
)