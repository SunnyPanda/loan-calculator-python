import math

principal = int(input('Enter the loan principal: '))
calculate = input('''What do you want to calculate?
type "m" - for number of monthly payments,
type "p" - for the monthly payment: ''')

if calculate == 'm':
    monthly_payment = int(input('Enter the monthly payment: '))
    months = math.ceil(principal / monthly_payment)
    if months == 1:
        print('It will take', months, 'month to repay the loan')
    else:
        print('It will take', months, 'months to repay the loan')
elif calculate == 'p':
    months = int(input('Enter the number of months: '))
    monthly_payment = math.ceil(principal / months)
    last_payment = principal - (months - 1) * monthly_payment
    if last_payment == monthly_payment:
        print('Your monthly payment =', monthly_payment)
    else:
        print('Your monthly payment =', monthly_payment, 'and the last payment =', last_payment)
