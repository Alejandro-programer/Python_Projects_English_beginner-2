# Display the Fibonacci program header.
print('-' * 10)
print('Fibonacci Sequence')
print('-' * 10)

# Start the sequence and ask how many terms should be shown.
first_term = 0
second_term = 1
shown_terms = 0
total_terms = int(input('How many terms do you want to show? '))

print('~' * 20)

# Print the requested amount of Fibonacci terms.
while shown_terms < total_terms:
    if shown_terms == 0:
        print(first_term, end=' ')
    elif shown_terms == 1:
        print('-> {}'.format(second_term), end=' ')
    else:
        next_term = first_term + second_term
        print('-> {}'.format(next_term), end=' ')
        first_term = second_term
        second_term = next_term
    shown_terms += 1

print('END')