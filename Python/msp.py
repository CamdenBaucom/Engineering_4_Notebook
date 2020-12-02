# _
#< |__
# | _ |
# || ||
def pinata(numWrong):
	counter = -1
	shape = [' _\n','< ','|','_','_\n ','| ','_ ','|\n ','|','| ','|','|'] 
	for x in range(numWrong):
		counter += 1
		newShape = shape[counter]
		print(str(newShape) + "", end='')
	print("\n")

def codedWord(inputWord):
	x = len(inputWord)
	secretWord = []
	for i in range(x):
		secretWord.append("-")
	global blankWord
	blankWord = ''.join(map(str, secretWord))
	return blankWord

def guessLog(newestGuess):
	global logOfGuesses 
	#logOfGuesses.sort()
	#print("You have guessed:", logOfGuesses)
	guessTest = ''.join(map(str, logOfGuesses))
	if newestGuess in guessTest:
		print("You have guessed:", logOfGuesses)
		#print("You have already guessed that, please input a new guess")
		return False
	else:
		logOfGuesses.append(newestGuess)
		logOfGuesses.sort()
		print("You have guessed:", logOfGuesses)
		return True

def wordSearch(guess):
	global blankWord
	blankWordList=[]
	blankWordList[:0]=blankWord
	guessPos = []
	if guess in word:
		print("Got one!")
		for i in range(len(word)):
			if word[i] == guess:
				guessPos.append(i)
		for i in range(len(guessPos)):
			blankWordList.remove("-")
		for i in range(len(guessPos)):
			blankWordList.insert(guessPos[i],guess)
		blankWord = ''.join(map(str, blankWordList))
		print(blankWord)
	else:
		print("Sorry wrong")
		print(blankWord)
		global numberWrong
		numberWrong += 1
		pinata(numberWrong)

global logOfGuesses
logOfGuesses = []
numberWrong = 0
secretWord = input("Player 1, please enter a lowercase word you want Player 2 to guess:\n")
print("\n" * 50)
print(codedWord(secretWord))
word = secretWord
#print("\n" * 50)
while numberWrong < 12 and blankWord != secretWord:
	newGuess = input("Player 2, please guess a letter:\n")
	#guessLog(newGuess)
	if guessLog(newGuess) == False:
		print("You have already guessed that, please input a new guess")
	#	guessLog(newGuess)
	else:
	#	guessLog(newGuess)
		wordSearch(newGuess)
if numberWrong == 12:
	print("Sorry, you lost! The answer was " + secretWord)
if blankWord == secretWord:
	print("You won, great job!") 
