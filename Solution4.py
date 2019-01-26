# 4.Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
# Hints:
# Use __init__ method to construct some parameters

class myclass:
	def __init__(self, string = ''):
		self.string = string
	def getString(self):
		self.string= input()
	def printString(self):
		print(self.string.upper())

# test
mystring = myclass()
mystring.getString()
mystring.printString()

