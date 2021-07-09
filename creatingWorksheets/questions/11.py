import sys
from fractions import gcd, Fraction
sys.path.insert(0, "F:/code/bielejec-sheets-be/creatingWorksheets/utils")
from equations import formatMathString, toLatexFraction, randomBetweenNot
import math
import string
import random


#System of 2x2 equations with finite solutions
class _11():
  def __init__(self, difficulty=1):
    self.kwargs = {"difficulty":[1,2,3]}
    self.toolTips = {"difficulty": {1:"add equations", 2:"multiply one equation", 3:"multiply both equations"}}
    #2x2
    """
    diff1 add equations
    diff2 multiply one equation
    diff3 multiply both equations
    """
    v1 = "x"
    v2 = "y"
    if difficulty == 1:
        #ax+by=c
        #-ax+dy=e
        a = randomBetweenNot(-10,10,[0])
        b = randomBetweenNot(-10,10,[0])
        x = randomBetweenNot(-10,10)
        y = randomBetweenNot(-10,10)

        c = a*x+b*y

        d = randomBetweenNot(-10,10,[0,-b])

        e = -1*a*x+d*y

        self.question = f"{a}{v1}+{b}{v2}={c}\n{-a}{v1}+{d}{v2}={e}"
        self.answer = formatMathString(f"{v1}={x}, {v2}={y}")
    elif difficulty == 2:
        #ax+by=c
        #multax+dy=e
        a = randomBetweenNot(-10,10,[0])
        b = randomBetweenNot(-10,10,[0])
        x = randomBetweenNot(-10,10)
        y = randomBetweenNot(-10,10)

        c = a*x+b*y

        #not technically multiple, more factor
        multiple = random.choice([x for x in range(-10,11) if x not in [-1,0,1]])
        aM = multiple*a

        #d cannot be the same multiple as a or else we have infinite solutions
        d = random.choice([num for num in range(-10,10) if num not in [0, multiple*b, -1*multiple*b]])
        
        e = aM*x+d*y
    
        self.question = f"{a}{v1}+{b}{v2}={c}\n{aM}{v1}+{d}{v2}={e}"
        self.answer = formatMathString(f"{v1}={x}, {v2}={y}")        
    else:
        #ax+by=c
        #dx+ey=f
        #gcd(a,d) == 1 but neither 1 or -1
        a = randomBetweenNot(-10,10,[0,1,-1])
        b = randomBetweenNot(-10,10,[0])
        x = randomBetweenNot(-10,10)
        y = randomBetweenNot(-10,10)

        c = a*x+b*y

        d = random.choice([d for d in range(-10,11) if (gcd(d,a) == 1 or gcd(d,a) == -1) and d not in [1,-1,0]])
        #Ensures we don't have infinite solutions
        e = randomBetweenNot(-10,10,[0, int(d/a*b), -1*int(d/a*b)])
        f = d*x + e*y
        self.question = f"{a}{v1}+{b}{v2}={c}\n{d}{v1}+{e}{v2}={f}"
        self.answer = f"{v1}={x}, {v2}={y}"    

    
    self.directions = "Solve the system for each variable: "

    #Take the worksheetQuestions and put them into a list form
    partsOfQuestion = self.question.split("\n")

    self.duplicateCheck = ""
    #Center environment but aligned equations by =
    self.question = [{"text": {"center-aligned": []}}]
    for part in partsOfQuestion:
        self.question[0]["text"]["center-aligned"].append(formatMathString(part))
        self.duplicateCheck += formatMathString(part)