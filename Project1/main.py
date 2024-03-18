import math
import bisection as bisect
#Constants
Alpha = 0.2
Beta = 2
Euler = math.e

# Given: f(x) =>  Butler-Volmer Equation
def butlerVolmer(x):
    return Euler**(Alpha*x)-Euler**((Alpha-1)*x)-Beta

# Goal: Find f(x) = 0
iteractions = 20
error = 1.0e-1
bisectionGuess = bisect.bisectionIteration(butlerVolmer,-5,5,iteractions)
print(f"Bisection Guess after {iteractions}: {bisectionGuess}")
bisectionErrorGuess = bisect.bisectionError(butlerVolmer, -5, 5, error)
print(f"Bisection Guess with {error} error: {bisectionErrorGuess}")
