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
howWrong = int(input("How many wrong"))
print("\n" * 50)
pinata(howWrong)
print("\n" * 30)
