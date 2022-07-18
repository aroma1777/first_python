print("Grade calculator")

grade=int(input("Grade: "))

if grade>=90:
	print("A+")
elif grade>=80 and grade<=89:
	print("A")
elif grade>=70 and grade<=79:
	print("B")
elif grade>=60 and grade<=69:
        print("C")
elif grade>=50 and grade<=59:
        print("D")
else:
        print("F")

