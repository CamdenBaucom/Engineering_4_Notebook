# Calculator
# Written by Camden Baucom

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
operator = input("Operator(either -,+,*,/,%):\n") #Print Operator..., then skip a line and wait for user input
print(doMath(numberOne,numberTwo,operator)) # The three user inputs from above are plugged into the doMath function below, and the answer is printed out on one line

