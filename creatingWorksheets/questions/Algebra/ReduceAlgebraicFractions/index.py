import random
from fractions import Fraction, gcd
from equations import formatMathString, randomBetweenNot

class ReduceAlgebraicFractions():
  def __init__(self, difficulty=3):
    self.kwargs = {"difficulty": [1,2,3]}
    """
    tri/dots or dots/tri
    tri/tri
    harderTri/harderDots or harderDots/harderTri
    """

    a = randomBetweenNot(-12,12,[0])
    print(a)
    b = random.choice([x for x in range(-100,101) if -100 <= x*a <= 150 and x != 0 and a + x != 0])
    c = randomBetweenNot(-12,12,[0])
    d = randomBetweenNot(2,5,[4])

    #(x+a)(x+b)/(x+a)(x-a)
    if difficulty == 1:
      top = f"x^2+{a+b}x+{a*b}"
      topAnswer = f"(x+{b})"
      bottom = f"x^2-{a**2}"
      bottomAnswer = f"(x-{a})"
    #(x+a)(x+b)/(x+a)(x+c)
    elif difficulty == 2:
      top = f"x^2+{a+b}x+{a*b}"
      topAnswer = f"(x+{b})"
      bottom = f"x^2+{a+c}x+{a*c}"
      bottomAnswer = f"(x+{c})"
    #(dx+a)(x+b)/(dx+a)(dx-a)
    elif difficulty == 3:
      a = random.choice([a for a in range(-12,13) if gcd(a,d) == 1])
      b = random.choice([b for b in range(-100,101) if a*b <= 150 and b != 0])
      top = f"{d}x^2+{a+b*d}x+{a*b}"
      topAnswer = f"(x+{b})"
      bottom = f"{d**2}x^2-{a**2}"
      bottomAnswer = f"({d}x-{a})"
    
    order = random.randint(1,2)
    if order == 1:
      self.worksheetQuestion = r"\frac{{{top}}}{{{bottom}}}".format(top=top, bottom=bottom)
      self.answer = r"\frac{{{topAnswer}}}{{{bottomAnswer}}}".format(topAnswer=topAnswer,bottomAnswer=bottomAnswer)
    else:
      self.worksheetQuestion = r"\frac{{{bottom}}}{{{top}}}".format(bottom=bottom, top=top)
      self.answer = r"\frac{{{bottomAnswer}}}{{{topAnswer}}}".format(bottomAnswer=bottomAnswer,topAnswer=topAnswer)

    self.answer = formatMathString(self.answer)
    self.worksheetAnswer = formatMathString(self.answer)
    self.worksheetQuestion = formatMathString(self.worksheetQuestion)

reduceAlgebraicFractionsQuestionsDict = {"ReduceAlgebraicFractions": ReduceAlgebraicFractions}