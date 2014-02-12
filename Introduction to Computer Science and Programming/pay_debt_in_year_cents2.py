initial_balance = float(raw_input('Enter the outstanding balance on your credit card:'))
annual_interest_rate = float(raw_input('Enter the annual credit card interest rate as a decimal:'))
monthly_interest_rate = annual_interest_rate/12
balance = initial_balance
low_pmt = balance/12
high_pmt = (balance *(1+ monthly_interest_rate)**12)/12
min_pmt = (low_pmt + high_pmt)/2
epsilon = .01

while high_pmt - low_pmt > epsilon:
	balance = initial_balance

	for months in range(1, 13):
		balance = balance * (1 + monthly_interest_rate) - min_pmt

	if balance < 0:
		high_pmt = min_pmt
		print 'High pmt =', high_pmt
	elif balance > 0:
		low_pmt = min_pmt
		print 'Low pmt =', low_pmt
	min_pmt = (low_pmt + high_pmt)/2

print min_pmt
print months