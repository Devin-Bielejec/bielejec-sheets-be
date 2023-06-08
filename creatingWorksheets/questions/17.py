import sys
from fractions import gcd, Fraction
sys.path.insert(0, "F:/code/bielejec-sheets-be/creatingWorksheets/utils")
from utils.equations import formatMathString, toLatexFraction, randomBetweenNot, getFactorPairs
from utils.shapes import triangleCoordinates
from utils.pdfFunctions import annotatePolygon
from utils.transformations import rotation
import math
import string
import random

#factoring a trinomial a = 1
"""
middle term sign
last number sign
"""
class _17():
    def __init__(self, option="++"):
        """
        ++
        -+
        +-
        --
        """
        self.kwargs = {
            "option": ["++","-+","+-","--"],
            
        }

        self.toolTips = {
            "option": {"++": "all positive coefficients", "--": "all negative coefficients", "-+": "- b coefficent + c coefficient", "+-": "+ b coefficient - c coefficient"}
        }

        #range between -12 and 12
        fNeg1 = randomBetweenNot(-12,-1,[0])
        fNeg2 = randomBetweenNot(-12,-1,[0,-fNeg1])

        fPos1 = randomBetweenNot(1,12,[0])
        fPos2 = randomBetweenNot(1,12,[0,-fPos1])

        if option == "++":
            f1 = fPos1
            f2 = fPos2
        elif option == "-+":
            f1 = fNeg1
            f2 = fNeg2
        #Pos factor is bigger
        elif option == "+-":
            f2 = randomBetweenNot(-11,-1,[0])
            f1 = randomBetweenNot(abs(f2),12,[0,-f2])
        #Neg factor is bigger
        elif option == "--":
            f2 = randomBetweenNot(1,11,[0])
            f1 = randomBetweenNot(-12,-1*abs(f2),[0,-f2])
 

        questionString = formatMathString(f"x^2+{f1+f2}x+{f1*f2}")
        self.directions = "Factor:"
        self.question = [{"text": questionString}]

        self.duplicateCheck = f"{f1}-{f2}"

        answerString = formatMathString(f"(x+{f1})(x+{f2})")
        self.answer = answerString
		
        

