import random
from fractions import Fraction, gcd
from equations import formatMathString, randomBetweenNot

def getPrimes(lowerRange, upperRange):
  primes = []

  for num in range(lowerRange,upperRange + 1):  
    if num > 1:  
        for i in range(2,num):  
            if (num % i) == 0:  
                break  
        else:  
            primes.append(num)

  return primes  

class AbsoluteValue():
  def __init__(self, difficulty=1, standardOrder=True):
    self.kwargs = {"standardOrder":False,"difficulty": [1,2,3,4,5,6]}
    """
    |ax|=b
    |x+a|=b
    |cx+a|=b

    c|x+a|=b
    c|x+a|+d=b
    c|dx+a|+e=b
    """

    b = random.randint(1,20)

    if difficulty == 1:
      a = random.choice([a for a in range(-20,20) if a not in [0,1] and b % a == 0])
      self.answer = f"x={b//a}, x={-b//a}"
      self.worksheetQuestion = f"|{a}x|={b}"
      if not standardOrder:
        self.worksheetQuestion = f"{b}=|{a}x]"
    elif difficulty == 2:
      a = randomBetweenNot(-20,20,[0])
      self.worksheetQuestion = f"|x+{a}|={b}"
      self.answer = f"x={b-a}, x={-b-a}"
      if not standardOrder:
        self.worksheetQuestion = f"|{a}+x|={b}"
    elif difficulty == 3:
      a = randomBetweenNot(-20,20,[0])
      c = random.choice([c for c in range(-20,21) if c not in [0,1] and (b-a) % c == 0 and (-b-a) % c == 0])
      self.worksheetQuestion = f"|{c}x+{a}|={b}"
      self.answer = f"x={(b-a)//c}, {(-b-a)//c}"
      if not standardOrder:
        self.worksheetQuestion = f"|{a}+{c}x|={b}"
    elif difficulty == 4:
      c = random.choice([c for c in range(2,21) if b % c == 0 and -b % c == 0])
      a = randomBetweenNot(-20,21,[0])
      self.worksheetQuestion = f"{c}|x+{a}|={b}"
      self.answer = f"x={b//c-a}, x={-b//c-a}"
      if not standardOrder:
        self.worksheetQuestion = f"{b}={c}|{a}+x|"
    elif difficulty == 5:
      a = randomBetweenNot(-20,21,[0])
      d = randomBetweenNot(-20,21,[0])
      c = random.choice([c for c in range(-20,21) if c not in [0,1] and (b-d) % c == 0 and (b-d)//c > 0])
      self.worksheetQuestion = f"{c}|x+{a}|+{d}={b}"
      self.answer = f"x={(b-d)//c-a}, x={-(b-d)//c-a}"
      if not standardOrder:
        self.worksheetQuestion = f"{d}+{c}|{a}+x|={b}"
    elif difficulty == 6:
      e = randomBetweenNot(-20,21,[0])
      c = random.choice([c for c in range(-20,21) if c not in [0,1] and (b-e) % c == 0 and (b-e)//c > 0])
      a = randomBetweenNot(-20,21,[0])
      d = random.choice([d for d in range(-20,21) if d not in [0,1] and (((b-e)//c-e)-a) % d == 0 and (((-b-e)//c-e)-a) % d == 0])
      self.worksheetQuestion = f"{c}|{d}x+{a}|+{e}={b}"
      isolatedRightSide = (b-e)//c

      self.answer = f"x={(isolatedRightSide-a)//d}, x={(-isolatedRightSide-a)//d}"
      if not standardOrder:
        self.worksheetQuestion = f"{e}+{c}|{a}+{d}x|={b}"

    self.worksheetAnswer = formatMathString(self.answer)
    self.worksheetQuestion = formatMathString(self.worksheetQuestion)

absoluteValueQuestionsDict = {"AbsoluteValue": AbsoluteValue}