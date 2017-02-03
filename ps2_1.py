interestrate = 0.18/12.0
def payment(balance,time):
    while time != 0:
        minpay = balance * 0.02
        unpaid = balance - minpay
        interest = unpaid * interestrate
        print('Minimum Payment: ' + str(minpay) + 'Unpaid Balance: ' + str(unpaid) + 'Interest: ' +str(interest))
        time -= 1
        balance = interest + unpaid
    return 0
balance = float(input('Input your balance'))
time = int(input('Input Months'))

payment(balance,time)