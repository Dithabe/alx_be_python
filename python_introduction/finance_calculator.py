#Personal Finance Calculator
income = input("Enter your monthly income: ")
expenses = input("Enter your monthly expenses: ")

#Do the calculation for monthly savings
monthly_savings = int(income) - int(expenses)

#Annual savings calculator
interest = 0.05
projectedSavings = int(monthly_savings * 12 + (monthly_savings * 12 * interest))

print (f'Your monthly savings are ${monthly_savings}')
print (f'Projected savings after one year, with interest, is: ${projectedSavings}')


