import sys
from fractions import gcd, Fraction
sys.path.insert(0, "F:/code/bielejec-sheets-be/creatingWorksheets/utils")
from equations import formatMathString, toLatexFraction, randomBetweenNot
import math
import string
import random

class _1():
  def __init__(self, firstStep="add", difficulty=1):
    self.kwargs = {"firstStep": ["add","subtract", "multiply", "divide"], "difficulty":[1,2,3]}
    self.toolTips = {"variable":"Variable to use","firstStep": "Operation to solve", "difficulty": {1: "Positive number result", 2:"Postive number result with larger numbers", 3:"Negative number result"}}

    #x+a=b
    var = random.choice([letter for letter in string.ascii_lowercase if letter not in ["o","b","f","a","q","t","u","v","i","l","c","d"]])

    if firstStep == "subtract":
        #whole number b - a easy subtraction
        if difficulty == 1:
            a = random.choice([num for num in range(1,18)])
            b = random.choice([num for num in range(a,20)])
        #b - a subtraction with larger numbers
        elif difficulty == 2:
            a = random.choice([num for num in range(1,45)])
            b = random.choice([num for num in range(a,51)])
        #b - a subtraction with negative numbers
        elif difficulty == 3:
            abChoices = []
            for b in range(-50,51):
                for a in range(-50,51):
                    if b - a < 0 and a > 0:
                        abChoices.append([a,b])
            random.shuffle(abChoices)

            b = abChoices[0][1]
            a = abChoices[0][0]

        self.question = formatMathString(f"{var}+{a}={b}")
        self.answer = formatMathString(f"{var}={b-a}")
    elif firstStep == "add":
        #whole number b - a easy addition
        if difficulty == 1:
            a = random.choice([num for num in range(1,10)])
            b = random.choice([num for num in range(1,10)])
        #b + a subtraction with larger numbers
        elif difficulty == 2:
            a = random.choice([num for num in range(1,50)])
            b = random.choice([num for num in range(1,50)])
        #b - a subtraction with negative numbers
        elif difficulty == 3:
            abChoices = []
            for b in range(-50,51):
                for a in range(-50,51):
                    if b + a < 0 and a > 0:
                        abChoices.append([a,b])
            random.shuffle(abChoices)

            b = abChoices[0][1]
            a = abChoices[0][0]

        self.question = formatMathString(f"{var}-{a}={b}")
        self.answer = formatMathString(f"{var}={b+a}")

    elif firstStep == "multiply":
        #x/a = b
        if difficulty == 1:
            a = random.randint(2,15)
            b = random.randint(1,15)
            self.answer = formatMathString(f"{var}={a*b}")
        #x/-a = b
        elif difficulty == 2:
            a = -1*random.randint(2,15)
            b = random.randint(1,15)
            self.answer = formatMathString(fr"{var}={b*-a}")
        #x/-a = -b
        elif difficulty == 3:
            a = -1*random.randint(2,15)
            b = -1*random.randint(1,15)
            self.answer = formatMathString(fr"{var}={b*a}")
        self.question = formatMathString(fr"\frac{{{var}}}{{{a}}}={b}")

    elif firstStep == "divide":
        #b/a=ans, so ans*a = b
        if difficulty == 1:
            ans = random.choice([num for num in range(-20,20) if num != 0])
            a = random.choice([num for num in range(-10,10) if num != 0])
            b = ans * a
            self.answer = formatMathString(f"{var}={int(b/a)}")
        #b/a reduced fraction
        elif difficulty == 2:
            ansNum = random.choice([num for num in range(-100,101) if num != 0])
            ansDenom = random.choice([num for num in range(-100,101) if num != 0 and math.gcd(ansNum, num) == 1 or math.gcd(ansNum,num) == -1])
            b = ansNum
            a = ansDenom
            self.answer = formatMathString(fr"{var}=\frac{{{ansNum}}}{{{ansDenom}}}")
        #b - a have to reduce fraction
        elif difficulty == 3:
            ansNum = random.choice([num for num in range(-100,101) if num != 0])
            ansDenom = random.choice([num for num in range(-100,101) if num != 0 and math.gcd(ansNum, num) == 1 or math.gcd(ansNum,num) == -1])
            
            gcf = random.randint(2,10)

            b = ansNum*gcf
            a = ansDenom*gcf
            self.answer = formatMathString(fr"{var}=\frac{{{ansNum}}}{{{ansDenom}}}")

        self.question = formatMathString(f"{a}{var}={b}")

    self.directions = f"Solve:"