import random

LIVES = 8
turnsLeft = 0
usedLetters = []
wordList = []

def generateWord():
	words = ['hello', 'summer', 'colours', 'batman']
	return random.choice(words)

def checkLetter(word, letter):
	global turnsLeft
	global usedLetters

	if letter in usedLetters:
		print("You have already used that letter.")
		print(usedLetters)
	else:
		if letter in word:
			printWord(word, wordList, letter)
			return "Good guess."
		else:
			turnsLeft = turnsLeft + 1
			return "Sorry. Try again."

def printWord(word, wordList, letter):
	for i, l in enumerate(word):
		if(l == letter):
			wordList[i] = letter

	for w in wordList:
		print(w, " ", end="")


def main():
	word = generateWord()

	for w in word:
		wordList.append("_")
		print("_ ", end="")
	print("")
	print("No of lives: ", LIVES)

	turn = 0
	while(turnsLeft <= LIVES):
		letter = input("Please enter your guess: ")
		print(checkLetter(word, letter))
		print("No of turn left: ", (LIVES - turnsLeft))
		print("")


if __name__ == "__main__":
	main()