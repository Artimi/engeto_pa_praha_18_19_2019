import pprint
import tabulate


def compute_totals(L, r, n):
    """
    :param L: is the amount of money we are borrowing
    :param r: is monthly interest rate that bank offers us
    :param n: is the number of months in which we will pay our mortgage
    :return: dict with keys 'monthly_payment', 'total_amount', 'total_interest'
    """
    monthly_payment = L * (r * (1 + r) ** n) / ((1 + r) ** n - 1)
    total_amount = monthly_payment * n
    total_interest = total_amount - L
    return {
        'monthly_payment': monthly_payment,
        'total_amount': total_amount,
        'total_interest': total_interest
    }


def compute_months(L, r, monthly_payment):
    months = []
    payment = 1
    while int(L) > 0:
        monthly_interest = L * r
        monthly_payment = min(L, monthly_payment)
        principal = monthly_payment - monthly_interest
        L -= monthly_payment
        months.append({
            'payment': payment,
            'interest': int(monthly_interest),
            'principal': int(principal),
            'left_to_pay': int(L),
        })
        payment += 1
    return months


def main():
    try:
        borrow = float(input('How much do you want to borrow: '))
        rate = float(input('At what rate: '))
        years = float(input('How many years: '))
    except ValueError:
        print('Invalid argument!')
        return

    monthly_rate = rate / 100 / 12

    totals = compute_totals(
        L=borrow,
        r=monthly_rate,
        n=int(years * 12)
    )
    months = compute_months(
        L=totals['total_amount'],
        r=monthly_rate,
        monthly_payment=totals['monthly_payment']
    )
    pprint.pprint(totals)
    pprint.pprint(months)
    header = ['Payment', 'Interest', 'Principal', 'Left to Pay']
    table = [
        [month['payment'], month['interest'], month['principal'], month['left_to_pay']]
        for month in months
    ]
    print(tabulate.tabulate(table, header))



main()