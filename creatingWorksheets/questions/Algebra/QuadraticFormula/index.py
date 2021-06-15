import random
from fractions import Fraction, gcd
from equations import formatMathString, randomBetweenNot

def getPrimes(lowerRange, upperRange):
  primes = []

  for num in range(lowerRange,upperRange + 1):  
    if num > 1:  
        for i in range(2,num):  
            if (num % i) == 0:  
                break  
        else:  
            primes.append(num)

  return primes  

class QuadraticFormula():
  def __init__(self):
    """
    x^2 + bx + c = 0
    x = -b +- sqrt(non breakable) / 2

    b^2 - 4ac = not divisible by ps
    """
    var = "x"

    choices = []
    for prime in getPrimes(1,145):
      for a in range(1,20):
        for b in range(-20,21):
          for c in range(-20,21):
            if b != 0 and c != 0 and b**2 - 4*a*c == prime:
              choices.append([a,b,c,prime])

    random.shuffle(choices)        
    a = choices[0][0]
    b = choices[0][1]
    c = choices[0][2]
    prime = choices[0][3]

    print(a,b,c)
    print(f"{-b}+-sqrt({prime})/{2*a}")

    self.worksheetQuestion = f"{a}x^2+{b}x+{c}"
    self.answer = fr"\frac{{{-b}\pm\sqrt{{{prime}}}}}{{{2*a}}}"
    self.worksheetQuestion = formatMathString(self.worksheetQuestion)
    self.answer = formatMathString(self.answer)

quadraticFormulaQuestionsDict = {"QuadraticFormula": QuadraticFormula}