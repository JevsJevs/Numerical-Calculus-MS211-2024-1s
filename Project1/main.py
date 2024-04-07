import math
import bisection as bisect
import secant as sec
import newton as new

#Constants
Alpha = 0.2
Beta = 2
Euler = math.e

# Given: f(x) =>  Butler-Volmer Equation
def butlerVolmer(x):
    return Euler**(Alpha*x)-Euler**((Alpha-1)*x)-Beta

# Goal: Find f(x) = 0
iterations = 17
error = 1.0e-1
bissectionGuess = bisect.bisectionIteration(butlerVolmer,-5,5,iterations)
bisectionErrorGuess = bisect.bisectionError(butlerVolmer, -5, 5, error)
secantGuess, secantIter = sec.secant(butlerVolmer,-5,5)
newtonGuess, newtonIter = new.newton(butlerVolmer, -5)

print(f"Bissection Guess after {iterations}: {bissectionGuess}")
print(f"Bisection Guess with {error} error: {bisectionErrorGuess}")
print(f"Secant Guess after {secantIter}: {secantGuess}")
print(f"Newton Guess after {newtonIter}: {newtonGuess}")