def menu_2():
	print("############")
	print("## Menu2 ###")
	x=int(input("Choose 1.If you want to convert again or any other to exit"))
	if x==1:
		menu_1()
	else:
		exit()
def c_to_k():
	x=int(input("Centigrade: "))
	print("The temprature in kelvin is ",x+273.15)
	menu_2()

def k_to_c():
	x=int(input("Kelvin: "))
	print("The temprature in centigrade is ",x-273.15)
	menu_2()

def menu_1():
	print("Menu 1")
	print("######")
	x=int(input("Choose 1.K to C or 2. C to K"))
	if x==1:
		k_to_c()
	elif x==2:
		c_to_k()
	else:
		print("You choose the wrong option.")
		print("Please try again")
		menu_1()

def main():
	print("#######################################")
	print("# Kelvin to centigrade and vice versa #")
	print("#######################################")
	menu_1()

main()
