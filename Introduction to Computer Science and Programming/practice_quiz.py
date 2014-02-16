1)
	1.1 True
	1.2 False
	1.3 True
	1.4 False
	1.5 

2)
True
True

3)
	3.1 cb a.
	3.2 O(n)

4)
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

5)
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

6)
	6.1 'b'
	6.2 print "Yes it will return 'b' because the elif statement only replaces the current character in the dictionary that occurs with the highest frequency if the new character occurs MORE frequently than the current character with the highest count.  Since 'b' and 'a' have the same count but 'b' occurs first, it will return 'b'."
	6.3 print "Yes other than the fact that an empty string will not be able to be counted or added/refrenced as a key in a dictionary.  Any other valid string should work."

7)
	7.1 a True
		b False
	7.2 [1, 2, 'a', 'a', 'b', (3, 4)]

8) print "About right."

9) print "About right."