import math
import error as errorClass
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

# Prompts for custom code execution
iterations = int(input("Maximo de iteracoes: "))

errSelect = None
while errSelect == None:
    try:
        errSelect = input("Qual tipo de erro quer usar? r - relativo | a - absoluto:")
        errSelect.lower()
        if errSelect != 'r' and errSelect != 'a':
            raise ValueError
    except:
        errSelect = None

errorValue = None
while errorValue == None:
    try:
        errorValue = float(input("Valor do erro[separador .]:"))
    except:
        errorValue = None

errObj = errorClass.absoluteError(errorValue) if errSelect == "a" else errorClass.relativeError(errorValue)
errorType = "absolute error" if errSelect == "a" else "relative error"

# Goal: Find f(x) = 0
secantGuess, secantIter = sec.secant(butlerVolmer,-5,5)
newtonGuess, newtonIter = new.newton(butlerVolmer, -5)
bisectGuess = bisect.bisection(butlerVolmer, -5, 5, iterations, errObj)

print("===============================================Results==========================================================\n")
print(f"Bisection Guess using {errorType} with {errObj.error} precision [Max iterations {iterations}]: {bisectGuess}")
print(f"Secant Guess after {secantIter}: {secantGuess}")
print(f"Newton Guess after {newtonIter}: {newtonGuess}")