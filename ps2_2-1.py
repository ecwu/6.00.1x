def balances(minpay,balance,irt):
    irt = 0
    while balance > 0:
        unpaid = balance - minpay
        interest = unpaid * monthlyPaymentRate
        balance = interest + unpaid
        irt += 1
    return irt

def times(bal,adda):
    irt = 0
    minpay = bal/12
    while irt != 12:
        irt = balances(minpay,bal,irt)
        minpay += adda
    return minpay

balance = int(input('Input your balance'))
annualInterestRate = float(input('Input Annual Interest Rate'))
monthlyPaymentRate = annualInterestRate/12

if balance < 10:
    adda = 0.01
elif balance < 100:
    adda = 0.1
else:
    adda = 1

print(str(times(balance,adda)))

##Use too much Resource
