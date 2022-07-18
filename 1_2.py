#kelvin to centigrade and vice versa convertor

print("#########################################")
print("#########################################")
print("#### Kelvin to centigrade convertor #####")
print("########           Vice versa    ########")
print("#########################################")
print("#########################################")
print("#### What do you want to convert ########")
x=int(input("## Choose 1. K To C or 2. C To K  "))
if x==1:
	k=int(input("Please write the temprature in kelvin"))
	print("The temprature in centigrade is ",k-273.15)
elif x==2:
	c=int(input("Please write the temprature in centigrade"))
	print("The temprature in kelvin is ",c+273.15)
else:
	print("Incorrect  input! bye bye!")

