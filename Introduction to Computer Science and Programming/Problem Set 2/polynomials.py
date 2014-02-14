def evaluate_poly(poly, x):
	index = 0
	total = 0
	for entry in poly:
		total += poly[index] * x**index
		index += 1
	print total

poly = (0.0, 0.0, 5.0, 9.3, 7.0)
x = -13
evaluate_poly(poly, x)
