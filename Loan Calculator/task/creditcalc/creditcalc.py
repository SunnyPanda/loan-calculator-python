import math

calculate = input('''What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal: ''')

if calculate == 'n':
    loan_principal = float(input('Enter the loan principal: '))
    monthly_payment = float(input('Enter the monthly payment: '))
    loan_interest = float(input('Enter the loan interest: '))
    interest_rate = loan_interest / 1200
    number_of_periods = math.ceil(math.log(monthly_payment / (monthly_payment - interest_rate * loan_principal), 1 + interest_rate))
    years = number_of_periods // 12
    months = number_of_periods % 12
    if years > 0 and months > 0:
        print(f'It will take {years} {"year" if years == 1 else "years"} and {months} {"month" if months == 1 else "months"}')
    elif years == 0:
        print(f'It will take {months} {"month" if months == 1 else "months"}')
    elif months == 0:
        print(f'It will take {years} {"year" if years == 1 else "years"}')
elif calculate == 'a':
    loan_principal = float(input('Enter the loan principal: '))
    number_of_periods = float(input('Enter the number of periods: '))
    loan_interest = float(input('Enter the loan interest: '))
    interest_rate = loan_interest / 1200
    annuity_payment = loan_principal * interest_rate * math.pow(1 + interest_rate, number_of_periods) / (math.pow(1 + interest_rate, number_of_periods) - 1)
    print(f'Your monthly payment = {math.ceil(annuity_payment)}!')
elif calculate == 'p':
    annuity_payment = float(input('Enter the annuity payment: '))
    number_of_periods = float(input('Enter the number of periods: '))
    loan_interest = float(input('Enter the loan interest: '))
    interest_rate = loan_interest / 1200
    loan_principal = annuity_payment / ((interest_rate * math.pow(1 + interest_rate, number_of_periods)) / (math.pow(1 + interest_rate, number_of_periods) - 1))
    print(f'Your loan principal = {round(loan_principal)}!')
