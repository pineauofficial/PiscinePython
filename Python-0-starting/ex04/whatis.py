import sys
sys.dont_write_bytecode = True

if (len(sys.argv) != 2):
	print("AssertionError: more than one argument is provided")
	exit()

if (isinstance(sys.argv[1], str)):
    try:
        float(sys.argv[1])
    except ValueError:
        print("AssertionError: argument is not an integer")
        exit()
        
number = float(sys.argv[1])
if (number % 1 != 0):
    print("AssertionError: argument is not an integer")
    exit()
if (number % 2 == 0):
    print ("I'm Even")
else:
    print ("I'm Odd")

















def est_nombre(variable):
    if isinstance(variable, (int, float)):
        return True
    if isinstance(variable, str):
        try:
            float(variable)
            return True
        except ValueError:
            return False
    return False


