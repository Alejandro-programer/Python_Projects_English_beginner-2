# Initialize the value, sum, and counter.
value = 0
total_sum = 0
counter = 0

# Use a break condition when the sentinel value appears.
while True:
    value = int(input('Enter a value (999 to stop): '))
    if value == 999:
        break
    counter += 1
    total_sum += value

print('The sum of the {} values was {}!'.format(counter, total_sum))