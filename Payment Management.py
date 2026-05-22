# Show the store title and ask for the purchase price.
print('\033[33m=' * 12, '\033[mFASHION SPACE', '\033[33m=\033[m' * 12)
purchase_price = float(input('Purchase price: $'))

# Present the payment options.
print('PAYMENT METHODS')
print('[ 1 ] cash/check upfront')
print('[ 2 ] card upfront')
print('[ 3 ] 2 installments on the card')
print('[ 4 ] 3 or more installments on the card')
option = int(input('Which option?\n'))

# Calculate the final price according to the selected method.
if option == 1:
    final_price = purchase_price - ((purchase_price * 10) / 100)
    print('Your ${} purchase will cost ${:.2f} in the end'.format(purchase_price, final_price))
elif option == 2:
    final_price = purchase_price - ((purchase_price * 5) / 100)
    print('Your ${} purchase will cost ${:.2f} in the end'.format(purchase_price, final_price))
elif option == 3:
    print('Your purchase will be split into 2 installments of ${:.2f}'.format(purchase_price / 2))
elif option == 4:
    installments = int(input('How many installments? '))
    installment_value = (purchase_price + ((purchase_price * 20) / 100)) / installments
    final_price = purchase_price + ((purchase_price * 20) / 100)
    print('Your purchase will be split into {} installments of ${:.2f} WITH INTEREST'.format(installments, installment_value))
    print('Your ${} purchase will cost ${:.2f} in the end.'.format(purchase_price, final_price))
else:
    print('INVALID payment option')