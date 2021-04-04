import argparse
import math


def output_periods(periods):
    start = 'It will take'
    joiner = 'and'
    end = 'to repay this loan!'

    years = periods // 12
    months = periods % 12

    years_str = str(f'{years} {"year" if years == 1 else "years"}')
    months_str = str(f'{months} {"month" if months == 1 else "months"}')

    if years > 0 and months > 0:
        return str(f'{start} {years_str} {joiner} {months_str} {end}')
    elif years == 0:
        return str(f'{start} {months_str} {end}')
    elif months == 0:
        return str(f'{start} {years_str} {end}')


def count_empty_args(arguments):
    count = 0
    for field in vars(arguments):
        if field is None:
            count += 1

    return count


def has_negative_args(arguments):
    is_negative = False
    args_array = [arguments.payment, arguments.periods, arguments.interest, arguments.principal]
    for arg in args_array:
        if arg is not None and float(arg) < 0:
            is_negative = True

    return is_negative


def check_input(arguments):
    count = count_empty_args(arguments)
    if count > 1 \
            or arguments.type is None \
            or arguments.type == 'diff' and arguments.payment \
            or arguments.interest is None \
            or has_negative_args(arguments):
        print('Incorrect parameters')
        return False
    return True


def calc_principal(periods, payment, interest_rate):
    principal = payment / ((interest_rate * math.pow(1 + interest_rate, periods)) / (math.pow(1 + interest_rate, periods) - 1))
    print(f'Your loan principal = {math.floor(principal)}!')
    calc_overpayment(periods * payment, math.floor(principal))


def calc_payment(periods, principal, interest_rate):
    payment = principal * interest_rate * math.pow(1 + interest_rate, periods) / (math.pow(1 + interest_rate, periods) - 1)
    print(f'Your annuity payment = {math.ceil(payment)}!')
    calc_overpayment(periods * math.ceil(payment), principal)


def calc_periods(principal, payment, interest_rate):
    periods = math.ceil(math.log(payment / (payment - interest_rate * principal), 1 + interest_rate))
    print(output_periods(periods))
    calc_overpayment(periods * payment, principal)


def calc_overpayment(result_payment, principal):
    print(f'Overpayment = {(result_payment - principal)}')


def calc_diff_payment(periods, principal, interest_rate, month):
    payment = math.ceil(principal / periods + interest_rate * (principal - principal * (month - 1) / periods))
    print(f'Month {month}: payment is {payment}')
    return payment


parser = argparse.ArgumentParser()
parser.add_argument('--type')
parser.add_argument('--payment')
parser.add_argument('--principal')
parser.add_argument('--periods')
parser.add_argument('--interest')

args = parser.parse_args()

if check_input(args):
    interest = float(args.interest) / 1200
    if args.type == 'annuity':
        if args.principal is None:
            calc_principal(int(args.periods), int(args.payment), interest)
        elif args.payment is None:
            calc_payment(int(args.periods), int(args.principal), interest)
        elif args.periods is None:
            calc_periods(int(args.principal), int(args.payment), interest)
    else:
        acc = 0
        for period in range(0, int(args.periods)):
            acc += calc_diff_payment(int(args.periods), int(args.principal), interest, period + 1)
        calc_overpayment(acc, int(args.principal))
