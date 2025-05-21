#Personal Finance Calculator
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your monthly expenses: "))

#Do the calculation for monthly savings
monthly_savings = float(monthly_income) - float(monthly_expenses)

#Annual savings calculator
interest = 0.05
projectedSavings = float(monthly_savings * 12 + (monthly_savings * 12 * interest))

print (f'Your monthly savings are ${monthly_savings}.')
print (f'Projected savings after one year, with interest, is: ${projectedSavings}.')


