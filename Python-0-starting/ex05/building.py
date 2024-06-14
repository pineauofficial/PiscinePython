"""
displays the sums of its upper-case characters, lower-case
characters, punctuation characters, digits and spaces of a string.
"""

import sys
sys.dont_write_bytecode = True

def main():
	"""main function"""
	if (len(sys.argv) != 2):
		print("AssertionError: more than one argument is provided")
		exit()

	upper, lower, punct, digit, space, total = 0, 0, 0, 0, 0, 0
	for char in sys.argv[1]:
		if char.isupper():
			upper += 1
		elif char.islower():
			lower += 1
		elif char.isdigit():
			digit += 1
		elif char.isspace():
			space += 1
		else:
			punct += 1
		total += 1
		
	print("total: ", total)
	print("upper: ", upper)
	print("lower: ", lower)
	print("punct: ", punct)
	print("space: ", space)
	print("digit: ", digit)

if __name__ == "__main__":
	main()