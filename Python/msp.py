# Hangman Pinata
# Written by Camden Baucom
# Easy hangman:
# _
#< |__
# | _ |
# || ||
# Regular hangman:
#O__
#|  |
#V  V
# Easy hangman:
#O_
#| |

def pinata(numWrong,howHard): #pinata function creates the hangman shape with two inpts, the number of wrong guess, and the difficulty level
	counter = -1 #counter starts at -1, because first counter should be 0, as lists start at 0
	shape1 = [' _\n','< ','|','_','_\n ','| ','_ ','|\n ','|','| ','|','|'] #easy hangman shape has 12 parts, each part includes the necessary spaces and newlines
	shape2 = ['O','_','_\n','|  ','|\n','V  ','V'] #regular hangman shape has 7 parts
	shape3 = ['O','_\n','| ','|'] #hard hangman shape has 4 parts
	for x in range(numWrong): #do this how ever many times there have been wrong guesses
		counter += 1 #counts from 0 up
		if howHard == 1: #if difficulty is easy
			newShape = shape1[counter] #create a new list with component number counter from the shape list above, as counter increases so does the part number from the shape list
		elif howHard == 2: #if difficulty is regular
			newShape = shape2[counter] #same as above with shape2
		else: #if difficulty is hard 
			newShape = shape3[counter] #same as above with shape 3
		print(str(newShape) + "", end='') #convert newShape from a list to a string and print
	print("\n") #skip a line

def codedWord(inputWord): #codedWord function takes the input Word and turns it into the appropriate number of dashes
	x = len(inputWord) #x is equal to the length of input word
	secretWord = [] #new list called SecretWord
	for i in range(x): #do this the number of times equal to the length of the input word
		secretWord.append("-") #add dashes to SecretWord
	global blankWord #create a global variable, a variable that can be accessed anywhere in the program
	blankWord = ''.join(map(str, secretWord)) #Turn SecretWord into a string called blankWord
	return blankWord #return blankWord

def guessLog(newestGuess): #guessLog function logs new guesses and stops repeat guesses
	global logOfGuesses #acceses gloabl variable logOfGuesses which is just an empty array initially
	guessTest = ''.join(map(str, logOfGuesses)) #turn logOfGuesses into a string
	if newestGuess in guessTest: #if the newest guess is already inside of the string of guesses
		print("You have guessed:", logOfGuesses) #tell the user the unique guesses they have already made
		return False #return False
	else: #if the newest guess is not already inside of the string of guesses
		logOfGuesses.append(newestGuess) #add the newest guess to the list of guesses
		logOfGuesses.sort() #sort them alphabetically
		print("You have guessed:", logOfGuesses) #tell the user the unique guesses they have already made
		return True #return True

def wordSearch(guess): #wordSearch function checks to see if the user's guess is correct
	global blankWord #access the global variable blankWord
	blankWordList=[] #make a new empty list called blankWordList
	blankWordList[:0]=blankWord #add blankWord to blankWordList, turning it into a list
	guessPos = [] #make a new empty list callde guessPos
	if guess in word: #if the user's guess is in the word
		print("Got one!") #print Got one!
		for i in range(len(word)): #loop through this function the number of times equal to the length of the word
			if word[i] == guess: #as i counts up from 0 to the length of the word, check each letter of the word, by looking at index i, to see if it matches the guess
				guessPos.append(i) #if the guess matches a letter at index i, add the number of i to guessPos
		for i in range(len(guessPos)): #loop through this function how ever many times the guess was inside the wod
			del blankWordList[guessPos[i]] #delete a dash from blankWordList at the index that the correct guess appeared
			blankWordList.insert(guessPos[i],guess) #add the correct guess to blankWordList at the index that the correct guess appeared
		blankWord = ''.join(map(str, blankWordList)) #blankWord is equal to the string of blankWordList
		print(blankWord) #print blankWord, which is the dashes with updated correct guesses
	else: #if the user's guess is not in the word
		print("Sorry wrong") #print Sorry wrong
		print(blankWord) #print blankWord
		global numberWrong #access global variable numberWrong
		numberWrong += 1 #add one to numberWrong
		global difficulty #access global variable difficulty
		pinata(numberWrong,difficulty) #run pinata function, with input of the number of wrong guesses and the difficulty

global logOfGuesses #create a global variable called logOfGuesses
logOfGuesses = [] #make logOfGuesses an empty list
numberWrong = 0 #create a variable called numberWrong equal to 0
difficulty = int(input("Player 2, choose difficulty(how many guesses you get)\nType 1 for easy(12 guesses), 2 for regular(7 guesses), or 3 for hard(4 guesses):\n"))
#difficulty is equal to the input of the user when prompted with the above question
while difficulty != 1 and difficulty != 2 and difficulty != 3: #while the user did not respond to the above question with 1,2,or 3 loop through this
	difficulty = int(input("Please input either 1,2, or 3:\n")) #difficulty is equal to the input of this question
secretWord = input("Player 1, please enter a lowercase word you want Player 2 to guess:\n") #secretWord is equal to the word Player 2 is trying to guess
print("\n" * 50) #clear the screen
print(codedWord(secretWord)) #print and run codedWord with input secretWord
word = secretWord #word is equal to secretWord
endCrit = 0 #create variable called endCrit with value 0
if difficulty == 1: #if easy difficulty is chosen
	endCrit = 12 #endCrit is equal to 12, which is the number of wrong guess before the game end
elif difficulty == 2: #if regular difficulty is chosen
	endCrit = 7 #endCrit is equal to 7
else: #if hard difficulty is chosen
	endCrit = 4 #endCrit is equal to 4
while numberWrong < endCrit and blankWord != secretWord: #while the number of wrong guess does not equal the end criteria (above) and the blankWord (dashes replaced with guesses) does not equal secretWord
	newGuess = input("Player 2, please guess a letter:\n") #player 2 is prompted to enter a guess
	if guessLog(newGuess) == False: #guessLog is run with the guess and if it returns false, meaning this is a repeat guess
		print("You have already guessed that, please input a new guess") #tell the user it is a repeat guess and ask them to enter another
	else: #if guessLog does not return false, meaning this is a unique guess
		wordSearch(newGuess) #run wordSearch function with the guess
if numberWrong == endCrit: #if the number of wrong guesses is equal to the end criteria
	print("Sorry, you lost! The answer was " + secretWord) #tell the user they lost and tell them the word that they were guessing
if blankWord == secretWord: #if blankWord, the word that starts with dashes and is replaced with correct guesses, is equal to secretWord, the starting word
	print("You won, great job!") #tell the user that they won
