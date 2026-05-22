# Read the two grades.
grade_1 = float(input('First grade: '))
grade_2 = float(input('Second grade: '))
average = (grade_1 + grade_2) / 2

# Show the average and the student's status.
print('With grades {} and {}, the student\'s average was {}'.format(grade_1, grade_2, average))
if average >= 7:
    print('The student has PASSED!')
elif average >= 5:
    print('The student is in RECOVERY')
else:
    print('The student has FAILED!')