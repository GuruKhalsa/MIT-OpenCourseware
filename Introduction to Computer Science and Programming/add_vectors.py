def addVectors(v1, v2):
	if len(v1) > len(v2):
		larger = v1
		smaller = v2
	else:
		larger = v2
		smaller = v1
	v3 = larger[:]
	count = 0
	for i in smaller:
		v3[count] += i
		count += 1
	print v3
	return v3

addVectors([4,5], [1,2,3])