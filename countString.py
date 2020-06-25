listOfString = ["This is the first string", "This is the first string",
				"This is the first string", "This is the first string",
				"This is the first string", "This is the first string"]
numSpaces = 0
for currentString in listOfString:
	for currentCharacter in currentString:
		if currentCharacter == " ":
			numSpaces += 1
numWords = numSpaces + len(listOfString)
print("There are", numWords, "words in these string")
