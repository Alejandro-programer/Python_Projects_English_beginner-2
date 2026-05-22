from datetime import date

# Initialize the counter and get the current year.
adults = 0
current_year = date.today().year

# Read the birth year of seven people.
for person in range(1, 8):
    birth_year = int(input('In which year was the {}th person born? '.format(person)))
    if current_year - birth_year > 18:
        adults += 1

# Show the number of adults and minors.
print('In total, we had {} adults'.format(adults))
print('And we also had {} minors'.format(person - adults))