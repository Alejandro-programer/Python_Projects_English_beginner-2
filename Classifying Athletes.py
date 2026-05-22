from datetime import date

# Ask for the athlete's birth year.
birth_year = int(input('Birth year: '))
age = date.today().year - birth_year

# Show the athlete's age and category.
print('The athlete is {} years old'.format(age))
if age < 9:
    print('Classification: \033[33mCHILD\033[m')
elif age < 14:
    print('Classification: \033[33mYOUTH\033[m')
elif age < 19:
    print('Classification: \033[33mJUNIOR\033[m')
elif age < 25:
    print('Classification: \033[33mSENIOR\033[m')
else:
    print('Classification: MASTER')