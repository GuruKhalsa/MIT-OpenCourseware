balance = float(raw_input('Enter the outstanding balance on your credit card:'))
annual_interest_rate = float(raw_input('Enter the annual credit card interest rate as a decimal:'))
monthly_interest_rate = annual_interest_rate/12
new_balance = balance

lower_payment = balance / 12.0 
upper_payment = (balance * (1 + monthly_interest_rate) ** 12.0) / 12.0
epsilon = .005
minimum_monthly_payment = (upper_payment + lower_payment) / 2

while abs(upper_payment - lower_payment) >= epsilon:
	print '\nmin payment=', minimum_monthly_payment
	print 'lower payment=', lower_payment
	print 'Upper payment=', upper_payment
	if new_balance < balance:
		lower_payment = minimum_monthly_payment
	else:
		upper_payment = minimum_monthly_payment
	minimum_monthly_payment = (upper_payment + lower_payment) / 2
	new_balance = balance
	months = 0
	while (abs(upper_payment - lower_payment) >= epsilon) and months <= 12:
		new_balance = new_balance * (1 + monthly_interest_rate) - minimum_monthly_payment
		months += 1 
	
	
	
print '\nRESULT'
print 'Fixed Minimum Monthly Payment = ' + str(minimum_monthly_payment)
print 'Number of Months = ' + str(months)
print 'Balance = ' + str(round(new_balance, 2))
