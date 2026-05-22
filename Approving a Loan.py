# Read the house price, buyer salary, and financing time.
house_value = float(input('House value: $'))
buyer_salary = float(input('Buyer salary: $'))
financing_years = int(input('How many years of financing? '))

# Calculate the monthly installment and compare it to 30% of the salary.
monthly_installment = house_value / (financing_years * 12)
salary_limit = (buyer_salary * 30) / 100

if monthly_installment < salary_limit:
    print(
        'To pay for a house worth ${:.2f} in {} years, the installment will be ${:.2f}.\n'
        'Loan \033[1mapproved!!!\033[m'.format(house_value, financing_years, monthly_installment)
    )
else:
    print(
        'To pay for a house worth ${:.2f} in {} years, the installment will be ${:.2f}.\n'
        'Loan \033[1mdenied!!!\033[m'.format(house_value, financing_years, monthly_installment)
    )