from pylatex import (Document, TikZ, TikZNode, Plot,
                     TikZDraw, TikZCoordinate, Axis, Tabular,
                     TikZUserPath, TikZOptions, Center, VerticalSpace, NewLine, Math, Alignat, Section, NewLine)
from pylatex.utils import (NoEscape, bold)
import sys
sys.path.insert(0, "F:/code/bielejec-sheets-be/creatingWorksheets/utils")
from questionFormatting import multipleChoice, multipleChoicePic
from equations import formatMathString, randomBetweenNot
from docRelated import alignedEquations
from graphs import graphLinearFunction, shadeLinearInequality, axisOptions
import math, fractions, numpy, string, uuid, random

"""

x^2 = PS
x^2 + a = PS
ax^2 + b = PS

(x+a)^2 = PS
(x+a)^2 + b = PS
c(x+a)^2 + b = PS
"""
class SquareRootSolving():
  def __init__(self, difficulty=1):
    self.kwargs = {"difficulty":[1,2,3,4,5,6]}

    x1 = random.randint(1,10)
    x2 = -x1
    ps = x1*x1

    a = randomBetweenNot(-10,10,[0])
    b = randomBetweenNot(-10,10,[0])
    c = randomBetweenNot(-10,10,[0])

    self.answer = f"x={x1}, x={x2}"
    if difficulty == 1:
      self.worksheetQuestion = f"x^2={ps}"
    elif difficulty == 2:
      self.worksheetQuestion = f"(x+{a})^2={ps}"
      x1 = x1 - a
      x2 = x2 - a
    elif difficulty == 3:
      self.worksheetQuestion = f"x^2+{a}={ps+a}"
    elif difficulty == 4:
      self.worksheetQuestion = f"(x+{a})^2+{a}={ps+a}"
      x1 = x1 - a
      x2 = x2 - a
    elif difficulty == 5:
      self.worksheetQuestion = f"{b}x^2+{a*b}={(ps+a)*b}"
    elif difficulty == 6:
      self.worksheetQuestion = f"{b}(x+{c})^2+{a*b}={(ps+a)*b}"
      x1 = x1 - c
      x2 = x2 - c

    self.worksheetQuestion = formatMathString(self.worksheetQuestion)
    self.answer = formatMathString(f"x={x1}, x={x2}")


squareRootSolvingQuestionsDict = {"SquareRootSolving": SquareRootSolving}
