# Read a number and display its multiplication table.
number = int(input('Enter a number to see its multiplication table: '))
for multiplication in range(0, 10):
    print('{} X {} = {}'.format(number, multiplication, number * multiplication))