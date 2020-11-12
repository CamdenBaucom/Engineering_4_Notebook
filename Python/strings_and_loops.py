# Strings and Loops
# Camden Baucom

def takeapart(sen):
	words = sen.split()
	sentence = [words]
	for word in sentence:
		let = [word]
		return [letter for letter in let]
		#for letter in word:
			#return letter
			#if letter == " ":
				#letter = "-"
			#else:
				#return letter
fullSentence = input("Enter a sentence and its letters' will be printed:\n")
print(takeapart(fullSentence))
