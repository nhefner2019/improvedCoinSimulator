import random
coin = random.randint(0,1)

name = raw_input("What is your name? ")

guess = raw_input("Hello {}. What do you think the coin will be? ".format(name))

if coin == 0 and guess == "Tails":
	print("Great job guessing, {}. The coin is tails.".format(name))
	
elif coin == 0 and guess != "Tails":
	print("Sorry, {}. You guessed wrong. The coin is tails.".format(name))
	
elif coin == 1 and guess == "Heads":
	print("Great job guessing, {}. The coin is heads.".format(name))
	
elif coin == 1 and guess != "Heads":
	print("Sorry, {}. You guessed wrong. The coin is heads.".format(name))