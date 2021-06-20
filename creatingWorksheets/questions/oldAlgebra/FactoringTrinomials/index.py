"""

random letter (fgh)
f - linear ax+b
g - quadratic ax^2 + bx + c
h - cubic ax^3 + bx^2 + bx + c

"""
import random
from fractions import Fraction, gcd
from equations import formatMathString, randomBetweenNot

class FactorTrinomials():
  def __init__(self, aEqualsOne=True, bValuePositive=True, cValuePositive=True):
    self.kwargs = {"aEqualsOne":True, "bValuePositive":True, "cValuePositive":True}

    minn = -10
    maxx = 10
    maxxProduct = 100

    if aEqualsOne:
      a = 1
      bNotList = [0]
    else:
      a = random.choice([2,3,5])
      aMults = [i for i in range(a, maxx+1, a)]
      print(aMults)
      aNegMults = [-1*i for i in aMults]
      aMults = aMults + aNegMults
      bNotList = aMults + [0]

    #We want abs(b1*b2) <= 100 ie maxxProduct, so that our "c" is less than or equal to maxxProduct
    if bValuePositive:
      # + + - all positive
      if cValuePositive:
        b1 = randomBetweenNot(1, maxx*2, bNotList)
        b2 = random.choice([b2 for b2 in range(1,maxxProduct+1) if abs(b1*b2) <= maxxProduct]) 
      # + - means bigger number is positive ie b1*a > b2
      else:
        b1 = random.choice([b1 for b1 in range(2, maxx*2+1) if b1 not in bNotList])
        print(b1, bNotList)
        #b1*a needs to be bigger
        b2 = random.choice([b2 for b2 in range(-maxxProduct,0) if b2 not in bNotList and b1*a > b2 and abs(b1*a*b2) <= 100])
    else:
      if cValuePositive:
        b1 = randomBetweenNot(-maxx*2, -1, bNotList)
        print(b1, bNotList)
        b2 = random.choice([b2 for b2 in range(-maxxProduct,0) if abs(b1*a*b2) <= 100])
      else:
        #b1*a should be less than b2, so that the sum is negative
        b1 = random.choice([b1 for b1 in range(-maxx*2,-1) if b1 not in bNotList])
        b2 = random.choice([b2 for b2 in range(1,maxxProduct+1) if b1*a < b2 and abs(b1*a*b2) <= 100])
    
    b = a*b1 + b2
    c = b1 * b2

    self.worksheetQuestion = f"{a}x^2+{b}x+{c}"
    self.worksheetQuestion = formatMathString(self.worksheetQuestion)
    self.answer = f"({a}x+{b2})(x+{b1})"
    self.answer = formatMathString(self.answer)

class FactorDOTS():
  def __init__(self, aEqualsOne=True):
    self.kwargs = {"aEqualsOne":True}
    
    if aEqualsOne:
      a = 1
      aSquared = a**2
      b = random.choice([x for x in range(1,13)])
      bSquared = b**2
    else:
      a = random.choice([x for x in range(2,13)])
      aSquared = a**2
      b = random.choice([x for x in range(1,13) if gcd(x**2,aSquared) == 1])
      bSquared = b**2

    self.worksheetQuestion = f"{aSquared}x^2-{bSquared}"
    self.worksheetQuestion = formatMathString(self.worksheetQuestion)
    self.answer = f"({a}x+{b})({a}x-{b})"
    self.answer = formatMathString(self.answer)

class FactoringSolving():
  def __init__(self, difficulty=1):
    #1: gcf numX(x+num)
    #2: trinomial a = 1
    #3: trinomial a > 1
    self.kwargs = {"difficulty":[1,2,3]}

    if difficulty == 1:
      x1 = 0
      x2 = randomBetweenNot(-10,10,[0])
      gcf = random.randint(2,5)
      self.worksheetQuestion = f"{gcf}x^2+{gcf*-1*x2}x=0"
      self.answer = f"x={x1}, x={x2}"
    elif difficulty == 2:
      a = 1
      b1 = randomBetweenNot(-10,10,[0])
      b2 = randomBetweenNot(-10,10,[0])
      b = b1 + b2
      c = b1*b2
      self.worksheetQuestion = f"x^2+{b}x+{c}=0"
      self.answer = f"x={-b1}, x={-b2}"
    elif difficulty == 3:
      a = random.choice([2,3,5])
      b1 = randomBetweenNot(-20,20,[item for item in range(-20,20)])
      #(ax+b2)(x+b1)
      b2 = randomBetweenNot(-100,100, [b2 for b2 in range(-100,100) if abs(b2*b1) >= 100 or b2 % a == 0 or a % b2 == 0])
      b = b1*a + b2
      c = b1 * b2
      answer1 = Fraction(-b2,a)
      self.worksheetQuestion = f"{a}x^2+{b}x+{c}=0"
      self.answer = fr"x=\frac{{{answer1.numerator}}}{{{answer1.denominator}}}, x={-b1}"

    self.worksheetQuestion = formatMathString(self.worksheetQuestion)
    self.answer = formatMathString(self.answer)

class PerfectSquareSolving():
  def __init__(self, difficulty=1):
    #1: (x+b)^2 = 0
    #2: (ax+b)^2 = 0
    self.kwargs = {"difficulty":[1,2]}

    b = randomBetweenNot(-10,10,[0])
    a = random.choice([a for a in range(2,10) if gcd(a,abs(b)) == 1])

    if difficulty == 1:
      self.worksheetQuestion = f"x^2+{2*b}x+{b**2}=0"
      self.answer = f"x={-b}, x={-b}"
    elif difficulty == 2:
      self.worksheetQuestion = f"{a**2}x^2+{2*a*b}x+{b**2}=0"
      self.answer = fr"x=\frac{{{-b}}}{{{a}}}, x=\frac{{{-b}}}{{{a}}}"

    self.worksheetQuestion = formatMathString(self.worksheetQuestion)
    self.answer = formatMathString(self.answer)

factoringTrinomialsQuestionsDict = {"FactorDOTS":FactorDOTS, "PerfectSquareSolving": PerfectSquareSolving, "FactorTrinomials": FactorTrinomials, "FactoringSolving": FactoringSolving}
