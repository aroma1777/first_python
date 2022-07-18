age=int(input("write your age: "))
if age<4:
	print("you must be a child")
elif age>=4 and age<=6:
	print("you must be K.G. student")
elif age>=7 and age<=14:
	print("you must be elementary student")
elif age>=15 and age<=18:
	print("you must be highschool student")
else:
	print("You have finished high school")
