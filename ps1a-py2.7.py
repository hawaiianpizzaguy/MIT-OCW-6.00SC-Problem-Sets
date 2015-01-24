# Problem Set 1
# Name: Connor Wyandt
# Collaborators:
# Time Spent: 0:45

# Retrieve input
balance = float(raw_input("Enter the outstanding balance on your credit card: "))
annualInterestRate = float(raw_input("Enter the annual credit card interest rate as a decimal: "))
minMonthlyPaymentRate = float(raw_input("Enter the minimum monthly payment rate as a decimal: "))
# Initialize state variables
numMonths = 1
minPayment = 0
interestPaid = 0
principalPaid = 0
totalAmtPaid = 0
# Monthly Interest Rate
monthlyInterestRate = annualInterestRate/12

def p():

    print("Month: " + str(numMonths))
    print("Minimum Monthly Payment: $" + str(minPayment))
    print("Interest Paid: $" + str(interestPaid))
    print("Principle Paid: $" + str(principalPaid))
    print("Total amount paid: $" + str(totalAmtPaid))
    print("Remaining Balance: $" + str(balance))
    print
    
for numMonths in range(1, 13, 1):
    # Minimum monthly payment of balance at start of the month
    minPayment = round(minMonthlyPaymentRate * balance, 2)
    totalAmtPaid += minPayment
    # Amt of monthly payment that goes to interest
    interestPaid = round(monthlyInterestRate * balance, 2)
    # Amt of principal paid off
    principalPaid = round(minPayment - interestPaid, 2)
    # Subtract monthly payment from outstanding balance
    balance -= round(principalPaid, 2)

    p()

print("RESULT")
print("Total amount paid: $" + str(totalAmtPaid))
print("Remaining balance: $" + str(balance))
