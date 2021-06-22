import sys
from fractions import gcd, Fraction
sys.path.insert(0, "F:/code/bielejec-sheets-be/creatingWorksheets/utils")
from equations import formatMathString, toLatexFraction, randomBetweenNot
import math
import string
import random
from .index import ExpressionsAndEquationsParent

class SolvingLinearEquations(ExpressionsAndEquationsParent):
    def __init__(self):
        super().__init__()
        self.standard = "A.REI.B.3"
        self.skill = "Solve linear equations"

#Complete
class OneStepEquationWorksheet(SolvingLinearEquations):
  def __init__(self, firstStep="add", difficulty=1, variable="x"):
    super().__init__()
    self.kwargs = {"firstStep": ["add","subtract", "multiply", "divide"], "difficulty":[1,2,3], "variable":[letter for letter in string.ascii_lowercase if letter not in ["o","b","f","a","q","t","u","v","i","l","c"]]}
    self.toolTips = {"variable":"Variable to use","firstStep": "Operation to solve", "difficulty": {1: "Positive number result", 2:"Postive number result with larger numbers", 3:"Negative number result"}}
    self.id = "OneStepEquationWorksheet"
    self.notes = ""
    #x+a=b
    var = variable
    print(firstStep, difficulty, variable)
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

        self.worksheetQuestion = formatMathString(f"{var}+{a}={b}")
        self.worksheetAnswer = formatMathString(f"{var}={b-a}")
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

        self.worksheetQuestion = formatMathString(f"{var}-{a}={b}")
        self.worksheetAnswer = formatMathString(f"{var}={b+a}")

    elif firstStep == "multiply":
        #x/a = b
        if difficulty == 1:
            a = random.randint(2,15)
            b = random.randint(1,15)
            self.worksheetAnswer = formatMathString(f"{var}={a*b}")
        #x/-a = b
        elif difficulty == 2:
            a = -1*random.randint(2,15)
            b = random.randint(1,15)
            self.worksheetAnswer = formatMathString(fr"{var}={b*-a}")
        #x/-a = -b
        elif difficulty == 3:
            a = -1*random.randint(2,15)
            b = -1*random.randint(1,15)
            self.worksheetAnswer = formatMathString(fr"{var}={b*a}")
        self.worksheetQuestion = formatMathString(fr"\frac{{{var}}}{{{a}}}={b}")

    elif firstStep == "divide":
        #b/a=ans, so ans*a = b
        if difficulty == 1:
            ans = random.choice([num for num in range(-20,20) if num != 0])
            a = random.choice([num for num in range(-10,10) if num != 0])
            b = ans * a
            self.worksheetAnswer = formatMathString(f"{var}={int(b/a)}")
        #b/a reduced fraction
        elif difficulty == 2:
            ansNum = random.choice([num for num in range(-100,101) if num != 0])
            ansDenom = random.choice([num for num in range(-100,101) if num != 0 and math.gcd(ansNum, num) == 1 or math.gcd(ansNum,num) == -1])
            b = ansNum
            a = ansDenom
            self.worksheetAnswer = formatMathString(fr"{var}=\frac{{{ansNum}}}{{{ansDenom}}}")
        #b - a have to reduce fraction
        elif difficulty == 3:
            ansNum = random.choice([num for num in range(-100,101) if num != 0])
            ansDenom = random.choice([num for num in range(-100,101) if num != 0 and math.gcd(ansNum, num) == 1 or math.gcd(ansNum,num) == -1])
            
            gcf = random.randint(2,10)

            b = ansNum*gcf
            a = ansDenom*gcf
            self.worksheetAnswer = formatMathString(fr"{var}=\frac{{{ansNum}}}{{{ansDenom}}}")

        self.worksheetQuestion = formatMathString(f"{a}{var}={b}")

    self.worksheetDirections = f"Solve for {variable}"

class TwoStepEquationWorksheet(SolvingLinearEquations):
  def __init__(self, firstStep="add", secondStep="multiply", difficulty=1):
    super().__init__()
    self.kwargs = {"firstStep":["add","subtract"], "secondStep":["multiply", "divide"], "difficulty":[1,2,3]}
    self.toolTips = {"firstStep":{"add": "1st operation to solve","subtract": "1st operation to solve"}, "secondStep":{"multiply": "2nd operation to solve", "divide": "2nd operation to solve"}, "difficulty":{1:"ax+b=c",2:"includes negative numbers and fractions",3:"b+ax=c"}}
    self.id = "TwoStepEquationWorksheet"
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

    self.worksheetAnswer = formatMathString(f"{var}={ans}")

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
            self.worksheetQuestion = formatMathString(f"{b}+{a}{var}={c}")
        else:
            self.worksheetQuestion = formatMathString(f"{a}{var}+{b}={c}")

    elif secondStep == "multiply":
        if difficulty == 1:
            a = random.choice([num for num in range(-10,11) if num not in [-1,0,1] and ans % num == 0])
        else:
            a = random.choice([num for num in range(-10,-1) if ans % num == 0])
        c = int(ans/a)+b
        if difficulty == 3:
            self.worksheetQuestion = formatMathString(fr"{b}+\frac{{{var}}}{{{a}}}={c}")
        else:
            self.worksheetQuestion = formatMathString(fr"\frac{{{var}}}{{{a}}}+{b}={c}")

class VariableOnBothSidesEquationWorksheet(SolvingLinearEquations):
  def __init__(self, difficulty=1):
    super().__init__()
    self.kwargs = {"difficulty":[1,2,3]}
    self.toolTips = {"difficulty":{1:"ax+b=cx",2:"ax+b=cx+d",3:"fractions in answer"}}
    self.id = "VariableOnBothSidesEquationWorksheet"
    self.subSkill = "Solve equations with variables on both sides"
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

class DistributeEquationWorksheet(SolvingLinearEquations):
  def __init__(self, difficulty=1):
    super().__init__()
    self.kwargs = {"difficulty":[1,2,3]}
    self.toolTips = {"difficulty": {1:"a(bx+c)=d", 2:"a(bx+c)=dx", 3:"a(bx+c)=d(ex+f)"}}
    self.subSkill = "Use the Distributive Property"
    self.id = "DistributeEquationWorksheet"
    """
    a(bx+c) = d diff1 -> abx + ac = d -> (d-ac)/(ab) = ans
    a(bx+c) = dx diff2 -> abx + ac = dx -> (ab-d)x = ac -> ac/(ab-d) = ans
    a(bx+c) = d(ex+f) diff3 -> abx + ac = dex + df -> (ab-de)x = (df-ac) -> (df-ac)/(ab-de) = ans
    """
    #x+a=b
    var = random.choice([letter for letter in string.ascii_lowercase if letter not in ["o","b","f","a","q","t","u","v","i","l","c"]])

    ans = random.choice([num for num in range(-10,11) if num != 0])

    if difficulty == 1:
        a = random.choice([num for num in range(-10,11) if num not in [0,1]])
        b = random.choice([num for num in range(-10,11) if num not in [0]])
        c = random.choice([num for num in range(-10,11) if num not in [0]])
        d = a*(b*ans+c)
        self.worksheetQuestion = formatMathString(f"{a}({b}{var}+{c})={d}")
        self.worksheetAnswer = formatMathString(f"{var}={ans}")

    elif difficulty == 2:
        #abx+ac = dx, abx - dx = -ac, so define a,b,d,answer
        choices = []
        for ans in range(-10,11):
            for b in range(-10,11):
                for d in range(-10,11):
                    for a in range(-10,11):
                        for c in range(-10,11):
                            if b not in [0] and ans not in [0] and d not in [0] and a not in [0] and c not in [0] and a*b*ans+a*c == d*ans:
                                choices.append([a,b,d,ans,c])
        random.shuffle(choices)

        a = choices[0][0]
        b = choices[0][1]
        d = choices[0][2]
        ans = choices[0][3]
        c = choices[0][4]

        #product of abx-dx must equal -ac
        product = a*b*ans - d*ans
        c = int(product/-a)
        
        self.worksheetQuestion = formatMathString(f"{a}({b}{var}+{c})={d}{var}")
        self.worksheetAnswer = formatMathString(f"{var}={ans}")

    elif difficulty == 3:
        #a(bx+c) = d(ex+f)
        a = random.choice([a for a in range(-10,11) if a not in [0,1]])
        b = random.choice([a for a in range(-10,11) if a not in [0]])
        c = random.choice([a for a in range(-10,11) if a not in [0]])
        d = random.choice([a for a in range(-10,11) if a not in [0,1]])
        e = random.choice([e for e in range(-20,21) if a not in [0] and a*b - d*e != 0])
        f = random.choice([f for f in range(-20,21) if a not in [0] and d*f - a*c != 0])

        #get x from this -> abx + ac = dex + df -> abx-dex = df-ac -> df-ac/ab-de
        ansNum = d*f-a*c
        ansDenom = a*b-d*e
        if ansNum % ansDenom == 0:
            self.worksheetAnswer = formatMathString(f"{var}={int(ansNum/ansDenom)}")
        else:

            if ansNum < 0 and ansDenom < 0:
                co = 1
            elif ansNum > 0 and ansDenom > 0:
                co = 1
            else:
                co = -1
            self.worksheetAnswer = formatMathString(fr"{var}=\frac{{{co*abs(ansNum)}}}{{{abs(ansDenom)}}}")
        self.worksheetQuestion = formatMathString(f"{a}({b}{var}+{c})={d}({e}{var}+{f})")
