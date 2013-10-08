import random

class Game:
	INCORRECT = 0
	CORRECT = 1
	LETTER_USED = 2
	WIN = 3

	def __init__(self, word):
		self.word = word
		self.turns = 8
		self.used_letters = []
		self.progress = ['_' for w in self.word]
		self.won = False

	def check_letter(self, letter):
		if letter in self.used_letters:
			return self.LETTER_USED
		else:
			if letter in self.word:
				# Replace letter
				for i, l in enumerate(self.word):
					if(l == letter):
						self.progress[i] = letter

				# Check for win
				if ''.join(self.progress) == self.word:
					self.win = True
					return self.WIN

				return self.CORRECT
			else:
				self.turns -= 1
				return self.INCORRECT

	def __str__(self):
		progress_string = 'Word: ' + ' '.join(self.progress) + '\n'
		turns_string = 'Number of turns left: ' + str(self.turns) + '\n'
		output_string = progress_string + turns_string
		return output_string

def generate_word():
	words = ['hello', 'summer', 'colours', 'batman']
	return random.choice(words)


def main():
	game = Game(generate_word())

	print game

	while game.turns > 0:
		letter = raw_input('Please enter your guess: ')
		result = game.check_letter(letter)

		if result is game.INCORRECT:
			print 'Sorry. Try again.'

		elif result is game.CORRECT:
			print 'Good guess.'

		elif result is game.WIN:
			print 'Congratulations. You win...at life!'

		elif result is game.LETTER_USED:
			print 'You have already used that letter.'
			print game.used_letters

		print game

	print "No more turns left. You have lost."

if __name__ == '__main__':
	main()