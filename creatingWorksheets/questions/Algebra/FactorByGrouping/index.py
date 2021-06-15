import random
from fractions import Fraction, gcd
from equations import formatMathString, randomBetweenNot

class FactorByGrouping():
  def __init__(self):
    """
    (ax^f+b)(cx^g+d)
    """

    #first exponent rand between 1 and 5
    f = random.randint(1,5)
    #second exponent just not first
    g = random.choice([g for g in range(1,6) if g != f])

    #a and c can be regularly set - make positive to help with answer
    a = randomBetweenNot(1,10,[0])
    c = randomBetweenNot(1,10,[0])
    
    #gcd(a,b) == 1 and same for c and d
    #If f or g == even, make sure b and d aren't pSquares
    pSquares = [x**2 for x in range(1,13)]

    if f % 2 != 0:
      b = random.choice([b for b in range(-10,11) if b != 0 and gcd(a,b) == 1 or gcd(a,b) == -1])
    else:
      b = random.choice([b for b in range(-10,11) if b != 0 and gcd(a,b) == 1 or gcd(a,b) == -1 and b not in pSquares])
    

    if g % 2 != 0:
      d = random.choice([d for d in range(-10,11) if d != 0 and gcd(c,d) == 1 or gcd(c,d) == -1])
    else:
      d = random.choice([d for d in range(-10,11) if d != 0 and gcd(c,d) == 1 or gcd(c,d) == -1 and d not in pSquares])
    

    #(ax^f+b)(cx^g+d)
    self.answer = formatMathString(f"({a}x^{f}+{b})({c}x^{g}+{d})")

    #acx^{f+g}+adx^f+bcx^g+bd
    #For Standard form
    if f > g:
      self.worksheetQuestion = f"{a*c}x^{f+g}+{a*d}x^{f}+{b*c}x^{g}+{b*d}"
    else:
      self.worksheetQuestion = f"{a*c}x^{f+g}+{b*c}x^{g}+{a*d}x^{f}+{b*d}"

    self.worksheetAnswer = formatMathString(self.answer)
    self.worksheetQuestion = formatMathString(self.worksheetQuestion)

factorByGroupingQuestionsDict = {"FactorByGrouping": FactorByGrouping}