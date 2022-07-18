import random


def dice_thrower():
	return random.randint(1,6)

def game_check(game_money,player_money):
	if player_money*2>game_money or player_money==0:
		print("Game over!")
		exit()
	return 1

def pick_num(game_money,player_money,playing_amount):
	print("The rule of this game is")
	print("You will win if you guss the number correctly")
	print("If you win, your money will be doubled")
	print("Otherwise you will lose your playing amount")
	x=int(input("Pick number 1 to 6"))
	if x>6 or x<1:
		print("#####################################")
		print("You have entered invalid number")
		print("Try again!")
		print("####################################")
		pick_num(game_money,player_money,playing_amount)
	lucky_number=dice_thrower()
	print("The number lucky number is",lucky_number)
	if x==lucky_number:
		print("You have gussed correctly")
		player_money=player_money+playing_amount*2
		game_money=game_money-playing_amount
		print("You have won ",playing_amount*2)
		print("Your current deposit ", player_money)
	else:
		print("You didn't guess correctly")
		game_money+=playing_amount
	menu_4(game_money,player_money)

def menu_4(game_money,player_money):
	print("########################")
	print("Do you want to play again?")
	print("1. To play again")
	print("Any other to exit")
	x=int(input("Choice: "))
	if x==1:
		menu_2(game_money,player_money)
	print("Thanks for playing")
	print("Game money",game_money)

def even_odd(game_money,player_money,playing_amount):
	print("The rule of this game is")
	print("You will win this game if you gussed the parity of the number correctly")
	print("If you win your money will be multiplid by 1.1")
	print("Otherwise tou will lose your playing amount")
	print("Choose 1. Even 2. Odd")
	x=int(input("Choise"))
	if x==1 or x==2:
		lucky_number=dice_thrower()
		print("The number lucky number is",lucky_number)
		if lucky_number%2==0 and x==1:
			print("You have gussed correctly")
			game_money-=playing_amount*0.1
			player_money+=playing_amount*1.1
		elif lucky_number%2!=0 and x==2:
			print("You have gussed correctly")
			game_money-=playing_amount*0.1
			player_money+=playing_amount*1.1
		else:
			print("You didn't guess correctly")
			game_money+=playing_amount
	else:
		print("#####################################")
		print("You have entered invalid number")
		print("Try again!")
		print("####################################")
		even_odd(game_money,player_money,playing_amount)
	menu_4(game_money,player_money)

def half_half(game_money,player_money,playing_amount):
	print("The rule of this game is")
	print("You will win this game if you gussed the part of the half correctly")
	print("If you win your money will be multiplid by 1.1")
	print("Otherwise tou will lose your playing amount")
	print("Choose 1. 1-3 2. 4-6")
	x=int(input("Choise"))
	if x==1 or x==2:
		lucky_number=dice_thrower()
		print("The number lucky number is",lucky_number)
		if lucky_number<4  and x==1:
			print("You have gussed correctly")
			game_money-=playing_amount*0.1
			player_money+=playing_amount*1.1
		elif lucky_number>=4 and x==2:
			print("You have gussed correctly")
			game_money-=playing_amount*0.1
			player_money+=playing_amount*1.1
		else:
			print("You didn't guess correctly")
			game_money+=playing_amount
	else:
		print("#####################################")
		print("You have entered invalid number")
		print("Try again!")
		print("####################################")
		half_half(game_money,player_money,playing_amount)
	menu_4(game_money,player_money)
	

def menu_2(game_money,player_money):
	game_check(game_money,player_money)
	print("###############################")
	print("You have ",player_money,"$")
	print("The game have ",game_money,"$")
	print("###############################")
	print("Choose the amount you want to play with")
	y=int(input("Money: "))
	if y>player_money:
		print("You cannot play with amount greater than you have in your account")
		print("Choose")
		print("1.Exit")
		print("Any other to try again")
		a=input("Choice: ")
		if a=="1":
			print("Thanks for playing, Game over!")
			exit()
		else:
			menu_2(game_money,player_money)
	player_money-=y
	menu_3(game_money,player_money,y)

def menu_3(game_money,player_money,playing_amount):
	print("######################")
	print("Choose a game ")
	print("1. pick num ")
	print("2. even/odd ")
	print("3. half/half ")
	x=int(input("Choice: "))
	if x==1:
		pick_num(game_money,player_money,playing_amount)
	elif x==2:
		even_odd(game_money,player_money,playing_amount)
	elif x==3:
		half_half(game_money,player_money,playing_amount)
	else:
		print("###################################")
		print("#Incorrect Input please try again!#")
		print("###################################")
	menu_3(game_money,player_money,playing_amount)

def menu_1(game_money,player_money):
	print("######################")
	print("## Init step        ##")
	print("#####################")
	print("The max deposit allowed is 1000")
	x=int(input("What is the amount of money you want to deposit"))
	if x>1000:
		print("#############################")
		print("#Incorrect amount, try again#")
		print("############################")
		menu_1(game_money,player_money)
	player_money=x
	menu_2(game_money,player_money)

def main():
	print("#####################")
	print("#### Dice game  #####")
	print("## by Aroma     #####")
	print("#####################")
	game_money=10000
	player_money=0
	menu_1(game_money,player_money)

main()
