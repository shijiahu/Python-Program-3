# 10.
# Write a program to solve a classic ancient puzzle:
# We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
# How many rabbits and how many chickens do we have?
# Hint:
# Use for loop to iterate all possible solutions.

# chickens 2 legs
# rabbits 4 legs

for chicken in range(36):
	rabbit = 35 - chicken
	if chicken * 2 + rabbit * 4 == 94:
		print("We have " + str(chicken) + ' chickens and ' + str(rabbit) + ' rabbits')

