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

class _21():
    def __init__(self, difficulty=1):
        #(x+a)(x-a)
        #(bx+a)(bx-a)
        #(bx^not2+a)(bx^not2+a)
        self.kwargs = {
            "difficulty": [1,2,3],
        }

        self.toolTips = {
            "difficulty": {1: "basic", 2: "two squares", 3: "not 2 exponent"}
        }
        #(ax^exp+b)(ax^exp-b)
        var = random.choice(["x","y","z"])
        if difficulty == 1:
          a = 1
          b = random.randint(1,12)
          exp = 1
        elif difficulty == 2:
          a = random.randint(1,12)
          exp = 1
          b = random.choice([x for x in range(1,13) if x != a and gcd(a,x) == 1])
        else:
          a = random.randint(1,12)
          exp = random.choice([x for x in range(2,4,1)])
          b = random.choice([x for x in range(1,13) if x != a and gcd(a,x) == 1]) 

        answerString = formatMathString(f"({a}{var}^{exp}+{b})({a}{var}^{exp}-{b})")
        questionString = formatMathString(f"{a**2}{var}^{{{exp*2}}}-{b**2}")
        self.directions = "Factor:"
        self.question = [{"text": questionString}]

        self.duplicateCheck = f"{a}-{b}-{exp}"

        self.answer = answerString
        

