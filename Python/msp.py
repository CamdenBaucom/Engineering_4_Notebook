# _
#< |__
# | _ |
# || ||

#O__
#|  |
#V  V

#O_
#| |

def pinata(numWrong,howHard):
	counter = -1
	shape1 = [' _\n','< ','|','_','_\n ','| ','_ ','|\n ','|','| ','|','|'] 
	shape2 = ['O','_','_\n','|  ','|\n','V  ','V']
	shape3 = ['O','_\n','| ','|']
	for x in range(numWrong):
		counter += 1
		if howHard == 1:
			newShape = shape1[counter]
		elif howHard == 2:
			newShape = shape2[counter]
		else:
			newShape = shape3[counter]
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
			del blankWordList[guessPos[i]]
			blankWordList.insert(guessPos[i],guess)
		#for i in range(len(guessPos)):
		#	blankWordList.insert(guessPos[i],guess)
		blankWord = ''.join(map(str, blankWordList))
		print(blankWord)
	else:
		print("Sorry wrong")
		print(blankWord)
		global numberWrong
		numberWrong += 1
		global difficulty
		pinata(numberWrong,difficulty)

global logOfGuesses
logOfGuesses = []
numberWrong = 0
difficulty = int(input("Player 2, choose difficulty(how many guesses you get)\nType 1 for easy(12 guesses), 2 for regular(7 guesses), or 3 for hard(4 guesses):\n"))
while difficulty != 1 and difficulty != 2 and difficulty != 3:
	difficulty = int(input("Please input either 1,2, or 3:\n"))
secretWord = input("Player 1, please enter a lowercase word you want Player 2 to guess:\n")
print("\n" * 50)
print(codedWord(secretWord))
word = secretWord
#print("\n" * 50)
endCrit = 0
if difficulty == 1:
	endCrit = 12
elif difficulty == 2:
	endCrit = 7
else:
	endCrit = 4
while numberWrong < endCrit and blankWord != secretWord:
	newGuess = input("Player 2, please guess a letter:\n")
	#guessLog(newGuess)
	if guessLog(newGuess) == False:
		print("You have already guessed that, please input a new guess")
	#	guessLog(newGuess)
	else:
	#	guessLog(newGuess)
		wordSearch(newGuess)
if numberWrong == endCrit:
	print("Sorry, you lost! The answer was " + secretWord)
if blankWord == secretWord:
	print("You won, great job!") 
