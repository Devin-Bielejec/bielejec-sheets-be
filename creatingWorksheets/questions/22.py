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

class _22():
    def __init__(self, option="sum",difficulty=1):
      #var^3 +- num^3
      #var^(num%3) +- num^3
      #num^3var^(num%3) +- num^3
      #num^3var^(num%3) +- num^3var2^(num%3)
      self.kwargs = {
            "option": ["sum","difference"],
            "difficulty": [1,2,3,4],
        }

      self.toolTips = {
          "difficulty": {1: "var^3 +- num^3", 2: "var^(num%3) +- num^3", 3: "num^3var^(num%3) +- num^3", 4: "num^3var^(num%3) +- num^3var2^(num%3)"}, "option": {"sum": "adding", "difference": "subtracting"}
      }
      var1 = random.choice(["x","y","z"])
      var2 = random.choice([item for item in ["x","y","z"] if item != var1])
      if difficulty == 1:
        #exponent is 1 (after cube rooting)
        var1Exp = 1
        var2Exp = 1
      else:
        #Exponents are between 1 and 5
        var1Exp = random.randint(1,5)
        var2Exp = random.randint(1,5)
      num1 = random.randint(1,12)
      #num2 cubed needs to be coprime of num1 cubed
      num2 = random.choice([item for item in range(1,13) if gcd(item**3,num1**3) == 1 or gcd(item**3,num1**3) == -1])
      sign = "+" if option == "sum" else "-"
      oppSign = "-" if option == "sum" else "+"
      if difficulty == 1:
        #var^3 pm num^3
        #Answer - (var pm num)(var^2 opp num*var + num^2)
        answerString = formatMathString(f"({var1}{sign}{num1})({var1}^2{oppSign}{num1}{var1}+{num1**2})")
        questionString = formatMathString(f"{var1}^3{sign}{num1**3}")
      elif difficulty == 2:
        #var^{exp%3} pm num^3
        answerString = formatMathString(f"({var1}^{{{var1Exp}}}{sign}{num1})({var1}^{{{var1Exp*2}}}{oppSign}{num1}{var1}^{{{var1Exp}}}+{num1**2})")
        questionString = formatMathString(f"{var1}^{{{var1Exp*3}}}{sign}{num1**3}")
      elif difficulty == 3:
        #num1var pm num2
        answerString = formatMathString(f"({num1}{var1}^{{{var1Exp}}}{sign}{num2})({num1**2}{var1}^{{{var1Exp*2}}}{oppSign}{num1*num2}{var1}^{{{var1Exp}}}+{num2**2})")
        questionString = formatMathString(f"{num1**3}{var1}^{{{var1Exp*3}}}{sign}{num2**3}")
      elif difficulty == 4:
        #num1var1 pm num2var2
        answerString = formatMathString(f"({num1}{var1}^{{{var1Exp}}}{sign}{num2}{var2}^{{{var2Exp}}})({num1**2}{var1}^{{{var1Exp*2}}}{oppSign}{num1*num2}{var1}^{{{var1Exp}}}{var2}^{{{var2Exp}}}+{num2**2}{var2}^{{{var2Exp**2}}})")
        questionString = formatMathString(f"{num1**3}{var1}^{{{var1Exp*3}}}{sign}{num2**3}{var2}^{{{var2Exp*3}}}")
      
      self.directions = "Factor:"
      self.question = [{"text": questionString}]

      self.duplicateCheck = f"{var1}{var2}{num1}{num2}{var1Exp}{var2Exp}"

      self.answer = answerString
        

