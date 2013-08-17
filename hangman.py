# Pseudocode
# Generate random word
# Output number of turns

import random

usedLetters = []

def generateWord():
	words = ['hello', 'summer', 'colours', 'batman']
	return random.choice(words)

def checkLetter(word, letter):
	global usedLetters
	if letter in word:
		usedLetters.append(letter)
		return "Good guess."
	else:
		return "Sorry. Try again."


def main():
	word = generateWord()

	for w in word:
		print ("_ ", end="")
	print("")

	while(True):
		
		letter = input("Please enter your guess: ")
		returnVal = checkLetter(word, letter)
		print(returnVal)
		print (usedLetters)


if __name__ == "__main__":
	main()