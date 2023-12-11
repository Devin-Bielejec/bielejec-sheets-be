import sys
from fractions import Fraction
sys.path.insert(0, "./creatingWorksheets/utils")
from utils.equations import formatMathString, toLatexFraction, randomBetweenNot
from utils.shapes import triangleCoordinates
from utils.pdfFunctions import annotatePolygon
from utils.transformations import rotation
import math
import string
import random

class _20():
    def __init__(self, difficulty=1):
        #diff1 (x^a+b)(x^[not a]+c)
        #diff2 (dx^a+b)(ex^[not a]+c) where math.gcd(d,b)=1 and math.gcd(e,c)=1 nothing 0 b,c not -ps's
        #diff3 (dx^2+b)(ex^[not 2]+c) where d and -b ps not each other
        self.kwargs = {
            "difficulty": [1,2,3],
            
        }

        self.toolTips = {
            "difficulty": {1: "fewer coefficients", 2: "more coefficients", 3: "factor by dots afterwards"}
        }
        #diff1 (ax^b+c)(dx^e[not a]+f)
        var = random.choice(["x","y","z"])
        if difficulty == 1:
          a = 1
          b = randomBetweenNot(1,5,[0])
          c = randomBetweenNot(-12,12, [0,-1,-4,-9])
          d = 1
          e = randomBetweenNot(1,5,[a])
          f = randomBetweenNot(-12,12,[0,-1,-4,-9])
        #diff2 (ax^b+c)(dx^e[not a]+f) where math.gcd(a,c)=1 and math.gcd(d,f)=1 nothing 0 b,c not -ps's
        elif difficulty == 2:
          a = randomBetweenNot(-12,12,[0])
          b = random.choice([1,5])
          c = random.choice([x for x in range(-12,13) if (math.gcd(x,a)==1 or math.gcd(x,a)==-1) and x not in [-9,-4,-1,0]])
          d = randomBetweenNot(-12,12,[0])
          e = randomBetweenNot(1,5,[b])
          f = random.choice([x for x in range(-12,13) if (math.gcd(x,d)==1 or math.gcd(x,d)==-1) and x not in [-9,-4,-1,0]]) 
        #diff3 (ax^b=2+c)(dx^e[not 2]+f) where math.gcd(a,c)1,-1 but c -ps
        elif difficulty == 3:
          a = random.choice([x**2 for x in range(1,13)])
          aRoot = int(a**(1/2))
          b = random.choice([2])
          c = random.choice([-1*x**2 for x in range(1,13) if math.gcd(-1*x**2,a)==1 or math.gcd(-1*x**2,b)==-1])
          cRoot = int((c*-1)**(1/2))
          d = randomBetweenNot(-12,12,[0])
          e = randomBetweenNot(1,5,[b])
          f = random.choice([x for x in range(-12,13) if (math.gcd(x,d)==1 or math.gcd(x,d)==-1) and x not in [-9,-4,-1,0]])      
          answerString = formatMathString(f"({aRoot}{var}+{cRoot})({aRoot}{var}-{cRoot})({d}{var}^{e}+{f})")
        
        if difficulty == 1 or difficulty == 2:
          answerString = formatMathString(f"({a}{var}^{{{b}}}+{c})({d}{var}^{{{e}}}+{f})")
        
        questionString = formatMathString(f"{a*d}{var}^{{{b+e}}}+{a*f}{var}^{{{b}}}+{c*d}{var}^{{{e}}}+{c*f}")
        self.directions = "Factor:"
        self.question = [{"text": questionString}]

        self.duplicateCheck = f"{a}-{b}-{c}-{d}-{e}-{f}"

        self.answer = answerString
        

