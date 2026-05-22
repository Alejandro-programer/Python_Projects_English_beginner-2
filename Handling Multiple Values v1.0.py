# Initialize the running sum and count.
total_sum = 0
counter = 0
stop = False

# Keep reading values until 999 is entered.
while not stop:
    number = int(input('Enter a number [999 to stop]: '))
    if number == 999:
        stop = True
    else:
        total_sum += number
        counter += 1

print('You entered {} numbers and the sum between them was {}'.format(counter, total_sum))