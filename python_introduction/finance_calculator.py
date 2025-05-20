#Personal Finance Calculator
income = input("Enter your monthly income: ")
expenses = input("Enter your monthly expenses: ")

#Do the calculation for monthly savings
savings = int(income) - int(expenses)

#Annual savings calculator
interest = 0.05
projectedSavings = int(savings * 12 + (savings * 12 * interest))

print (f'Your monthly savings are ${savings}')
print (f'Projected savings after one year, with interest, is: $int({projectedSavings})')


