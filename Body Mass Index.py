# Read the person's weight and height.
weight = float(input('What is your weight (Kg)? '))
height = float(input('What is your height (m)? '))
bmi = weight / (height * height)

# Show the BMI value and its classification.
print('Your BMI is {:.2f}'.format(bmi))
if bmi < 18.5:
    print('You are UNDERWEIGHT!')
elif bmi < 25:
    print('You are at a NORMAL WEIGHT!')
elif bmi < 30:
    print('You are OVERWEIGHT!')
elif bmi < 40:
    print('You are OBESE!')
else:
    print('You are SEVERELY OBESE!')