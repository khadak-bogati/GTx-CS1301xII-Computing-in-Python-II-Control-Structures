import random
#Get a random number from 1 to 100
GuessNumber = random.randint(1,100)
#Create userGuess and give a value tht can't be correct
myGuess = 0
#Repeat until guess is correct
while not myGuess == GuessNumber:
	myGuess = int(input("Guess a Number: "))
#Check if the guess number is too high
	if myGuess > GuessNumber:
		print("It is too High")
#Check if the guess is too low
	elif myGuess < GuessNumber:
		print("It is too low")
#Guess must be right
	else:
		print("That's Right")
