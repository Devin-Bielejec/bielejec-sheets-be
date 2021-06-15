import sys
from fractions import gcd, Fraction
sys.path.insert(0, "F:/code/bielejec-sheets-be/creatingWorksheets/utils")
from equations import formatMathString, toLatexFraction, randomBetweenNot
import math



class Solving():
    #Initialize class with info to store in database, then we can dyamically add it to the database
    def __init__(self):
        #ID is topic + MAIN SKILL
        self.subject = "Algebra"
        self.standards = []
        self.state = "New York"
        self.topics = ["Solving Equations"]
        self.worksheetAnswer = None
        self.solution = None

        self.instructions = "Solve:"

        """
        What if we keep track of pieces we need, then a different function actually adds it to the document

        For example:

        self.instructions #for worksheets
        self.worksheetQuestion
        self.worksheetAnswer

        self.assessmentData = [strings, graphs, tables, multipleChoice]
        Then we loop through assessment data, if it's a string we type it and return afterwards
        if graph we make it do graph things
        if table same thing
        if multiple choice


        maybe put doc related functions in here that pertain pretty much to all within here - might be a nice clean way to do this
        """

"""
1 step equations
subtract#
add#
divide#
multiply#

ax=b
x+a=b
x-a=b
x/a=b


2 step equations
add/subtract# divide/multiply
ax+b=c
ax-b=c
x/a+b=c
x/a-b=c
diff 2, negative numbers/fractions
diff 3, change order (b +ax etc)

x on both sides equations
# on both sides equations
ax+b=cx diff1
ax+b=cx+d diff2
diff3 fraction and negative numbers

a(bx+c) = d
a(bx+c) = dx
a(bx+c) = d(ex+f)

"""

import string
import random

class OneStepEquation():
  def __init__(self, firstStep="add", difficulty=1):
    self.kwargs = {"firstStep": ["add","subtract", "multiply", "divide"], "difficulty":[1,2,3]}
    self.skills = ["Solve 1-step Equations"]
    self.id = "OneStepEquation"
    
    #x+a=b
    var = random.choice([letter for letter in string.ascii_lowercase if letter not in ["o","b","f","a","q","t","u","v","i","l","c"]])
    
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
        choices = [formatMathString(f"{b-a}"),formatMathString(f"{b+a}"),formatMathString(f"{b*a}"),formatMathString(fr"\frac{{{b}}}{{{a}}}")]
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
        choices = [ormatMathString(f"{b+a}"),formatMathString(f"{b-a}"),formatMathString(f"{b*a}"),formatMathString(fr"\frac{{{b}}}{{{a}}}")]

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
        choices = [formatMathString(f"{b*a}"),formatMathString(f"{b+a}"),formatMathString(f"{b-a}"),formatMathString(fr"\frac{{{b}}}{{{a}}}")]

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
        choices = [formatMathString(fr"\frac{{{ansNum}}}{{{ansDenom}}}"),formatMathString(f"{var}={b+a}"),formatMathString(f"{var}={b*a}"),formatMathString(f"{var}={b-a}")]

        self.worksheetQuestion = formatMathString(f"{a}{var}={b}")

    self.assessmentData = [{"text": True, "data": f"What is the solution to ${self.worksheetQuestion}"}, {"multipleChoice": True, "data": choices}]
    self.answer = self.worksheetAnswer

class TwoStepEquation():
  def __init__(self, firstStep="add", secondStep="multiply", difficulty=1):
    self.kwargs = {"firstStep":["add","subtract"], "secondStep":["multiply", "divide"], "difficulty":[1,2,3]}
    self.skills = ["Solve 1-step Equations"]
    self.id = "OneStepEquation"
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
        choices = [f"{ans}", f"{toLatexFraction(c+b,a)}", f"{(c-b)*a}", f"{(c+b)*a}" ]

    elif secondStep == "multiply":
        if difficulty == 1:
            print(ans)
            a = random.choice([num for num in range(-10,11) if num not in [-1,0,1] and ans % num == 0])
        else:
            a = random.choice([num for num in range(-10,-1) if ans % num == 0])
        c = int(ans/a)+b
        if difficulty == 3:
            self.worksheetQuestion = formatMathString(fr"{b}+\frac{{{var}}}{{{a}}}={c}")
        else:
            self.worksheetQuestion = formatMathString(fr"\frac{{{var}}}{{{a}}}+{b}={c}")
        choices = [f"{ans}", f"{toLatexFraction(c-b,a)}", f"{toLatexFraction(c+b,a)}", f"{(c+b)*a}" ]

    self.answer = self.worksheetAnswer
    self.assessmentData = [
        {"text": True, "data": f"What is the solution to {self.worksheetAnswer}?"}, {"multipleChoice": True, "data": choices}
    ]

class VariableOnBothSidesEquation():
  def __init__(self, difficulty=1):
    self.kwargs = {"difficulty":[1,2,3]}
    self.skills = ["Solve Equations with the variable on both sides"]
    self.id = "VariableOnBothSidesEquation"
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
        choices = [formatMathString(f"{ans}"), f"{toLatexFraction(b,a-c)}", f"{toLatexFraction(c-b,a)}", f"{-ans}"]
    elif difficulty == 2:
        a = random.choice([num for num in range(-10,11) if num not in [0]])
        c = random.choice([num for num in range(-10,11) if a-num not in [-1,0,1] and num not in [0]])
        bdDifference = ans*(a-c)
        b = random.choice([num for num in range(-10,11) if num not in [0,-bdDifference]])
        d = bdDifference + b
        self.worksheetQuestion = formatMathString(f"{a}{var}+{b}={c}{var}+{d}")
        self.worksheetAnswer = formatMathString(fr"{var}={ans}")
        choices = [formatMathString(f"{ans}"), f"{toLatexFraction(d+b,a-c)}", f"{toLatexFraction(d-b,a+c)}", f"{-ans}"]
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
        choices = [formatMathString(fr"\frac{{{ansNum}}}{{{ansDenom}}}"), f"{toLatexFraction(ansDenom, ansNum)}", f"{toLatexFraction(d-b,a+c)}", f"{toLatexFraction(d+b,a-c)}"]

    self.assessmentData = [{"text": True, "data": f"What are the solutions to {self.worksheetQuestion}?"}, {"multipleChoice": True, "data": choices}]

    self.answer = self.worksheetAnswer

class DistributeEquation():
  def __init__(self, difficulty=1):
    self.kwargs = {"difficulty":[1,2,3]}
    self.skills = ["Solve Equations with the variable on both sides"]
    self.id = "VariableOnBothSidesEquation"
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
        choices = [formatMathString(f"{ans}"), f"{(d-a*c)*a*b}", f"{toLatexFraction(d-c,a*b)}", f"{-ans}"]
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
        print(choices)
        a = choices[0][0]
        b = choices[0][1]
        d = choices[0][2]
        ans = choices[0][3]
        c = choices[0][4]

        #product of abx-dx must equal -ac
        product = a*b*ans - d*ans
        c = int(product/-a)
        
        self.worksheetQuestion = formatMathString(f"{a}({b}{var}+{c})={d}{var}")
        choices = [formatMathString(f"{ans}"), f"{(d-a*c)*a*b}", f"{toLatexFraction(d-c,a*b)}", f"{-ans}"]
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
        choices = [formatMathString(f"{ans}"), f"{(d*f-a*c)*(a*b-d*e)}", f"{toLatexFraction(d*f-a*c,a*b+d*e)}", f"{-ans}"]

    self.answer = self.worksheetAnswer
    self.assessmentData = [{"text": True, "data": f"What are the solutions to {self.worksheetQuestion}?"}, {"multipleChoice": True, "data": choices}]

class FractionEquation():
  def __init__(self, difficulty=1):
    self.kwargs = {"difficulty":[1,2,3]}
    self.skills = ["Solve Equations with 2 or more fractions"]
    self.id = "FractionEquation"
    """
    diff1 - two fractions
    diff2 - three fraction int answer
    diff3 - three fractions fractional answer
    """
    #x+a=b
    var = "x"

    if difficulty == 1:
        correct = False
        while not correct:
            p1 = random.choice([num for num in range(2,10) if num not in [0]])
            p2 = random.choice([num for num in range(2,10) if num not in [0,p1,-p1]])
            p3 = 1

            product = p1*p2*p3

            #ax + b = c
            a = random.choice([num for num in range(-20,21) if num != 0 and num % p1 != 0])
            b = random.choice([num for num in range(-20,21) if num != 0 and num % p2 != 0])
            c = random.choice([num*p3 for num in range(-10,10) if num not in [0]])

            #ax/product + b/product = c/product

            aFrac = Fraction(a,p1)
            bFrac = Fraction(b,p2)
            cFrac = Fraction(c,p3)
            #a/p1 x + b/p2 = c/p3
            #p2p3a x + p1p3b = p1p2c
            #(p1p2c-p1p3b)/(p2p3a)

            ansFrac = Fraction(p1*p2*c-p1*p3*b,p2*p3*a)
            ansDeno = ansFrac.denominator

            if ansDeno == 1 and bFrac.denominator != aFrac.denominator:
                correct = True

        self.worksheetQuestion = formatMathString(f"{toLatexFraction(aFrac.numerator, aFrac.denominator)}{var}+{toLatexFraction(bFrac.numerator, bFrac.denominator)}={cFrac.numerator}")
        self.answer = formatMathString(f"{ansFrac.numerator}")
        # choices = [formatMathString(f"{ans}"), f"{(d-a*c)*a*b}", f"{toLatexFraction(d-c,a*b)}", f"{-ans}"]
        self.worksheetAnswer = formatMathString(f"{var}={ansFrac.numerator}")

    elif difficulty == 2:
        denominatorsOne = False
        while not denominatorsOne:
            p1 = random.choice([num for num in range(2,10) if num not in [0]])
            p2 = random.choice([num for num in range(2,10) if num not in [0,p1]])
            p3 = random.choice([num for num in range(2,10) if num not in [0,p1,p2]])

            product = p1*p2*p3

            a = random.choice([num for num in range(-20,21) if num not in [0] and num % p1 != 0])
            b = random.choice([num for num in range(-20,21) if num != 0 and num % p2 != 0])
            c = random.choice([num for num in range(-20,21) if num != 0 and num % p3 != 0])

            #ax/product + b/product = c/product

            aFrac = Fraction(a,p1)
            bFrac = Fraction(b,p2)
            cFrac = Fraction(c,p3)
            #a/p1 x + b/p2 = c/p3
            #p2p3a x + p1p3b = p1p2c
            #(p1p2c-p1p3b)/(p2p3a)

            ansFrac = Fraction(p1*p2*c-p1*p3*b,p2*p3*a)
            ansDeno = ansFrac.denominator
            aDeno = aFrac.denominator
            bDeno = bFrac.denominator
            cDeno = cFrac.denominator
            print(ansDeno, aDeno, bDeno, cDeno)
            if aDeno != 1 and bDeno != 1 and cDeno != 1 and ansDeno == 1:
                denominatorsOne = True

        self.worksheetQuestion = formatMathString(f"{toLatexFraction(aFrac.numerator, aFrac.denominator)}{var}+{toLatexFraction(bFrac.numerator, bFrac.denominator)}={toLatexFraction(cFrac.numerator, cFrac.denominator)}")
        self.answer = formatMathString(f"{ansFrac.numerator}")
        # choices = [formatMathString(f"{ans}"), f"{(d-a*c)*a*b}", f"{toLatexFraction(d-c,a*b)}", f"{-ans}"]
        self.worksheetAnswer = formatMathString(f"{var}={ansFrac.numerator}")

    elif difficulty == 3:
        denominatorsOne = False
        while not denominatorsOne:
            p1 = random.choice([num for num in range(2,10) if num not in [0]])
            p2 = random.choice([num for num in range(2,10) if num not in [0,p1]])
            p3 = random.choice([num for num in range(2,10) if num not in [0,p1,p2]])

            product = p1*p2*p3

            a = random.choice([num for num in range(-20,21) if num not in [0] and num % p1 != 0])
            b = random.choice([num for num in range(-20,21) if num != 0 and num % p2 != 0])
            c = random.choice([num for num in range(-20,21) if num != 0 and num % p3 != 0])

            #ax/product + b/product = c/product

            aFrac = Fraction(a,p1)
            bFrac = Fraction(b,p2)
            cFrac = Fraction(c,p3)
            #aN/aD x + bN/bD = cN/cD
            #aNbDcD x + bNaDcD = cNaDbN
            #

            ansFracN = cFrac.numerator * aFrac.denominator * bFrac.denominator - bFrac.numerator * aFrac.denominator * cFrac.denominator
            ansFracD = aFrac.numerator * bFrac.denominator * cFrac.denominator
            ansFrac = Fraction(ansFracN,ansFracD)
            ansDeno = ansFrac.denominator
            aDeno = aFrac.denominator
            bDeno = bFrac.denominator
            cDeno = cFrac.denominator
            print(ansDeno, aDeno, bDeno, cDeno)
            #Denominator makes it a fraction
            if aDeno != 1 and bDeno != 1 and cDeno != 1 and ansDeno != 1:
                denominatorsOne = True

        #Change order of x in first or second spotq
        order = random.randint(1,2)
        if order == 1:
            self.worksheetQuestion = formatMathString(f"{toLatexFraction(aFrac.numerator, aFrac.denominator)}{var}+{toLatexFraction(bFrac.numerator, bFrac.denominator)}={toLatexFraction(cFrac.numerator, cFrac.denominator)}")
        else:
            self.worksheetQuestion = formatMathString(f"{toLatexFraction(bFrac.numerator, bFrac.denominator)}+{toLatexFraction(aFrac.numerator, aFrac.denominator)}{var}={toLatexFraction(cFrac.numerator, cFrac.denominator)}")
        self.answer = formatMathString(f"{toLatexFraction(ansFracN, ansFracD, simplified=False)}={toLatexFraction(ansFracN,ansFracD)}")
        # choices = [formatMathString(f"{ans}"), f"{(d-a*c)*a*b}", f"{toLatexFraction(d-c,a*b)}", f"{-ans}"]
        self.worksheetAnswer = formatMathString(f"{var}={toLatexFraction(ansFracN,ansFracD, simplified=False)}={toLatexFraction(ansFracN, ansFracD)}")

    self.answer = self.worksheetAnswer
    # self.assessmentData = [{"text": True, "data": f"What are the solutions to {self.worksheetQuestion}?"}, {"multipleChoice": True, "data": choices}]

class LikeTermsEquation():
  def __init__(self, difficulty=1, termToCombine=1):
    #1 is var, 2 is num
    self.kwargs = {"difficulty": [1,2,3], "termToCombine": [1,2]}
    var = "x"

    if difficulty == 1:
      if termToCombine == 1:
        #We'll combine the x's
        #ax + bx = c
        x = randomBetweenNot(-10,10,[0])
        a = randomBetweenNot(-10,10,[0])
        b = randomBetweenNot(-10,10,[0,-a])
        c = a*x + b*x

        self.worksheetQuestion = formatMathString(f"{a}{var}+{b}{var}={c}")
        self.worksheetAnswer = formatMathString(f"{var}={x}")
      else:
        #We'll combine the number
        #a + b = cx
        x = randomBetweenNot(-10,10,[0])
        c = randomBetweenNot(-10,10,[0])
        b = randomBetweenNot(-10,10,[0])
        a = c*x - b

        self.worksheetQuestion = formatMathString(f"{a}+{b}={c}{var}")
        self.worksheetAnswer = formatMathString(f"{var}={x}")
    elif difficulty == 2:
      if termToCombine == 1:
        #ax+bx+c=dx+ex
        #(a+b-d-e)x = -c
        x = randomBetweenNot(-10,10,[0])
        a = randomBetweenNot(-10,10,[0])
        b = randomBetweenNot(-10,10,[0])
        
        d = randomBetweenNot(-10,10,[0])
        e = randomBetweenNot(-10,10,[0,(a+b-d)])
        
        c = (a+b-d-e)*x*-1
        
        self.worksheetQuestion = formatMathString(f"{a}{var}+{b}{var}+{c}={d}{var}+{e}{var}")
        self.worksheetAnswer = formatMathString(f"{var}={x}")
      else:
        #a+b+cx=d+e+fx
        #(a+b-d-e) = (-c+f)x
        x = randomBetweenNot(-10,10,[0])
        f = randomBetweenNot(-10,10,[0])
        c = randomBetweenNot(-10,10,[0,f])
        
        d = randomBetweenNot(-10,10,[0])
        e = randomBetweenNot(-10,10,[0])
        a = randomBetweenNot(-10,10,[0])
        b = (-c+f)*x - a + d + e

        c = (a+b-d-e)*x*-1
        
        self.worksheetQuestion = formatMathString(f"{a}+{b}+{c}{var}={d}+{e}+{f}{x}")
        self.worksheetAnswer = formatMathString(f"{var}={x}")        
    else:
      #distribute twice on one side
      #a(bx+c)+d(ex+f)=g
      x = randomBetweenNot(-10,10,[0])
      a = randomBetweenNot(-10,10,[0,1])
      b = randomBetweenNot(-10,10,[0])
      c = randomBetweenNot(-10,10,[0])
      
      d = randomBetweenNot(-10,10,[0,1])
      e = randomBetweenNot(-10,10,[0])
      f = randomBetweenNot(-10,10,[0])
      
      g = a*(b*x+c) + d*(e*x+f)
      
      self.worksheetQuestion = formatMathString(f"{a}({b}{var}+{c})+{d}({e}{var}+{f})={g}")
      self.worksheetAnswer = formatMathString(f"{var}={x}")
    self.answer = self.worksheetAnswer

solvingEquationsQuestionsDict = {"OneStepEquation": OneStepEquation, "TwoStepEquation": TwoStepEquation, "VariableOnBothSidesEquation": VariableOnBothSidesEquation, "DistributeEquation": DistributeEquation, "FractionEquation":FractionEquation, "LikeTermsEquation": LikeTermsEquation}