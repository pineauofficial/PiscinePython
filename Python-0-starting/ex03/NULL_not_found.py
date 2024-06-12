def NULL_not_found(object: any) -> int:
	error = 0
	if (object == None):
		print("Nothing :",object, type(object))
	elif (type(object) == float):
		print("Cheese :",object, type(object))
	elif (object == 0 and type(object) == int):
		print("Zero :",object, type(object))
	elif (object == ""):
		print("Empty :",object, type(object))
	elif (object == False):
		print("Fake :",object, type(object))
	else:
		print("Type not found")
		error = 1
	return error