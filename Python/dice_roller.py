# Automatic Dice Roller
# Written by Camden Baucom

from random import randint #imports the random function

print ("Automatic Dice Roller")


activeProgram = True #boolean used to loop or exit the program

while activeProgram == True: #loops the program
	roll = input("Press enter to get a random number from 1 to 6\nPress x and then enter to escape the program:\n") #logs the input of the user, and determines the type of variable, before assigning the value of the input to roll	
	if roll == "": #if the user just presses enter
		rollValue = randint(1,6) #A random number from 1 to 6 is generated
		print(rollValue) #That number is printed
	elif roll == "x": #if the user presses x and then presses enter
		activeProgram = False #kicks the user out of the while loop 
	else: #if something other than enter, or x and then enter, was pressed
		print("Please reenter value") #tell the user to reenter their input
else: #if the activeProgram boolean is False, which can only be done through the elif roll == "x"
	print("leaving program") #tell the user they are leaving the program
	exit() #leave the program"
