import building

"""doc du module"""
import sys
sys.dont_write_bytecode = True
def main():
	"""doc de la fonction"""
	print("Hello World")
if __name__ == "__main__":
	main()
	print(main.__doc__)
	print(__doc__)
else:
	print("Hello Pas World")