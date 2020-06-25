import random
numGame = int(input("How many games would you like to play? "))
#Repates this the number of games the user chose
for i in range(0, numGame):
	print("Game Start!")
	hiddenNumber = random.randint(1,100)
	#Create userGuess and give is a value that can't be correct
	userGuess =0
	#Repate until the guess is correct
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
