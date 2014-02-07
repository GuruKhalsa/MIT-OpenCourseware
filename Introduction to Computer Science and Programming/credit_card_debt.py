balance = float(raw_input('What is the outstanding balance of the credit card?\n'))
annual_interest_rate = float(raw_input('What is the annual interest rate of the credit card?\n'))
minimum_payment_rate = float(raw_input('What is the minimum monthly payment rate of the credit card?\n'))

monthly_interest_rate = annual_interest_rate/12

for i in range(1,13):
	monthly_payment = minimum_payment_rate * balance
	interest_paid = monthly_interest_rate * balance
	principle_paid = monthly_payment - interest_paid
	balance = balance - principle_paid
	print '\nYear ' + str(i)
	print 'Monthly Payment= $' + str(round(monthly_payment, 2))
	print 'Principle Paid= $' + str(round(principle_paid, 2))
	print 'Remaing Balance= $' + str(round(balance, 2))