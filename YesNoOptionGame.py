import random
keepPlaying = "y"
while keepPlaying == "y":
	print("Game start ")
	hiddenNumber = random.randint(1,100)
	userGuess = 0
	while not userGuess == hiddenNumber:
		#Get the user's next guess as an integer
		userGuess = int(input("Guess a Number: "))
		#Check if the guess is too high
		if userGuess > hiddenNumber:
			print("Too High")
		elif userGuess < hiddenNumber:
			print("Too Low")
		else:
			print("That is right!")
	keepPlaying=input("Play again(y for yes, n for no)?")
