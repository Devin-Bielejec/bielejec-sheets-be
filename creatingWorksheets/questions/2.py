import sys
from fractions import Fraction
sys.path.insert(0, "./creatingWorksheets/utils")
from equations import formatMathString, toLatexFraction, randomBetweenNot
import math
import string
import random

class _2():
  def __init__(self, firstStep="add", secondStep="multiply", difficulty=1):
    self.kwargs = {"firstStep":["add","subtract"], "secondStep":["multiply", "divide"], "difficulty":[1,2,3]}
    self.toolTips = {"firstStep":{"add": "1st operation to solve","subtract": "1st operation to solve"}, "secondStep":{"multiply": "2nd operation to solve", "divide": "2nd operation to solve"}, "difficulty":{1:"ax+b=c",2:"includes negative numbers and fractions",3:"b+ax=c"}}
    """
    2 step equations
    add/subtract# divide/multiply
    ax+b=c -> c-b/a = ans
    ax-b=c
    x/a+b=c -> (c-b)*a = ans
    x/a-b=c
    diff 2, negative numbers/fractions
    diff 3, change order (b +ax etc)
    """
    #x+a=b
    var = random.choice([letter for letter in string.ascii_lowercase if letter not in ["o","b","f","a","q","t","u","v","i","l","c"]])


    ans = random.choice([num for num in range(-10,11) if num not in [-1,0,1]])

    self.answer = formatMathString(f"{var}={ans}")
    self.directions = f"Solve:"
    if firstStep == "subtract":
        b = random.randint(1,10)
    elif firstStep == "add":
        b = random.randint(-10,-1)

    if secondStep == "divide":
        if difficulty == 1:
            a = random.choice([num for num in range(-10,11) if num not in [-1,0,1]])
        else:
            a = random.choice([num for num in range(-10,-1)])

        c = ans*a+b
        if difficulty == 3:
            self.question = formatMathString(f"{b}+{a}{var}={c}")
        else:
            self.question = formatMathString(f"{a}{var}+{b}={c}")

    elif secondStep == "multiply":
        if difficulty == 1:
            a = random.choice([num for num in range(-10,11) if num not in [-1,0,1] and ans % num == 0])
        else:
            a = random.choice([num for num in range(-10,-1) if ans % num == 0])
        c = int(ans/a)+b
        if difficulty == 3:
            self.question = formatMathString(fr"{b}+\frac{{{var}}}{{{a}}}={c}")
        else:
            self.question = formatMathString(fr"\frac{{{var}}}{{{a}}}+{b}={c}")