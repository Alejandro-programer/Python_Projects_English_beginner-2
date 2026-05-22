# Show the program title.
print('Arithmetic Progression Generator')
print('\033[33m-=\033[m' * 10)

# Read the first term and the common difference.
first_term = int(input('First term: '))
common_difference = int(input('Common difference: '))
counter = 0
current_term = first_term

# Display the first 10 terms of the progression.
while counter != 10:
    print('{}'.format(current_term), end=' ')
    print('->', end=' ')
    counter += 1
    current_term += common_difference

print('END!')