from datetime import date

# Ask for the person's birth year.
birth_year = int(input('Birth year: '))

# Calculate the current age and the enlistment year.
current_year = date.today().year
age = current_year - birth_year
enlistment_year = birth_year + 18

# Show the proper enlistment message based on the age.
if age < 18:
    years_left = 18 - age
    print(
        'Anyone born in {} is {} years old in {}.\n'
        'There are still {} years left until enlistment.\n'
        'Your enlistment year will be {}.'.format(
            birth_year, age, current_year, years_left, enlistment_year
        )
    )
elif age == 18:
    print(
        'Anyone born in {} is {} years old in {}.\n'
        'You must enlist IMMEDIATELY!'.format(birth_year, age, current_year)
    )
else:
    overdue_years = age - 18
    print(
        'Anyone born in {} is {} years old in {}.\n'
        'You should have enlisted {} years ago.\n'
        'Your enlistment year was {}.'.format(
            birth_year, age, current_year, overdue_years, enlistment_year
        )
    )