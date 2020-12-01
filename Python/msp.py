# _
#< |__
# | _ |
# || ||
def pinata(numWrong):
	counter = -1
	shape = [' _\n','< ','|','_','_\n ','| ','_ ','|\n ','|','| ','|','|'] 
	print("\n" * 50)
	for x in range(numWrong):
		counter += 1
		newShape = shape[counter]
		print(str(newShape) + "", end='')
	print("\n")

def wordSearch(guess):
	if guess in word:
		print("Got one!")
		if word.count(guess) > 1:
			#print("more than one")
			showWord = []
			showWords = word.replace(guess, '!')
			showWord.append(showWords) 
			print(showWord)
		#print(word.index(guess))
	else:
		print("Sorry wrong")


#pinata(int(10))
secretWord = input("Player 1, please enter the word you want Player 2 to guess:\n")
word = list(secretWord)
print("\n" * 50)
newGuess = input("Player 2, please guess a letter:\n")
wordSearch(newGuess)
