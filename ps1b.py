# Problem Set 1
# Name: Connor Wyandt
# Collaborators:
# Time Spent: 0:20

# Retrieve input
initialBalance = float(input("Enter the outstanding balance on your credit card: "))
annualInterestRate = float(input("Enter the annual credit card interest rate as a decimal: "))
# Initialize state variables
monthlyPayment = 0
monthlyInterestRate = annualInterestRate/12
balance = initialBalance
numMonths = 0
# Test increasing amounts of monthlyPayment
# until it can be paid off in a year
while(balance > 0):

    monthlyPayment += 10
    balance = initialBalance
    numMonths = 0

    # Simulate passage of time until outstanding balance is paid off
    # Each iteration represents 1 month
    while(numMonths < 12 and balance > 0):

        # Count this as a new month
        numMonths += 1
        
        # Interest for the month
        interest = monthlyInterestRate * balance
        
        # Subtract monthly payment from outstanding balance
        balance -= monthlyPayment
        
        # Add interest
        balance += interest
        
# Round final balance to 2 decimal places
balance = round(balance, 2)

print ("RESULT")
print ("Monthly payment to pay off debt in 1 year: $" + str(monthlyPayment))
print ("Number of months needed: " + str(numMonths))
print ("Balance: $" + str(balance))
