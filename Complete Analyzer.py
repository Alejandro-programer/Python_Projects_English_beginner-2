# Initialize the counters and tracking variables.
age_sum = 0
average_age = 0
oldest_man_name = ''
oldest_man_age = 0
women_under_twenty = 0

# Read the data for four people.
for person_number in range(1, 5):
    print('---- {}th PERSON ----'.format(person_number))
    name = str(input('Name: ')).strip().upper()
    age = int(input('Age: '))
    sex = str(input('Sex [M/F]: ')).strip().upper()

    # Keep track of the age average.
    age_sum += age
    average_age = age_sum / 4

    # Check the oldest man in the group.
    if sex == 'M' and age > oldest_man_age:
        oldest_man_age = age
        oldest_man_name = name

    # Count women younger than 20 years old.
    if sex == 'F' and age < 20:
        women_under_twenty += 1

# Display the final results.
print('The average age of the group is {} years'.format(average_age))
print('The oldest man is {} and he is {} years old'.format(oldest_man_name, oldest_man_age))
print('There are {} women under 20 years old in total'.format(women_under_twenty))