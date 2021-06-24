import sys
from fractions import gcd, Fraction
sys.path.insert(0, "F:/code/bielejec-sheets-be/creatingWorksheets/utils")
from equations import formatMathString, toLatexFraction, randomBetweenNot
import math
import string
import random

class _3():
  def __init__(self, difficulty=1):
    self.kwargs = {"difficulty":[1,2,3]}
    self.toolTips = {"difficulty":{1:"ax+b=cx",2:"ax+b=cx+d",3:"fractions in answer"}}
    """
    x on both sides equations
    # on both sides equations
    ax+b=cx diff1 -> (a-c)x = -b -> -b/(a-c) = ans
    ax+b=cx+d diff2 -> (a-c)x = (d-b) -> (d-b)/(a-c) = ans
    diff3 fraction
    """
    #x+a=b
    var = random.choice([letter for letter in string.ascii_lowercase if letter not in ["o","b","f","a","q","t","u","v","i","l","c"]])


    ans = random.choice([num for num in range(-10,11) if num != 0])

    if difficulty == 1:
        a = random.choice([num for num in range(-10,11) if num not in [0]])
        c = random.choice([num for num in range(-10,11) if a-num not in [-1,0,1] and num not in [0]])
        b = -1*ans*(a-c)
        self.worksheetQuestion = formatMathString(f"{a}{var}+{b}={c}{var}")
        self.worksheetAnswer = formatMathString(fr"{var}={ans}")
    elif difficulty == 2:
        a = random.choice([num for num in range(-10,11) if num not in [0]])
        c = random.choice([num for num in range(-10,11) if a-num not in [-1,0,1] and num not in [0]])
        bdDifference = ans*(a-c)
        b = random.choice([num for num in range(-10,11) if num not in [0,-bdDifference]])
        d = bdDifference + b
        self.worksheetQuestion = formatMathString(f"{a}{var}+{b}={c}{var}+{d}")
        self.worksheetAnswer = formatMathString(fr"{var}={ans}")
    elif difficulty == 3:
        denos = []
        for ansNum in range(-20,21):
            for ansDenom in range(2,11):
                if ansNum not in [-1,0,1] and ansDenom not in [-1,0,1] and gcd(ansDenom, ansNum) == 1:
                    denos.append([ansDenom, ansNum])
        random.shuffle(denos)
        ansNum = denos[0][1]
        ansDenom = denos[0][0]

        b = random.choice([num for num in range(-10,11) if num not in [0,-ansNum]])
        d = ansNum + b

        c = random.choice([num for num in range(-10,11) if num not in [0,-ansDenom]])
        a = ansDenom + c
        self.worksheetQuestion = formatMathString(f"{a}{var}+{b}={c}{var}+{d}")
        self.worksheetAnswer = formatMathString(fr"{var}=\frac{{{ansNum}}}{{{ansDenom}}}")
