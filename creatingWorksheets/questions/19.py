import sys
from fractions import Fraction
sys.path.insert(0, "F:/code/bielejec-sheets-be/creatingWorksheets/utils")
from utils.equations import formatMathString, toLatexFraction, randomBetweenNot, getFactorPairs
from utils.shapes import triangleCoordinates
from utils.pdfFunctions import annotatePolygon
from utils.transformations import rotation
import math
import string
import random

#factoring a trinomial a > 1 but not factoring completely
"""
per signs
difficulty = [1,2]
1 is that a prime
2 is that a is not prime
"""
class _19():
    def __init__(self, option="++", difficulty=1):
        """
        ++
        -+
        +-
        --
        """
        self.kwargs = {
            "option": ["++","-+","+-","--"],
            "difficulty": [1,2]
            
        }

        self.toolTips = {
            "option": {"++": "all positive coefficients", "--": "all negative coefficients", "-+": "- b coefficent + c coefficient", "+-": "+ b coefficient - c coefficient"},
            "difficulty": {1: "a coefficient is prime", 2: "a coefficient is not prime"}
        }  

        if difficulty == 1:
            #a is prime
            prime = random.choice([2,3,5,7])
            a1 = prime
            a2 = 1
        elif difficulty == 2:
            #Making a1 bigger or equal
            aList = random.choice([[5,2], [5,4],[5,3],[4,3], [3,2], [3,3], [2,2], [4,4]])
            a1 = aList[0]
            a2 = aList[1]

        if option == "++":
            f1 = random.choice([num for num in range(1,13) if math.gcd(num,a1) == 1])
            f2 = random.choice([num for num in range(1,13) if math.gcd(num,a2) == 1])
        elif option == "-+":
            f1 = -1*random.choice([num for num in range(1,13) if math.gcd(num,a1) == 1])
            f2 = -1*random.choice([num for num in range(1,13) if math.gcd(num,a2) == 1])
        #Pos factor is bigger
        elif option == "+-":
            f1 = random.choice([num for num in range(1,13) if math.gcd(num,a1) == 1])
            #and make sure f1*a2 does not equal f2*a1 which would create 0 in the middle
            f2 = random.choice([num for num in range(1,13) if math.gcd(num,a2) == 1 and f1*a2 != num*a1])
            #check if f1 * a2 is bigger, then make f1 positive else f2 positive
            if f1 * a2 > f2 * a1:
                f2 = -1*f2
            else:
                f1 = -1*f1
        elif option == "--":
            f1 = random.choice([num for num in range(1,13) if math.gcd(num,a1) == 1])
            #and make sure f1*a2 does not equal f2*a1 which would create 0 in the middle
            f2 = random.choice([num for num in range(1,13) if math.gcd(num,a2) == 1 and f1*a2 != num*a1])
            #check if f1 * a2 is bigger, then make f1 positive else f2 positive
            if f1 * a2 < f2 * a1:
                f2 = -1*f2
            else:
                f1 = -1*f1
 
        questionString = formatMathString(f"{a1*a2}x^2+{f1*a2+f2*a1}x+{f1*f2}")
        self.directions = "Factor:"
        self.question = [{"text": questionString}]

        self.duplicateCheck = f"{f1}-{f2}"

        answerString = formatMathString(f"({a1}x+{f1})({a2}x+{f2})")
        self.answer = answerString
		
        

