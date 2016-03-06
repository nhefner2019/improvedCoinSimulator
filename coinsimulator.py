import random
coin = random.randint(0,1)

name = raw_input("What is your name?")

print("Hello {}.".format(name))

if coin == 0:
	print("The coin is tails.")
if coin == 1:
	print("The coin is heads.")