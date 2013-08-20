import random

LIVES = 8
usedLetters = []
turnsLeft = 0

def generateWord():
	words = ['hello', 'summer', 'colours', 'batman']
	return random.choice(words)

def checkLetter(word, letter):
	global turnsLeft
	global usedLetters

	if letter in usedLetters:
		print("You have already used that letter")
	else:
		if letter in word:
			usedLetters.append(letter)
			return "Good guess."
		else:
			turnsLeft = turnsLeft + 1
			return "Sorry. Try again."

def drawLetterOnScreen(word, letter):



def main():
	word = generateWord()

	for w in word:
		print ("_ ", end="")
	print("")
	print("No of lives: ", LIVES)

	turn = 0
	while(turnsLeft <= LIVES):
		
		letter = input("Please enter your guess: ")
		print(checkLetter(word, letter))
		print("No of turn left: ", (LIVES - turnsLeft))




if __name__ == "__main__":
	main()