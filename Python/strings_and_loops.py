# Strings and Loops
# Camden Baucom

def takeapart(sen): #takeapart fucntion, with a variable called sen
	sen = sen.replace(" ", "- ") #replace all instances of spaces with a dash and then the space, so that later at the end of each word will be a minus sign
	words = sen.split() #split the words wherever there is a space, and create an array with the list called word
	for word in words: #for the items, each indidual word, in the array words
		for letter in word: #for the items, each individual letter, in the array word
			print(letter) #print the letters
fullSentence = input("Enter a sentence and its letters will be printed:\n") #the user is prompted to put in an input after seeing the "Enter a sentence..."
takeapart(fullSentence) #the user's input is put into the takeapart function
print("-") #print the final minus sign
