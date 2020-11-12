# Quadratic Solver
# Camden Baucom

import math #imports a math module with a square root function, which Python does not have
def quadSolver(co1,co2,co3): #quadSolver function, with 3 inputs
	discrim = (co2 ** 2)-(4 * co1 * co3) #find the discriminant, b^2 - 4ac 
	if discrim < 0: #if the discriminant is less than 0, you are finding the square root of a negative number which is non-real
		return "No real roots" #tell the user that there are no real roots
	else: #if the discriminant is greater than or equal to 0
		roots = [] #create an empty array called roots
		roots.append(((-1 * co2) - (math.sqrt(discrim))) / (co1 * 2)) #plug the coefficients into the quadratic formula, and add the root to the array
		roots.append(((-1 * co2) + (math.sqrt(discrim))) / (co1 * 2)) #plug the coefficients into the quadratic formula, and add the root to the array
		return roots #return the array
coeff1 = int(input("Quadratic Solver\n Enter the coefficients for ax^2 + bx +c = 0\n Enter the first coefficient:\n")) #ask user for coefficient 1 
coeff2 = int(input("Enter the second coefficient:\n")) #ask user for coefficient 2
coeff3 = int(input("Enter the third coefficient:\n")) #ask user for coefficient three
print(quadSolver(coeff1,coeff2,coeff3)) #plug the inputs into the function and print the results

