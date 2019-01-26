# 8.
# Write a program to compute the frequency of the words from the input. 
# The output should output after sorting the key alphanumerically.
# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3. Then, the output should be:
# 2:2
# 3.:1
# 3?:1 
# New:1 
# Python:5 
# Read:1 
# and:1 
# between:1 
# choosing:1 
# or:2
# to:1

def compute_frequency():
	sentence = input()
	mylist = sentence.split()
	mydict = {}
	for x in mylist:
		if x not in mydict:
			mydict[x] = 1
		else:
			mydict[x] += 1
	for key, value in mydict.items():
		print(key + ':' + str(value))

compute_frequency()
