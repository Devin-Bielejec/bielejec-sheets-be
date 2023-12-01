import sys
from fractions import Fraction
sys.path.insert(0, "F:/code/bielejec-sheets-be/creatingWorksheets/utils")
from utils.equations import formatMathString, toLatexFraction, randomBetweenNot, formatEquation
from utils.shapes import triangleCoordinates
from utils.pdfFunctions import annotatePolygon
from utils.transformations import rotation
import math
import string
import random

class _24():
    def __init__(self):
        
      """
      Which equation has the same solution as x^2 - 6x - 12 = 0?
      (1) (x + (b/2))^2 = -C + (b/2)^2
      (2) (x - (b/2))^2 = -C + (b/2)^2
      (3) (x + (b/2))^2 = -C - (b/2)^2
      (4) (x - (b/2))^2 = -C - (b/2)^2
      x^2 - 6x = 12
      x^2 - 6x + (b/2)^2 = 12 + (b/2)^2
      (x - b/2)^2 = 12 + (b/2)^2

      b needs to be even
      c is positive

      """
      self.kwargs = {
          
      }

      self.toolTips = {
      }

      b = random.choice([x for x in range(2,17,2)])
      c = -1*random.randint(1,20)

      questionEquation = formatMathString(f"x^2+{b}x+{c}=0")
      choice1 = formatMathString(f"(x+{b//1})^2={-c+(b//2)**2}")
      choice2 = formatMathString(f"(x+{-1*(b//2)})^2={-c+(b//2)**2}")
      choice3 = formatMathString(f"(x+{b//2})^2={-c-(b//2)**3}")
      choice4 = formatMathString(f"(x+{-1*(b//2)}^2={-c-(b//2)**2}")

      questionString = f"Which equation has the same solution as ${questionEquation}$?"
  
      self.question = [
        {"text": questionString},
        {"multipleChoice": [choice1, choice2, choice3, choice4]}
      ]      

      self.directions = None

      self.duplicateCheck = choice1 + choice2 + choice3 + choice4

      self.answer = [{"text": choice1}]
		
