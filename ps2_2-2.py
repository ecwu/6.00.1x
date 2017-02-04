def balances(minpay,balance,irt):
    while balance > 0:
        unpaid = balance - minpay
        interest = unpaid * monthlyPaymentRate
        balance = interest + unpaid
        irt += 1
    return irt

def times(bal):
    irt = 0
    minpay = int(bal/12)
    while irt != 12:
        irt = balances(minpay,bal,irt)
        minpay += 1
    return minpay

balance = int(input('Input your balance'))
annualInterestRate = float(input('Input Annual Interest Rate'))
monthlyPaymentRate = annualInterestRate/12


print(str(times(balance)))

##Use too much Resource
