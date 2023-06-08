import sys
from fractions import gcd, Fraction
sys.path.insert(0, "F:/code/bielejec-sheets-be/creatingWorksheets/utils")
from utils.equations import formatMathString, toLatexFraction, randomBetweenNot
from utils.shapes import triangleCoordinates
from utils.pdfFunctions import annotatePolygon
from utils.transformations import rotation
import math
import string
import random

class _23():
    def __init__(self, difficulty=1):
        #difficulty 1 - one step linear
        #d/a + x/b = e/f
        
        #difficulty 2 - two step linear
        #a/b + dx/b = c/b
        #(gcf1)a/b + (gcf2)dx/b = (gcf3)c/b
        
        self.kwargs = {
            "difficulty": [1],
            
        }

        self.toolTips = {
            "difficulty": {1: "one step linear equation"}
        }
        #diff1 (x^a+b)(x^d[not a]+c)
        var = random.choice(["x","y","z"])
      
        if difficulty == 1:
          #difficulty 1 - one step linear
          #d/a + x/b = e/f
          a = random.randint(2,10)
          d = random.choice([i for i in range(2,30) if gcd(i,a) == 1])
          a = a*random.choice([-1,1])
          
          b = random.randint(2,20)
          b = b*random.choice([-1,1])
          
          e = random.randint(1,20)
          #Keep fraction smaller side
          try:
            f = random.choice([i for i in range(2,30) if gcd(e,i) == 1 and (abs(Fraction(e/i-d/a)*b).limit_denominator().numerator) <= 100])
          except:
            f = random.choice([i for i in range(2,30) if gcd(e,i) == 1])

          e = e*random.choice([-1,1])
          f = f*random.choice([-1,1])
            
          
          #x = (e - d/a)*b
          answerString = "x=" + toLatexFraction((e/f-d/a)*b, simplified=False)

          questionString = toLatexFraction(d,a)
          sign = "-" if b < 0 else "+"
          questionString += sign
          questionString += fr"\frac{{{'x'}}}{{{abs(b)}}}"
          questionString += "="
          questionString += toLatexFraction(e,f)
        elif difficulty == 2:
          #ax/bx + c/d = e/fx
          a = randomBetweenNot(-10,10,[0])
          b = random.choice([b for b in range(-20,21) if abs(gcd(a,b)) == 1])
          
          c = randomBetweenNot(-10,10,[0])
          d = random.choice([d for d in range(-20,21) if abs(gcd(c,d)) == 1])
          
          e = randomBetweenNot(-10,10,[0])
          f = random.choice([f for f in range(-20,21) if abs(gcd(e,f)) == 1])
          
        self.directions = "Solve for x:"
        self.question = [{"text": formatMathString(questionString)}]

        self.duplicateCheck = questionString

        self.answer = [{"text": formatMathString(answerString)}]
		
