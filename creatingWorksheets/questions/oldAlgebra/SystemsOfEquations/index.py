"""

combine like terms
.
combine two terms
combine two terms on both sides
two distribute on one side

"""

#Combine two terms
import random, sys, re
from math import gcd
sys.path.insert(0, "F:/code/bielejec-sheets-be/creatingWorksheets/utils")
from equations import formatMathString, toLatexFraction, randomBetweenNot

class SystemsOfEquations():
  def __init__(self, variables = 2, difficulty = 1, solutionType="Solutions"):
    self.kwargs = {"variables": [2,3], "difficulty": [1,2,3], "solutionType": ["Solutions", "No Solutions", "Infinite Solutions"]}

    #2x2
    """
    diff 1 ax+by=c
          -ax+dy=e
    
    diff 2 ax+by=c
          aMx+dy = e

    diff 3 ax+by=c
          dx+ey=f   where gcd(a,d) == 1

    No solutions, x and y coefficients are multiples but #'s on right aren't
    Infinite Solutions, make second equation a multiple of first

    """
    v1 = "x"
    v2 = "y"
    if variables == 2:
      if difficulty == 1:
        a = randomBetweenNot(-10,10,[0])
        b = randomBetweenNot(-10,10,[0])
        x = randomBetweenNot(-10,10)
        y = randomBetweenNot(-10,10)

        c = a*x+b*y

        d = randomBetweenNot(-10,10,[0,-b])

        e = -1*a*x+d*y

        if solutionType == "No Solutions":
          #if 0 = 0, infinite solutions
          e = e - 1 if c+e == 0 else e
          #make a,b - verions of a,b
          self.worksheetQuestion = f"{a}{v1}+{b}{v2}={c}\n{-a}{v1}+{-b}{v2}={e}"
          self.worksheetAnswer = "No Solutions"
        elif solutionType == "Infinite Solutions":
          #a,b,c all multiples of -1
          mult = -1
          self.worksheetQuestion = f"{a}{v1}+{b}{v2}={c}\n{a*mult}{v1}+{b*mult}{v2}={c*mult}"
          self.worksheetAnswer = "Infinite Solutions"
        else:
          self.worksheetQuestion = f"{a}{v1}+{b}{v2}={c}\n{-a}{v1}+{d}{v2}={e}"
          self.worksheetAnswer = formatMathString(f"{v1}={x}, {v2}={y}")
      elif difficulty == 2:
        #second a is a mult of first a
        a = randomBetweenNot(-10,10,[0])
        b = randomBetweenNot(-10,10,[0])
        x = randomBetweenNot(-10,10)
        y = randomBetweenNot(-10,10)

        c = a*x+b*y

        multiple = random.randint(2,4)
        aM = multiple*a

        #d cannot be the same multiple as a or else we have infinite solutions
        d = random.choice([num for num in range(-10,10) if num not in [0, multiple*b, -1*multiple*b]])
        
        e = aM*x+d*y
        if solutionType == "No Solutions":
          #if 0 = 0, infinite solutions
          e = e - 1 if c*aM+e == 0 else e
          #make a,b - verions of a,b
          self.worksheetQuestion = f"{a}{v1}+{b}{v2}={c}\n{aM}{v1}+{b*aM}{v2}={e}"
          self.worksheetAnswer = "No Solutions"
        elif solutionType == "Infinite Solutions":
          #a,b,c all multiples
          mult = random.randint(2,5)
          self.worksheetQuestion = f"{a}{v1}+{b}{v2}={c}\n{a*mult}{v1}+{b*mult}{v2}={c*mult}"
          self.worksheetAnswer = "Infinite Solutions"
        else:
          self.worksheetQuestion = f"{a}{v1}+{b}{v2}={c}\n{aM}{v1}+{d}{v2}={e}"
          self.worksheetAnswer = formatMathString(f"{v1}={x}, {v2}={y}")        
      else:
        #gcd(a,d) == 1 but neither 1 or -1
        a = randomBetweenNot(-10,10,[0,1,-1])
        b = randomBetweenNot(-10,10,[0])
        x = randomBetweenNot(-10,10)
        y = randomBetweenNot(-10,10)

        c = a*x+b*y

        d = random.choice([num for num in range(-10,11) if gcd(num,a) == 1 and num not in [1,-1,0]])
        #Ensures we don't have infinite solutions
        e = randomBetweenNot(-10,10,[0, int(d/a*b), -1*int(d/a*b)])

        if solutionType == "No Solutions":
          x = randomBetweenNot(-10,10,[x])

        f = d*x + e*y
        if solutionType == "No Solutions":
          #if 0 = 0, infinite solutions
          e = e - 1 if c*aM+e == 0 else e
          #make a,b - verions of a,b
          self.worksheetQuestion = f"{a}{v1}+{b}{v2}={c}\n{aM}{v1}+{b*aM}{v2}={e}"
          self.worksheetAnswer = "No Solutions"
        elif solutionType == "Infinite Solutions":
          #a,b,c all multiples
          mult = random.randint(2,5)
          self.worksheetQuestion = f"{a}{v1}+{b}{v2}={c}\n{a*mult}{v1}+{b*mult}{v2}={c*mult}"
          self.worksheetAnswer = "Infinite Solutions"
        else:
          self.worksheetQuestion = f"{a}{v1}+{b}{v2}={c}\n{d}{v1}+{e}{v2}={f}"
          self.worksheetAnswer = f"{v1}={x}, {v2}={y}"    

    elif variables == 3:
      """
      a1x+b1y+c1z=d1
      a2x+b2y+c2z=d2
      a3x+b3y+c3z=d3
      """      

    print(re.search(self.worksheetAnswer, "^[ A-Za-z]+$"))
    self.worksheetAnswer = self.worksheetAnswer if re.search(self.worksheetAnswer, "^[ A-Za-z]+$") is not None else formatMathString(self.worksheetAnswer)
    #Take the worksheetQuestions and put them into a list form
    partsOfQuestion = self.worksheetQuestion.split("\n")
    self.worksheetQuestion = []
    for part in partsOfQuestion:
        self.worksheetQuestion.append({"center": True, "data": formatMathString(part)})

systemsOfEquationsQuestionsDict = {"SystemsOfEquations": SystemsOfEquations}