def compute_deriv(poly):
	index = 0
	derivative = ()
	for entry in poly:
		if index != 0:
			derivative += (poly[index] * index,)
		index += 1
	print derivative

poly = (-13.39, 0.0, 17.5, 3.0, 1.0)
compute_deriv(poly)
