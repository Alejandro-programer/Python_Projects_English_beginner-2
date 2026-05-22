# Read a number and count its divisors.
divisor_count = 0
number = int(input('Enter a number: '))

for current_number in range(1, number + 1):
    if number % current_number == 0:
        print('\033[33m', end=' ')
        divisor_count += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(current_number), end=' ')

# Show whether the number is prime.
print('\n\033[mThe number {} was divisible {} times'.format(number, divisor_count))
print('That is why it IS PRIME!' if divisor_count == 2 else 'And that is why it is NOT PRIME')