# Strings and Loops
# Camden Baucom

def takeapart(sen):
	sen = sen.replace(" ", "- ")
	words = sen.split()
	for word in words:
		for letter in word:
			print(letter)
fullSentence = input("Enter a sentence and its letters' will be printed:\n")
takeapart(fullSentence)
print("-")
