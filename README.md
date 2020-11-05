# Engineering_4_Notebook
My Engineering 4 Notebook

## Hello Python
A short program to generate a random number from 1-6 based on user input. This assignment helped refresh me on some Python syntax that I had used in the past but had kind of forgotten. It was also the first time I had used the input() function, which takes user input and determines what return type it is( in contrast to raw_input() which always returns a string,) then whatever the user inputed can then be assigned to a variable and used like any other value.

```ruby
# Automatic Dice Roller
# Written by Camden Baucom

from random import randint #imports the random function

print ("Automatic Dice Roller")


activeProgram = True #boolean used to loop or exit the program

while activeProgram == True: #loops the program
	roll = input("Press enter to get a random number from 1 to 6\nPress x and then enter to escape the program:\n") 
         #logs the input of the user, and determines the type of variable, before assigning the value of the input to roll	
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
```

## Python Program 01 – Calculator
A calculator with 5 different operators and two different numbers, all based off user input. The input mechanism was similar to the one on Hello Python above, but since the inputs were two integers and then an operator, I first treated them all like strings. Then with the operators, I matched the string of the operator with the actual operation. Finally with the integers, I just put them into an int() before sticking them into the function.
```ruby
def doMath(numOne,numTwo,operation):
	if operation == "-":
		return numOne - numTwo
	elif operation == "+":
		return numOne + numTwo
	elif operation == "*":
		return numOne * numTwo
	elif operation == "/":
		divNum = numOne / numTwo
		roundedNum = round(divNum, 2)
		return roundedNum
	elif operation == "%":
		return numOne % numTwo
	else:
		return "invalid operator syntax"
numberOne = int(input("First number:\n"))
numberTwo = int(input("Second number:\n"))
```
With all that, the user is prompted with the input(), where the quotations in the brackets appear as text for the user to see. The function runs and the results are then printed and the program ends.
