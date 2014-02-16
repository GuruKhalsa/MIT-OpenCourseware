def getLines(): 
	inputs = [] 
	while True: 
		line = int(raw_input('Enter a positive integer, -1 to quit: '))
		if line == -1: 
			break 
		inputs.append(line) 
	total = 0 
	for e in inputs: 
		total += e 
	print total

getLines()