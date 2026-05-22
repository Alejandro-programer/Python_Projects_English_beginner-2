# Initialize the sum and the counter.
total_sum = 0
even_counter = 0

# Read six values and sum only the even ones.
for counter in range(1, 7):
    number = int(input('Enter the {} value: '.format(counter)))
    if number % 2 == 0:
        total_sum += number
        even_counter += 1

print('You entered {} EVEN numbers and their sum was {}'.format(even_counter, total_sum))