# Calculator
# Written by Camden Baucom

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
operator = input("Operator(either -,+,*,/,%):\n")
print(doMath(numberOne,numberTwo,operator))

