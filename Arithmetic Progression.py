# Display the title of the arithmetic progression program.
print('=' * 30)
print('      10 TERMS OF AN AP      ')
print('=' * 30)

# Read the first term and the common difference.
first_term = int(input('First term: '))
common_difference = int(input('Common difference: '))
tenth_term = first_term + (10 - 1) * common_difference

# Print the 10 terms of the progression.
for progression_term in range(first_term, tenth_term + common_difference, common_difference):
    print('{}'.format(progression_term), end=' -> ')
print('END')