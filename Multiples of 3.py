from time import sleep

# Initialize the total sum and counter.
total_sum = 0
counter = 0

print('Hello!!!')
sleep(1)
print('\033[33mLet\'s count the multiples of 3 up to 500 and add them at the end :)\033[m')
sleep(5)
print('\033[34mHere are all the multiples of 3 up to 500 ;)\033[m')

# Iterate over odd numbers and keep only those divisible by 3.
for multiple in range(1, 501, 2):
    if multiple % 3 == 0:
        print(multiple, end=' ')
        counter += 1
        total_sum += multiple

print('\n \033[34mThe sum of all {} requested values is {}\033[m'.format(counter, total_sum))
print('\033[33mThank you!!!\033[m \n \033[35mAnd have a great afternoon!!!\033[m')