# Problem Set 1
# Name: Connor Wyandt
# Collaborators:
# Time Spent: 0:30

# Retrieve input
initialBalance = float(raw_input("Enter the outstanding balance on your credit card: "))
interestRate = float(raw_input("Enter the annual credit card interest rate as a decimal: "))
# Initialize state variables
balance = initialBalance
lowPayment = balance/12
highPayment = (balance*(1+(interestRate/12))**12)/12

# Use bisection search until the search space is sufficiently small
while (True):

    balance = initialBalance
    monthlyPayment = (lowPayment + highPayment)/2

    # Simulate passage of time until outstanding balance is paid off
    # Each iteration represents 1 month
    for month in range(1, 13):
        interest = round(balance*interestRate/12, 2)
        balance += interest - monthlyPayment
        if (balance <= 0):
            break
        
    if(highPayment - lowPayment < 0.005):
        # Bisection search space is small enough
        # Print result
        print("RESULT")

        # Round monthly payment up to the nearest cent
        monthlyPayment = round(monthlyPayment + 0.004999, 2)
        print "Monthly payment to pay off debt in 1 year:", round(monthlyPayment,2)

        # Recompute remaining balance and the number of months needed
        balance = initialBalance
        for month in range(1, 13):
            interest = round(balance*interestRate/12, 2)
            balance += interest - monthlyPayment
            if(balance <= 0):
                break
        print("Number of months needed: " + str(month))
        balance = round(balance, 2)
        print("Balance: " + str(balance))
        break
    elif(balance < 0):
        #Paying too much
        highPayment = monthlyPayment
    else:
        #Paying too little
        lowPayment = monthlyPayment
