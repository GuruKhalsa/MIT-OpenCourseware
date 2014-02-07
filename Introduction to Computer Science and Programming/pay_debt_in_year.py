balance = float(raw_input('Enter the outstanding balance on your credit card:'))
annual_interest_rate = float(raw_input('Enter the annual credit card interest rate as a decimal:'))
monthly_interest_rate = annual_interest_rate/12
minimum_monthly_payment = 0
new_balance = balance

while new_balance > 0:
	new_balance = balance
	minimum_monthly_payment += 10
	months = 0
	while new_balance > 0 and months < 12:
		new_balance = new_balance * (1 + monthly_interest_rate) - minimum_monthly_payment
		months += 1 
	
	
	
print '\nRESULT'
print 'Fixed Minimum Monthly Payment= ' + str(minimum_monthly_payment)
print 'Number of Months= ' + str(months)
print 'Balance= ' + str(round(new_balance, 2))
