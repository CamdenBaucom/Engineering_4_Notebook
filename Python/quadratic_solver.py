# Quadratic Solver
# Camden Baucom

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
coeff1 = int(input("Quadratic Solver\n Enter the coefficients for ax^2 + bx +c = 0\n Enter the first coefficient:\n")) 
coeff2 = int(input("Enter the second coefficient:\n"))
coeff3 = int(input("Enter the third coefficient:\n"))
print(quadSolver(coeff1,coeff2,coeff3))

