def findAll(wordList, lStr):
	result = []
	for w in wordList:
		wordcopy = w[:]
		strcopy = lStr[:]
		for c in wordcopy:
			if c in strcopy:
				wordcopy.replace(c, '')
				strcopy.replace(c, '')
				print wordcopy
				print strcopy
			else:
				break
		print w
		if wordcopy == [] and strcopy == []:
			result.append(w)
			print result
	print result
	return result

words = ['here', 'ereh', 'glib', 'balloon', 'reeh', 'heer']
stringthing = 'here' 
print findAll(words, stringthing)