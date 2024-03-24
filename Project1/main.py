import math
import bissection as bisect
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
iteractions = 20
bissectionGuess = bisect.bissection(butlerVolmer,-5,5,iteractions)
secantGuess, secantIter = sec.secant(butlerVolmer,-5,5)
newtonGuess, newtonIter = new.newton(butlerVolmer, -5)

print(f"Bissection Guess after {iteractions}: {bissectionGuess}")
print(f"Secant Guess after {secantIter}: {secantGuess}")
print(f"Newton Guess after {newtonIter}: {newtonGuess}")