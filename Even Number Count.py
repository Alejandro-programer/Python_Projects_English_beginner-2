from time import sleep

# Introduce the even counting activity.
print('Let\'s count the even numbers up to 50 :)')
sleep(5)
print('Let\'s go!')
sleep(2)

# Print all even numbers from 0 to 50.
for even_number in range(0, 52, 2):
    print(even_number, end=' ')

print('Done ;)')