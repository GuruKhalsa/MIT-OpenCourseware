1)
	^1.1) False
	^1.2) True
	^1.3) False
	^1.4) False
	X 1.5) True

2) print x = .2
	print x = 2.2
	print i = 1
"i starts at 0 and goes to range 2 which doesn't include 2"

3) 'atm'
	'tham'



4)
def findAll(wordList, lStr):
	result = []
	for w in wordList:
		wordcopy = w[:]
		strcopy = lStr[:]
		for c in wordcopy:
			if c in strcopy:
				wordcopy.remove(c)
				strcopy.remove(c)
			else
				break
		if wordcopy == [] and strcopy == []
			result.append(w)
	return result

5)
def addVectors(v1, v2): 
	"""assumes v1 and v2 are lists of ints. 
	Returns a list containing the pointwise sum of 
	the elements in v1 and v2. For example, 
	addVectors([4,5], [1,2,3]) returns [5,7,3],and 
	addVectors([], []) returns []. Does not modify inputs.""" 
	if len(v1) > len(v2): 
		result = v1 
		other = v2 
	else: 
		result = v2 
		other = v1
	total = result[:]
	count = 0
	for i in other: 
		total[count] += i
		count += 1 
	return total

6)
	6.1) 	1
			2
			0
	6.2) "No it doesn't terminate normally because 'result' is in the definition scope and is not a global variable so is therefore not available to be called outside of the definition."

7)
	7.1) 	n = 1
			n = 10

	7.2) O(n)

8) 	"Big O notation = b) upper bound"
	"Newton's Method = d) approximation"
	"recursion = a) induction"

10) "about right"

10) "about right"