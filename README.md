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
def doMath(numOne,numTwo,operation): #the doMath function, with the input points named numOne,numTwo, and operation respectively
	if operation == "-": #if the string input is "-" then
		return numOne - numTwo #subtract numTwo from numOne and return the answer
	elif operation == "+": #if the string input is "+" then
		return numOne + numTwo #add numTwo to numOne and return the answer
	elif operation == "*": #if the string input is "*" then
		return numOne * numTwo #multiply numOne by numTwo and return the answer
	elif operation == "/": #if the string input is "/" then
		divNum = numOne / numTwo #divide numOne by numTwo and save the answer as divNum
		roundedNum = round(divNum, 2) #round that answer to two decimal places
		return roundedNum #return the rounded answer
	elif operation == "%": #if the string input is "%" then
		return numOne % numTwo #divide numOne by numTwo, determine the remainder, and save the answer 
	else:
		return "invalid operator syntax" #if the input for operation does not match one of these above, then it was imputed incorrectly
numberOne = int(input("First number:\n")) #Print First number:, then skip a line and wait for user input, which is converted into an integer
numberTwo = int(input("Second number:\n")) #Print Second number:, then skip a line and wait for user input, which is converted into an integer
```
With all that, the user is prompted with the input(), where the quotations in the brackets appear as text for the user to see. The function runs and the results are then printed and the program ends.

## Python Program 02 – Quadratic Solver
A basic quadratic solver with three coefficient inputs, which first determines if there are real roots, by taking the discriminant, and if it does exist, puts the roots into an array and returns the roots. The bulk of the code is the quadSolver function, which first determines the discriminant, b^2 -4ac, and since the square root of the discriminant is then determined, the only way to get a real root(i is non-real) is for the discriminant to be greater than or equal to 0. For non real roots, it returns "No real roots," but for real roots it first creates an empty array called roots, and adds the two roots to them, which is then returned and printed. I also had to import math, as Python doesn't have a built in square root function.
```ruby
import math
def quadSolver(co1,co2,co3):
	discrim = (co2 ** 2)-(4 * co1 * co3)
	if discrim < 0:
		return "No real roots"
	else:
		roots = []
		roots.append(((-1 * co2) - (math.sqrt(discrim))) / (co1 * 2))
		roots.append(((-1 * co2) + (math.sqrt(discrim))) / (co1 * 2))
		return roots
```
