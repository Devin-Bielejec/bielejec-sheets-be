import random
from fractions import Fraction, gcd
from equations import formatMathString, randomBetweenNot

class RadicalEquations():
  def __init__(self, difficulty=1):
    self.kwargs = {"difficulty": [1,2,3,4,5]}
    """
    sqrt(ax+b)=x -> Ax^2 + Bx + C = 0
    
    sqrt(ax)=bx -> b^2x^2 - ax 

    sqrt(ax+b)=x+c -> x^2 + (2c - a)x + (-b + c^2)
    sqrt(ax+b)-c=x
    sqrt(ax+b)-x=c
    
    """
    
    b1 = randomBetweenNot(-15,16,[0])
    b2 = randomBetweenNot(-15,16,[0])
    A = 1
    B = b1 + b2
    C = b1 * b2
    if difficulty == 1:
      a = -B
      b = -C
      self.answer = f"x={-b2}, x={-b1}"
      self.worksheetQuestion = fr"\sqrt{{{a}x+{b}}}=x"
    elif difficulty == 2:
      b = random.randint(1,10)
      a = randomBetweenNot(-20,21,[0])
      x1 = 0
      x2 = Fraction(a, b**2)
      x2Num = x2.numerator
      x2Denom = x2.denominator
      self.worksheetQuestion = fr"\sqrt{{{a}x}}={b}x"
      self.answer = fr"x=0, x=\frac{{{x2Num}}}{{{x2Denom}}}"
    elif difficulty >= 3:
      c = randomBetweenNot(-20,21,[0])
      a = -(B - 2*c)
      b = -(C - c**2)
      self.answer = f"x={-b1}, x={-b2}"
      if difficulty == 3:
        self.worksheetQuestion = fr"\sqrt{{{a}x+{b}}}=x+{c}"
      elif difficulty == 4:
        self.worksheetQuestion = fr"\sqrt{{{a}x+{b}}}-{c}=x"
      elif difficulty == 5:
        self.worksheetQuestion = fr"\sqrt{{{a}x+{b}}}-x={c}"

    self.worksheetQuestion = formatMathString(self.worksheetQuestion)
    self.answer = formatMathString(self.answer)

radicalEquationsQuestionsDict = {"RadicalEquations": RadicalEquations}