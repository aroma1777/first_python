##Kelvin to centigrade mofiied

def k_to_c(kelvin):
	return kelvin-273.15

print(k_to_c(1))

#print None
def function_with_no_return():
	x=2

print(function_with_no_return())

def function_with_no_return_2(x):
	print(x)

function_with_no_return_2(10)
print(function_with_no_return_2(3))

def f3(x):
	print(x)
	return 2

print(f3(9))

def k_to_c(kelvin):
	print(2)

#CHooses the nearest function
print(k_to_c(3))

#implementing the above function in different way
def k_to_c_2(kelvin):
	#variable inside function is called local variable
	centigrade=kelvin-273.15
	return centigrade

#varaible outside function is called global variable
centigrade=3
print(centigrade)
