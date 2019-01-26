# 6.
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program: hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

def calculate():
	sentence = input()
	letter_count = 0
	digit_count = 0
	for x in sentence:
		if x.isalpha():
			letter_count += 1
		elif x.isdigit():
			digit_count += 1
	print('LETTERS ' + str(letter_count))
	print('DIGITS ' + str(digit_count))

calculate()