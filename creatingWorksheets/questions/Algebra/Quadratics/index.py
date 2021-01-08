import sys
sys.path.insert(0, "F:/code/bielejec-sheets-be/creatingWorksheets/utils")
from equations import formatMathString, toLatexFraction
import math, fractions, string, random


def getPrimes(upperRange):
  lowerRange = 2

  primes = []

  for num in range(lowerRange,upperRange + 1):  
    if num > 1:  
        for i in range(2,num):  
            if (num % i) == 0:  
                break  
        else:  
            primes.append(num)

  return primes  

def notDivisibleByPerfectSquareList(upperRange):
    squares = [x**2 for x in range(2, upperRange+1)]
    results = []
    for item in range(2, upperRange+1):
      foundSquare = True
      for square in squares:
        if item % square == 0:
          foundSquare = False
      
      if foundSquare:
        results.append(item)

    return results

def getFactorPairs(num):
  factorPairs = []
  for item in range(1,abs(num)+1):
    if num % item == 0:    
      factorPairs.append([item, num//item])


  return factorPairs

class Quadratics():
    #Initialize class with info to store in database, then we can dyamically add it to the database
    def __init__(self):
        #ID is topic + MAIN SKILL
        self.subject = "Algebra"
        self.standards = ["A.REI.B.4"]
        self.state = "New York"
        self.topics = ["Quadratics"]
        self.answer = None
        self.solution = None

        self.instructions = "Solve the quadratic equation"

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

   
#166
class June14Q8(Quadratics):
    #Initialize class with info to store in database, then we can dyamically add it to the database
    def __init__(self):
        super().__init__()
        #ID is topic + MAIN SKILL
        self.exam = "June2014"
        self.questionNumber = 8
        self.type = "MC"

        #This can get convoluted, so maybe don't worry about it so much right now
        self.skills = ["Complete the square"]

        #Junk here where you add to the document
        """
        Which equation has the same solution as x^2 + bx + c = 0?
        (1) (x + d)^2 = e
        (2) (x - d)^2 = e
        (3) (x + d)^2 = abs(-c - (b/2)^2)
        (4) (x - d)^2 = abs(-c - (b/2)^2)
        """

        #Start with correct answer
        #(x + d)^2 = e

        d = random.choice([x for x in range(-9,10) if x != 0])
        e = random.choice(getPrimes(50))

        #bx + c
        b = d*2
        c = -e + d**2

        self.worksheetQuestion = formatMathString(f"x^2+{b}x+{c}=0")
        self.worksheetAnswer = formatMathString(f"x=-{d}\pm\sqrt{e}")

        choice1 = formatMathString(f"(x+{d})^2={e}")
        choice2 = formatMathString(f"(x+{-d})^2={e}")
        choice3 = formatMathString(f"(x+{d})^2={abs(int(-c-(b/2)**2))}")
        choice4 = formatMathString(f"(x+{-d})^2={abs(int(-c-(b/2)**2))}")

        choices = [choice1, choice2, choice3, choice4]

        self.assessmentData = [{
            "text": True,
            "data": f"Which equation has the same solution as {self.worksheetQuestion}"
        }, {
            "multipleChoice": True,
            "data": choices
        }]

        self.answer = choice1

#167
class Jan15Q03(Quadratics):
    #Initialize class with info to store in database, then we can dyamically add it to the database
    def __init__(self):
        super().__init__()
        #ID is topic + MAIN SKILL
        self.exam = "Jan2015"
        self.questionNumber = 3
        self.type = "MC"

        #This can get convoluted, so maybe don't worry about it so much right now
        self.skills = ["Factor a trinomial with a > 1"]

        #(dx+e)(x+f)=0

        d = random.randint(2,3)
        prime = random.choice(getPrimes(15))

        efChoices =[[-1*prime,1], [prime, -1], [1,prime], [-1,prime]]
        eChosen = random.choice(efChoices)

        e = eChosen[0]
        f = eChosen[1]

        a = d
        b = d*f + e
        c = e*f

        c1 = formatMathString(f"({d}x+{e})(x+{f})=0")
        c2 = formatMathString(f"({d}x+{f})(x+{e})=0")
        c3 = formatMathString(f"({d}x+{-f})(x+{-e})=0")
        c4 = formatMathString(f"({d}x+{-e})(x+{-f})=0")

        self.worksheetQuestion = formatMathString(f"{a}x^2+{b}x+{c}=0")
        self.worksheetAnswer = formatMathString(f"x={-f} and x={toLatexFraction(-e, d)}")

        choices = [c1, c2, c3, c4]

        self.assessmentData = [{
            "text": True,
            "data": f"Which equation has the same solutions as {self.worksheetQuestion}"
        }, {
            "multipleChoice": True,
            "data": choices
        }]

        self.answer = choice1

#168
class Jan15Q17(Quadratics):
    #Initialize class with info to store in database, then we can dyamically add it to the database
    def __init__(self):
        super().__init__()
        #ID is topic + MAIN SKILL
        self.exam = "Jan2015"
        self.questionNumber = 17
        self.type = "MC"

        #This can get convoluted, so maybe don't worry about it so much right now
        self.skills = ["Complete the square"]

        #Junk here where you add to the document
        """
        Which equation has the same solution as x^2 + bx + c = 0?
        (1) (x + d)^2 = e
        (2) (x - d)^2 = e
        (3) (x + d)^2 = abs(-c - (b/2)^2)
        (4) (x - d)^2 = abs(-c - (b/2)^2)
        """

        #Start with correct answer
        #(x + d)^2 = e

        d = random.choice([x for x in range(-9,10) if x != 0])
        e = random.choice([x**2 for x in range(1,12)])

        #bx + c
        b = d*2
        c = -e + d**2

        self.worksheetQuestion = formatMathString(f"x^2+{b}x+{c}=0")
        self.worksheetAnswer = formatMathString(f"x={e**(1/2)-d} and x={-e**(1/2)-d}")

        choice1 = formatMathString(f"(x+{d})^2={e}")
        choice2 = formatMathString(f"(x+{-d})^2={e}")
        choice3 = formatMathString(f"(x+{d})^2={abs(int(-c-(b/2)**2))}")
        choice4 = formatMathString(f"(x+{-d})^2={abs(int(-c-(b/2)**2))}")

        choices = [choice1, choice2, choice3, choice4]

        self.assessmentData = [{
            "text": True,
            "data": f"Which equation has the same solution as {self.worksheetQuestion}"
        }, {
            "multipleChoice": True,
            "data": choices
        }]

        self.answer = choice1

#169
class Jan16Q14(Quadratics):
    #Initialize class with info to store in database, then we can dyamically add it to the database
    def __init__(self):
        super().__init__()
        #ID is topic + MAIN SKILL
        self.exam = "Jan2016"
        self.questionNumber = 14
        self.type = "MC"

        #This can get convoluted, so maybe don't worry about it so much right now
        self.skills = ["Complete the square"]

        #Junk here where you add to the document
        """
        When solving the equation x^2 + bx + c = 0 by completing the sqaure, which equation is a step in the process?
        (1) (x + d)^2 = e
        (2) (x - d)^2 = e
        (3) (x + d)^2 = abs(-c - (b/2)^2)
        (4) (x - d)^2 = abs(-c - (b/2)^2)
        """

        #Start with correct answer
        #(x + d)^2 = e

        d = random.choice([x for x in range(-9,10) if x != 0])
        e = random.choice(getPrimes(50))

        #bx + c
        b = d*2
        c = -e + d**2

        self.worksheetQuestion = formatMathString(f"x^2+{b}x+{c}=0")
        self.worksheetAnswer = formatMathString(f"x=-{d}\pm\sqrt{{{e}}}")

        choice1 = formatMathString(f"(x+{d})^2={e}")
        choice2 = formatMathString(f"(x+{-d})^2={e}")
        choice3 = formatMathString(f"(x+{d})^2={abs(int(-c-(b/2)**2))}")
        choice4 = formatMathString(f"(x+{-d})^2={abs(int(-c-(b/2)**2))}")

        choices = [choice1, choice2, choice3, choice4]

        self.assessmentData = [{
            "text": True,
            "data": f"When solving the equation {self.worksheetQuestion} by completing the square, which equation is a step in the process?"
        }, {
            "multipleChoice": True,
            "data": choices
        }]

        self.answer = choice1

#170
class Jan17Q22(Quadratics):
    #Initialize class with info to store in database, then we can dyamically add it to the database
    def __init__(self):
        super().__init__()
        #ID is topic + MAIN SKILL
        self.exam = "Jan2017"
        self.questionNumber = 22
        self.type = "MC"

        #This can get convoluted, so maybe don't worry about it so much right now
        self.skills = ["Complete the square"]

        #Junk here where you add to the document
        """
        The method of completing the squre was used to solve the equation x^2 + bx + c = 0. Which equation is a correct step when using this method?
        (1) (x + d)^2 = e
        (2) (x + d)^2 = -e
        (3) (x + d)^2 = -c + d^2
        (4) (x + d)^2 = -(-c+d^2)
        """

        gcf = random.randint(2,5)

        #(x+d)^2 = e

        d = random.choice([x for x in range(-9,10) if x != 0])
        e = random.choice([x for x in notDivisibleByPerfectSquareList(20) if x != 0 or x != d or x != -d])

        a = gcf
        b = gcf*2*d
        c = gcf*(d**2-e)

        self.worksheetQuestion = formatMathString(f"{a}x^2+{b}x+{c}=0")
        self.worksheetAnswer = formatMathString(f"x=-{d}\pm\sqrt{{{e}}}")

        choice1 = formatMathString(f"(x+{d})^2={e}")
        choice2 = formatMathString(f"(x+{-d})^2={-e}")
        choice3 = formatMathString(f"(x+{d})^2={-c+d**2}")
        choice4 = formatMathString(f"(x+{-d})^2={-1*(-c+d**2)}")

        choices = [choice1, choice2, choice3, choice4]

        self.assessmentData = [{
            "text": True,
            "data": f"The method of completing the square was used to solve the equation {self.worksheetQuestion}. Which equation is a correct step when using this method?"
        }, {
            "multipleChoice": True,
            "data": choices
        }]

        self.answer = choice1


#171
class Jan19Q15(Quadratics):
    #Initialize class with info to store in database, then we can dyamically add it to the database
    def __init__(self):
        super().__init__()
        #ID is topic + MAIN SKILL
        self.exam = "Jan2019"
        self.questionNumber = 15
        self.type = "MC"

        #This can get convoluted, so maybe don't worry about it so much right now
        self.skills = ["Complete the square"]

        #Junk here where you add to the document
        """
        Which equation has the same solution as x^2 + bx + c = 0?
        (1) (x + d)^2 = e
        (2) (x - d)^2 = e
        (3) (x + d)^2 = abs(-c - (b/2)^2)
        (4) (x - d)^2 = abs(-c - (b/2)^2)
        """

        #Start with correct answer
        #(x + d)^2 = e

        d = random.choice([x for x in range(-9,10) if x != 0])
        e = random.choice([x**2 for x in range(1,12)])

        #bx + c
        b = d*2
        c = -e + d**2

        self.worksheetQuestion = formatMathString(f"x^2+{b}x+{c}=0")
        self.worksheetAnswer = formatMathString(f"x={e**(1/2)-d}") + " and " + formatMathString(f"x={-e**(1/2)-d}")

        choice1 = formatMathString(f"(x+{d})^2={e}")
        choice2 = formatMathString(f"(x+{-d})^2={e}")
        choice3 = formatMathString(f"(x+{d})^2={abs(int(-c-(b/2)**2))}")
        choice4 = formatMathString(f"(x+{-d})^2={abs(int(-c-(b/2)**2))}")

        choices = [choice1, choice2, choice3, choice4]

        self.assessmentData = [{
            "text": True,
            "data": f"Which equation has the same solution as {self.worksheetQuestion}"
        }, {
            "multipleChoice": True,
            "data": choices
        }]

        self.answer = choice1

#172 - skipped not regents question
#173
class June14Q10(Quadratics):
    #Initialize class with info to store in database, then we can dyamically add it to the database
    def __init__(self):
        super().__init__()
        #ID is topic + MAIN SKILL
        self.exam = "June2014"
        self.questionNumber = 10
        self.type = "MC"

        #This can get convoluted, so maybe don't worry about it so much right now
        self.skills = ["Complete the square"]

        #Start with correct answer
        # x^2 - 2dx + (d^2 - e^2f) = 0
        # x^2 - 2dx + d^2 = e^2 f
        # (x-d)^2 = e^2 f
        #x - d = e sqrt(f)
        #x = d +- e sqrt(f)

        d = random.choice([x for x in range(-10,11) if x != 0])
        b = -d*2

        #choose e and f such that c will be less than 100
        efChoices = []
        for e in range(1,11):
            for f in notDivisibleByPerfectSquareList(50):
                if -100 <= d**2-e**2*f <= 100 and d**2-e**2*f != 0:
                    efChoices.append([e,f])

        random.shuffle(efChoices)
        e = efChoices[0][0]
        f = efChoices[0][1]

        #bx + c
        a = 1

        c = d**2-e**2*f

        self.worksheetQuestion = formatMathString(f"{a}x^2+{b}x+{c}=0")
        self.worksheetAnswer = formatMathString(f"x={d}\pm{e}\sqrt{f}")

        choice1 = formatMathString(f"x={d}\pm{e}\sqrt{f}")
        choice2 = formatMathString(f"x={-d}\pm{e}\sqrt{f}")
        choice3 = formatMathString(f"x={d}\pm{2*e}\sqrt{f}")
        choice4 = formatMathString(f"x={-d}\pm{2*e}\sqrt{f}")

        choices = [choice1, choice2, choice3, choice4]

        self.assessmentData = [{
            "text": True,
            "data": f"What are the roots of the equation {self.worksheetQuestion}?"
        }, {
            "multipleChoice": True,
            "data": choices
        }]

        self.answer = choice1

#174
class Aug14Q03(Quadratics):
    #Initialize class with info to store in database, then we can dyamically add it to the database
    def __init__(self):
        super().__init__()
        #ID is topic + MAIN SKILL
        self.exam = "Aug2014"
        self.questionNumber = 3
        self.type = "MC"

        #This can get convoluted, so maybe don't worry about it so much right now
        self.skills = ["Take square roots"]

        #ax^2 + b = 0
        #a(x+c)(x-c)=0

        a = random.randint(2,5)
        c = random.randint(2,10)

        b = -1*(c)**2*a
        
        self.worksheetQuestion = formatMathString(f"{a}x^2+{b}=0")
        self.worksheetAnswer = formatMathString(f"x={-c}") + " and " + formatMathString(f"x={c}")

        choice1 = formatMathString(f"{c}") + " and " + formatMathString(f"{-c}")
        choice2 = formatMathString(f"{-(c)**2}") + " and " + formatMathString(f"{c**2}")
        choice3 = formatMathString(f"{-(c)**2}") + ", only"
        choice4 = formatMathString(f"{-c}") + ", only"

        choices = [choice1, choice2, choice3, choice4]

        self.assessmentData = [{
            "text": True,
            "data": f"If {self.worksheetQuestion}, the roots of the equation are"
        }, {
            "multipleChoice": True,
            "data": choices
        }]

        self.answer = choice1

#175
class June15Q23(Quadratics):
    #Initialize class with info to store in database, then we can dyamically add it to the database
    def __init__(self):
        super().__init__()
        #ID is topic + MAIN SKILL
        self.exam = "June2015"
        self.questionNumber = 23
        self.type = "MC"

        #This can get convoluted, so maybe don't worry about it so much right now
        self.skills = ["Complete the square"]

        #d +- e sqrt(f)

        d = random.choice([x for x in range(-5,6) if x != 0])
        e = random.choice([x for x in range(-6,7) if x != 0])
        f = random.choice(notDivisibleByPerfectSquareList(50))

        a = 1
        b = -d*2
        c = (4*e**2*f-b**2)//(-4*a)

        newC = -c
        discriminant = b**2 - 4*a*c

        pSquares = [x**2 for x in range(1,round(discriminant**(1/2))+1)]
        pSquares.reverse()
        chosenPS = 1
        for ps in pSquares:
            if discriminant % ps == 0:
                chosenPS = ps
                break

        newF = discriminant//chosenPS
        newE = int(chosenPS**(1/2)/2)
        
        self.worksheetQuestion = formatMathString(f"{a}x^2+{b}x={-c}")
        self.worksheetAnswer = formatMathString(f"x={d}\pm{e}\sqrt{f}")

        choice1 = formatMathString(f"x={d}\pm{e}\sqrt{f}")
        choice2 = formatMathString(f"x={-d}\pm{e}\sqrt{f}")
        choice3 = formatMathString(f"x={d}\pm{newE}\sqrt{newF}")
        choice4 = formatMathString(f"x={-d}\pm{newE}\sqrt{newF}")

        choices = [choice1, choice2, choice3, choice4]

        self.assessmentData = [{
            "text": True,
            "data": f"What are the solutions to the equation {self.worksheetQuestion}?"
        }, {
            "multipleChoice": True,
            "data": choices
        }]

        self.answer = choice1

#176
class Aug15Q23(Quadratics):
    #Initialize class with info to store in database, then we can dyamically add it to the database
    def __init__(self):
        super().__init__()
        #ID is topic + MAIN SKILL
        self.exam = "Aug2015"
        self.questionNumber = 23
        self.type = "MC"

        #This can get convoluted, so maybe don't worry about it so much right now
        self.skills = ["Take square roots"]

        #(x+a)^2 = b

        a = random.choice([x for x in notDivisibleByPerfectSquareList(25) if x != 0])
        b = random.choice([x for x in notDivisibleByPerfectSquareList(25) if x != a and x != -a])
        
        self.worksheetQuestion = formatMathString(f"(x+{a})^2={b}")
        self.worksheetAnswer = formatMathString(f"x={-a}\pm\sqrt{b}")

        choice1 = formatMathString(f"x={-a}\pm\sqrt{b}")
        choice2 = formatMathString(f"x={a}\pm\sqrt{b}")
        choice3 = formatMathString(f"x={-b}\pm\sqrt{a}")
        choice4 = formatMathString(f"x={b}\pm\sqrt{a}")

        choices = [choice1, choice2, choice3, choice4]

        self.assessmentData = [{
            "text": True,
            "data": f"The solution of the equation {self.worksheetQuestion} is"
        }, {
            "multipleChoice": True,
            "data": choices
        }]

        self.answer = choice1

#177
class June16Q19(Quadratics):
    #Initialize class with info to store in database, then we can dyamically add it to the database
    def __init__(self):
        super().__init__()
        #ID is topic + MAIN SKILL
        self.exam = "June2016"
        self.questionNumber = 19
        self.type = "MC"

        #This can get convoluted, so maybe don't worry about it so much right now
        self.skills = ["Take square roots"]

        """
        x + a = +- b
        (x+a)^2 = b^2
        c(x+a)^2 = c*b^2
        c(x+a)^2 + d = c*b^2 + d
        """

        a = random.choice([x for x in range(-9,10) if x != 0])
        b = random.choice([x for x in range(-9,10) if x not in [0,a,-a]])
        c = random.randint(2,4)
        d = random.choice([x for x in range(-9,10) if x not in [0]])

        self.worksheetQuestion = formatMathString(f"{c}(x+{a})^2+{d}={c*b**2+d}")
        self.worksheetAnswer = formatMathString(f"x={b-a}") + " and " + formatMathString(f"x={-b-a}")

        choice1 = formatMathString(f"{b-a}") + " and " + formatMathString(f"{-b-a}")
        choice2 = formatMathString(f"{a-b}") + " and " + formatMathString(f"{a+b}")
        choice3 = formatMathString(f"{b-a}")
        choice4 = formatMathString(f"{a+b}")

        choices = [choice1, choice2, choice3, choice4]

        self.assessmentData = [{
            "text": True,
            "data": f"What is the solution of the equation {self.worksheetQuestion}?"
        }, {
            "multipleChoice": True,
            "data": choices
        }]

        self.answer = choice1

#178
class Aug16Q19(Quadratics):
    #Initialize class with info to store in database, then we can dyamically add it to the database
    def __init__(self):
        super().__init__()
        #ID is topic + MAIN SKILL
        self.exam = "Aug2016"
        self.questionNumber = 19
        self.type = "MC"

        #This can get convoluted, so maybe don't worry about it so much right now
        self.skills = ["Factor a trinomial with a > 1"]

        """
        (x+a/b)(x+c)=0
        """
        b = random.choice(getPrimes(5))
        a = random.choice([x for x in range(-9,10) if x != 0 and x % b != 0 and b % x != 0])
        c = random.choice([x for x in range(-9,10) if x != 0 and x % b != 0 and b % x != 0])

        #(bx+a)(x+c)=0
        #bx^2
        #bx^2 + (a+bc)x = -ac
        self.worksheetQuestion = formatMathString(f"{b}x^2+{a+b*c}x={-a*c}")
        self.worksheetAnswer = formatMathString(f"x={toLatexFraction(-a,b)}") + " and " + formatMathString(f"x={-c}")

        choice1 = formatMathString(f"{toLatexFraction(-a,b)}") + " and " + formatMathString(f"{-c}")
        choice2 = formatMathString(f"{toLatexFraction(a,b)}") + " and " + formatMathString(f"{c}")
        choice3 = formatMathString(f"{-a}") + " and " + formatMathString(f"{toLatexFraction(-c,b)}")
        choice4 = formatMathString(f"{a}") + " and " + formatMathString(f"{toLatexFraction(c,b)}")

        choices = [choice1, choice2, choice3, choice4]

        self.assessmentData = [{
            "text": True,
            "data": f"What are the solutions to the equation {self.worksheetQuestion}?"
        }, {
            "multipleChoice": True,
            "data": choices
        }]

        self.answer = choice1

#179
class Jan17Q15(Quadratics):
    #Initialize class with info to store in database, then we can dyamically add it to the database
    def __init__(self):
        super().__init__()
        #ID is topic + MAIN SKILL
        self.exam = "Jan2017"
        self.questionNumber = 15
        self.type = "MC"

        #This can get convoluted, so maybe don't worry about it so much right now
        self.skills = ["Take square roots"]

        """
        x=a/b
        x=a^2/b^2
        b^2x=a^2
        c+b^2x=a^+c
        """

        a = random.choice([x for x in range(-9,10) if x not in [-1,0,1]])
        b = random.choice([x for x in range(2,10) if x % a != 0 and a % x != 0])
        c = random.choice([x for x in range(-20,21) if x != 0])

        self.worksheetQuestion = formatMathString(f"{c}+{b**2}x^2={a**2+c}")
        self.worksheetAnswer = formatMathString(f"x={toLatexFraction(a,b)}")

        choice1 = formatMathString(f"{toLatexFraction(a,b)}")
        choice2 = formatMathString(f"{toLatexFraction(b,a)}")
        choice3 = formatMathString(f"{toLatexFraction(a**2,b**2)}")
        choice4 = formatMathString(f"{toLatexFraction(b**2,a**2)}")

        choices = [choice1, choice2, choice3, choice4]

        self.assessmentData = [{
            "text": True,
            "data": f"Which value of $x$ is a solution to the equation {self.worksheetQuestion}?"
        }, {
            "multipleChoice": True,
            "data": choices
        }]

        self.answer = choice1

#180
class Jan17Q02(Quadratics):
    #Initialize class with info to store in database, then we can dyamically add it to the database
    def __init__(self):
        super().__init__()
        #ID is topic + MAIN SKILL
        self.exam = "Jan2017"
        self.questionNumber = 2
        self.type = "MC"

        #This can get convoluted, so maybe don't worry about it so much right now
        self.skills = ["Factor trinomials with a = 1"]

        """
        (x+a)(x+var1)
        """

        a = random.choice([x for x in range(-9,10) if x not in [0]])
        var1 = random.choice([x for x in string.ascii_lowercase if x != "x"])
        b = random.choice([-1,1])

        self.worksheetQuestion = formatMathString(f"(x+{a})(x+{b}{var1})")
        self.worksheetAnswer = formatMathString(f"x={-a} and x={-b}{var1}")

        choice1 = formatMathString(f"{-a}") + " and " + formatMathString(f"{-b}{var1}")
        choice2 = formatMathString(f"{a}") + " and " + formatMathString(f"{b}{var1}")
        choice3 = formatMathString(f"{-a}") + " and " + formatMathString(f"{b}{var1}")
        choice4 = formatMathString(f"{a}") + " and " + formatMathString(f"{-b}{var1}")

        choices = [choice1, choice2, choice3, choice4]

        self.assessmentData = [{
            "text": True,
            "data": f"What is the solution set of the equation {self.worksheetQuestion}?"
        }, {
            "multipleChoice": True,
            "data": choices
        }]

        self.answer = choice1

#181
class June17Q22(Quadratics):
    #Initialize class with info to store in database, then we can dyamically add it to the database
    def __init__(self):
        super().__init__()
        #ID is topic + MAIN SKILL
        self.exam = "June2017"
        self.questionNumber = 22
        self.type = "MC"

        #This can get convoluted, so maybe don't worry about it so much right now
        self.skills = ["Complete the square"]

        """
        d +- sqrt(e)
        """ 

        d = random.choice([x for x in range(-9,10) if x not in [0]])
        b = -d*2
        a = 1

        e = random.choice([e for e in notDivisibleByPerfectSquareList(50) if abs((4*e**2-b**2)//(-4*a)) < 100])

        c = (4*e**2-b**2)//(-4*a)
        
        self.worksheetQuestion = formatMathString(f"{a}x^2+{b}x={-c}")
        self.worksheetAnswer = formatMathString(f"x={d}\pm\sqrt{e}")

        choice1 = formatMathString(f"{d}\pm\sqrt{e}")
        choice2 = formatMathString(f"{-d}\pm\sqrt{e}")
        choice3 = formatMathString(f"{d}\pm\sqrt{-c}")
        choice4 = formatMathString(f"{-d}\pm\sqrt{-c}")

        choices = [choice1, choice2, choice3, choice4]

        self.assessmentData = [{
            "text": True,
            "data": f"What are the solutions to the equation {self.worksheetQuestion}?"
        }, {
            "multipleChoice": True,
            "data": choices
        }]

        self.answer = choice1

#182
class Jan18Q14(Quadratics):
    #Initialize class with info to store in database, then we can dyamically add it to the database
    def __init__(self):
        super().__init__()
        #ID is topic + MAIN SKILL
        self.exam = "Jan2018"
        self.questionNumber = 14
        self.type = "MC"

        #This can get convoluted, so maybe don't worry about it so much right now
        self.skills = ["Take square roots"]

        """
        x+d= +- e
        (x+d)^2 = e^2
        f(x+d)^2 = fe^2
        """ 
        
        d = random.choice([x for x in range(-9,10) if x not in [0]])
        e = random.choice([x for x in range(-9,10) if x not in [0]])
        f = random.randint(2,5)
        
        self.worksheetQuestion = formatMathString(f"{f}(x+{d})^2={f*e**2}")
        self.worksheetAnswer = formatMathString(f"x={e-d} and x={-e-d}")

        choice1 = formatMathString(f"{e-d}") + " and " + formatMathString(f"{-e-d}")
        choice2 = formatMathString(f"{d-e}") + " and " + formatMathString(f"{e+d}")
        choice3 = formatMathString(f"{d}\pm\sqrt{f*e**2-f}")
        choice4 = formatMathString(f"{-d}\pm\sqrt{f*e**2-f}")

        choices = [choice1, choice2, choice3, choice4]

        self.assessmentData = [{
            "text": True,
            "data": f"What are the solutions to the equation {self.worksheetQuestion}?"
        }, {
            "multipleChoice": True,
            "data": choices
        }]

        self.answer = choice1

       
#183
class June18Q12(Quadratics):
    #Initialize class with info to store in database, then we can dyamically add it to the database
    def __init__(self):
        super().__init__()
        #ID is topic + MAIN SKILL
        self.exam = "June2018"
        self.questionNumber = 12
        self.type = "MC"

        #This can get convoluted, so maybe don't worry about it so much right now
        self.skills = ["Complete the square"]

        """
        x^2-bx=c
        x^2 + 2px + p**2 - q = 0
        (x+p)^2=q
        """ 
        
        p = random.choice([x for x in range(-10,11) if x not in [0,1,-1]])
        q = random.choice(getPrimes(50))

        b = 2*p
        c = p**2 - q

        self.worksheetQuestion = formatMathString(f"x^2+{b}x={-c}")
        self.worksheetAnswer = formatMathString(f"x={-p}\pm\sqrt{q}")

        choice1 = formatMathString(f"{p}")
        choice2 = formatMathString(f"{p**2}")
        choice3 = formatMathString(f"{-p**2}")
        choice4 = formatMathString(f"{-c}")

        choices = [choice1, choice2, choice3, choice4]

        self.assessmentData = [{
            "text": True,
            "data": f"The quadratic equation {self.worksheetQuestion} is rewritten in the form $(x+p)^2=q$, where $q$ is a constant. What is the value of $p$?"
        }, {
            "multipleChoice": True,
            "data": choices
        }]

        self.answer = choice1

#184
class Jan20Q15(Quadratics):
    #Initialize class with info to store in database, then we can dyamically add it to the database
    def __init__(self):
        super().__init__()
        #ID is topic + MAIN SKILL
        self.exam = "Jan2020"
        self.questionNumber = 15
        self.type = "MC"

        #This can get convoluted, so maybe don't worry about it so much right now
        self.skills = ["Take square roots"]

        """
        (x+d)^2+f=e^2+f
        (x+d)^2=e^2
        x+d= +- e
        """ 
        
        d = random.choice([x for x in range(-9,10) if x not in [0]])
        e = random.choice([x for x in range(-9,10) if x not in [0]])
        #ensure radicand is not negative
        f = random.choice([f for f in range(-9,10) if f not in [0] if e**2 + 2*f > 0])
        
        self.worksheetQuestion = formatMathString(f"(x+{d})^2+{f}={e**2+f}")
        self.worksheetAnswer = formatMathString(f"x={e-d} and x={-e-d}")

        choice1 = formatMathString(f"{e-d}") + " and " + formatMathString(f"{-e-d}")
        choice2 = formatMathString(f"{-e+d}") + " and " + formatMathString(f"{e+d}")
        choice3 = formatMathString(f"{-d}\pm\sqrt{e**2+f+f}")
        choice4 = formatMathString(f"{d}\pm\sqrt{e**2+f+f}")

        choices = [choice1, choice2, choice3, choice4]

        self.assessmentData = [{
            "text": True,
            "data": f"The solutions to {self.worksheetQuestion} are"
        }, {
            "multipleChoice": True,
            "data": choices
        }]

        self.answer = choice1   


#185
class June19Q21(Quadratics):
    #Initialize class with info to store in database, then we can dyamically add it to the database
    def __init__(self):
        super().__init__()
        #ID is topic + MAIN SKILL
        self.exam = "June2019"
        self.questionNumber = 21
        self.type = "MC"

        #This can get convoluted, so maybe don't worry about it so much right now
        self.skills = ["Quadratic Formula"]

        """
        The roots of x^2+bx+c=0 are
        x^2 - dx + (d^2-e)//4 = 0
        4x^2 - 4dx + (d^2-e) = 0
        4x^2-4dx+d^2-e=0
        (2x-d)^2 = e
        2x-d = sqrt(e)
        x = d +- sqrt(e) / 2
        """ 

        #random odd number
        a = 1
        c = random.choice([x for x in range(-10, 2) if x not in [-1,0,1] and (x-1)**2 - 4*x in getPrimes(150)])
        b = c + -1

        d = -b
        e = b**2 - 4*a*c

        self.worksheetQuestion = formatMathString(f"{a}x^2+{b}x+{c}=0")
        self.worksheetAnswer = formatMathString(fr"x=\frac{{{d}\pm\sqrt{{{e}}}}}{{{2}}}")

        choice1 = formatMathString(fr"x=\frac{{{d}\pm\sqrt{{{e}}}}}{{{2}}}")
        choice2 = formatMathString(fr"x=\frac{{{-d}\pm\sqrt{{{e}}}}}{{{2}}}")
        choice3 = formatMathString(f"{-1}") + " and " + formatMathString(f"{c}")
        choice4 = formatMathString(f"{1}") + " and " + formatMathString(f"{-c}")

        choices = [choice1, choice2, choice3, choice4]

        self.assessmentData = [{
            "text": True,
            "data": f"The roots of {self.worksheetQuestion} are"
        }, {
            "multipleChoice": True,
            "data": choices
        }]

        self.answer = choice1

#186
class June15Q18(Quadratics):
    #Initialize class with info to store in database, then we can dyamically add it to the database
    def __init__(self):
        super().__init__()
        #ID is topic + MAIN SKILL
        self.exam = "June2015"
        self.questionNumber = 18
        self.type = "MC"

        #This can get convoluted, so maybe don't worry about it so much right now
        self.skills = ["Complete the square"]

        """
        (x-d/2)^2 = e/4
        (x-d/2) = sqrt(e)/2
        x = (d +- sqrt(e))/2
        """ 
        
        a = 1
        d = random.choice([x for x in range(-9,10,2) if x not in [-1,0,1]])
        b = -d

        e = random.choice([x for x in getPrimes(50) if x-b**2 != 0])

        c = (e-b**2)//(-4)

        self.worksheetQuestion = formatMathString(f"(x+{toLatexFraction(d,2)})^2={toLatexFraction(e,4)}")
        self.worksheetAnswer = formatMathString(fr"x=\frac{{{-1*d}\pm\sqrt{{{e}}}}}{{{2}}}")

        choice1 = formatMathString(f"x^2+{b}x+{c}=0")
        choice2 = formatMathString(f"x^2+{b}x+{(-3-b**2)//-4}=0")
        choice3 = formatMathString(f"x^2+{-b}x+{c}=0")
        choice4 = formatMathString(f"x^2+{-b}x+{(-3-b**2)//-4}=0")

        choices = [choice1, choice2, choice3, choice4]

        self.assessmentData = [{
            "text": True,
            "data": f"When directed to solve a quadratic equation by completing the square, Sam arrived at the equation {self.worksheetQuestion}. Which equation could have been the original equation given to Sam?"
        }, {
            "multipleChoice": True,
            "data": choices
        }]

#187
class June15Q21(Quadratics):
    #Initialize class with info to store in database, then we can dyamically add it to the database
    def __init__(self):
        super().__init__()
        #ID is topic + MAIN SKILL
        self.exam = "June2015"
        self.questionNumber = 21
        self.type = "MC"

        #This can get convoluted, so maybe don't worry about it so much right now
        self.skills = ["Take square roots"]

        """
        d(ax+b)^2+e=dc^2+e
        d(ax+b)^2=dc^2
        (ax+b)^2=c^2
        ax+b=+-sqrt(c)
        """ 
        
        a = random.randint(2,9)
        b = random.choice([x for x in range(-9,10) if x not in [0]])
        c = random.randint(2,9)
        d = random.randint(2,7)
        e = random.choice([x for x in range(-9,10) if x not in [0]])

        self.worksheetQuestion = formatMathString(f"{d}({a}x+{b})^2+{e}={d*c**2+e}")
        self.worksheetAnswer = formatMathString(f"x={toLatexFraction(c-b,a)}") + " and " + formatMathString(f"x={toLatexFraction(-c-b,a)}")

        choice1 = formatMathString(f"{a}x+{b}=\pm{c}")
        choice2 = formatMathString(f"{a}x+{b}=\pm{c**2}")
        choice3 = formatMathString(f"{a**2}x^2+{b}={c**2}")
        choice4 = formatMathString(f"{a**2}x^2+{2*b*a}x+{b**2}={c}")

        self.answer = choice1

        choices = [choice1, choice2, choice3, choice4]

        self.assessmentData = [{
            "text": True,
            "data": f"A student is asked to solve the equation {self.worksheetQuestion}. The student's solution to the problem starts as {formatMathString(f'{d}({a}x+{b})^2={d*c**2}')} and goes to {formatMathString(f'({a}x+{b})^2={c**2}')}. A correct next step in the solution of the problem is"
        }, {
            "multipleChoice": True,
            "data": choices
        }]

#188 - skip
#189
class June14Q33(Quadratics):
    #Initialize class with info to store in database, then we can dyamically add it to the database
    def __init__(self):
        super().__init__()
        #ID is topic + MAIN SKILL
        self.exam = "June2014"
        self.questionNumber = 33
        self.type = "SA"

        #This can get convoluted, so maybe don't worry about it so much right now
        self.skills = ["Factor a trinomial with a = 1"]

        """
        (ax+b)(c+dx)+ex^2+f
        (ad+e)x^2 + (ac+bd)x + (bc + f)
        A              B          C
        A = 1,
        e = 1 - a*d

        then pick two numbers that add to B

        then their product = bc + f
        f = product - b*c

        predefine abcd, just so they are prime of each other in pairs

        
        """ 
        a = random.choice([x for x in range(-5,6) if x not in [-1,0,1]])
        b = random.choice([x for x in range(-5,6) if x != 0 and x % a != 0 and a % x != 0])
        
        c = random.choice([x for x in range(-5,6) if x not in [-1,0,1]])
        d = random.choice([x for x in range(-5,6) if x != 0 and x % a != 0 and a % x != 0])
        
        e = 1 - a*d

        B = a*c + b*d

        #ensures that f1 and f2 are not 0
        f1 = random.choice([x for x in range(-10,11) if (B - x) != 0 and x != 0])

        f2 = B - f1

        f = f1*f2 - b*c

        self.worksheetQuestion = formatMathString(f"({a}x+{b})({c}+{d}x)+{e}x^2+{f}")
        self.worksheetAnswer = formatMathString(f"x={-f1}") + " and " + formatMathString(f"x={-f2}")

        self.assessmentData = [{
            "text": True,
            "data": f"Write an equation that defines $m(x)$ as a trinomial where $m(x)$ = {self.worksheetQuestion}. Solve for $x$ when $m(x)=0$."
        }]

#190
class Aug14Q25(Quadratics):
    #Initialize class with info to store in database, then we can dyamically add it to the database
    def __init__(self):
        super().__init__()
        #ID is topic + MAIN SKILL
        self.exam = "Aug2014"
        self.questionNumber = 25
        self.type = "SA"

        #This can get convoluted, so maybe don't worry about it so much right now
        self.skills = ["Factor a trinomial with a = 1"]

        """
                
        """ 
        x1 = random.randint(-9,-1)
        x2 = random.randint(-9,-1)

        self.worksheetQuestion = formatMathString(f"x^2+{-x1-x2}x+{x1*x2}")
        self.worksheetAnswer = formatMathString(f"b={-x2}") + " and " + formatMathString(f"b={-x1}")

        self.assessmentData = [{
            "text": True,
            "data": f"In the equation {formatMathString(f'x^2+{-x1-x2}x+{x1*x2}=(x+a)(x+b)')}, $b$ is an integer. Find algebraically $all$ possible values of $b$."
        }]        

#191
class Jan15Q29(Quadratics):
    #Initialize class with info to store in database, then we can dyamically add it to the database
    def __init__(self):
        super().__init__()
        #ID is topic + MAIN SKILL
        self.exam = "Jan2015"
        self.questionNumber = 29
        self.type = "SA"

        #This can get convoluted, so maybe don't worry about it so much right now
        self.skills = ["Factor a trinomial with a > 1"]

        """
        4x^2 + bx = -c

        (2x+a)(2x+b)        
        """ 

        a = random.choice([x for x in range(-9,10,2)])
        b = random.choice([x for x in range(-9,10,2) if x != a and x != -a])
        
        self.worksheetQuestion = formatMathString(f"4x^2+{2*a+2*b}x={-a*b}")
        self.worksheetAnswer = formatMathString(f"x={toLatexFraction(-a,2)}") + " and " + formatMathString(f"x={toLatexFraction(-b,2)}")

        self.assessmentData = [{
            "text": True,
            "data": f"Solve the equation {self.worksheetQuestion} algebraically for $x$."
        }]      

#192
class Jan16Q27(Quadratics):
    #Initialize class with info to store in database, then we can dyamically add it to the database
    def __init__(self):
        super().__init__()
        #ID is topic + MAIN SKILL
        self.exam = "Jan2016"
        self.questionNumber = 27
        self.type = "SA"

        #This can get convoluted, so maybe don't worry about it so much right now
        self.skills = ["Factor a trinomial with a = 1"]

        """
        (y-a)^2=-b(y-a)

        y=a
        y=-b+a       
        """ 

        a = random.choice([x for x in range(-9,10) if x not in [0]])
        b = random.choice([x for x in range(-9,10) if x not in [0,1,-1]])
        
        self.worksheetQuestion = formatMathString(f"(y-{a})^2={-b}(y-{a})")
        self.worksheetAnswer = formatMathString(f"y={a}") + " and " + formatMathString(f"y={-b+a}")

        self.assessmentData = [{
            "text": True,
            "data": f"Solve the equation for $y$: {self.worksheetQuestion}"
        }]      

#193
class Aug17Q32(Quadratics):
    #Initialize class with info to store in database, then we can dyamically add it to the database
    def __init__(self):
        super().__init__()
        #ID is topic + MAIN SKILL
        self.exam = "Aug2017"
        self.questionNumber = 32
        self.type = "SA"

        #This can get convoluted, so maybe don't worry about it so much right now
        self.skills = ["Complete the square"]

        """
        ans = a +- b sqrt(c)

        eq = x^2 - 2ax = b^2c - a^2   
        """ 

        a = random.choice([x for x in range(-9,10) if x not in [0]])
        b = random.choice([x for x in range(-5,6) if x not in [0]])
        c = random.choice([x for x in notDivisibleByPerfectSquareList(25) if (b**2*x-a**2) < 100])

        self.worksheetQuestion = formatMathString(f"x^2+{-2*a}x={b**2*c-a**2}")
        self.worksheetAnswer = formatMathString(f"x={a}\pm{b}\sqrt{c}")

        self.assessmentData = [{
            "text": True,
            "data": f"Solve the equation {self.worksheetQuestion} by completing the square."
        }]      

#194
class Jun18Q27(Quadratics):
    #Initialize class with info to store in database, then we can dyamically add it to the database
    def __init__(self):
        super().__init__()
        #ID is topic + MAIN SKILL
        self.exam = "Jun2018"
        self.questionNumber = 27
        self.type = "SA"

        #This can get convoluted, so maybe don't worry about it so much right now
        self.skills = ["Quadratic Formula"]

        """
        ans = d +- sqrt(e) / 2

        eq = x^2 + bx + c = 0   
        """ 

        edChoices = []
        for e in notDivisibleByPerfectSquareList(50):
            for d in range(-5,6):
                if (e-d**2) % -4 == 0:
                    edChoices.append([e,d])

        random.shuffle(edChoices)
        e = edChoices[0][0]
        d = edChoices[0][1]
        a = 1
        b = -1*d
        c = (e - b**2)//(-4*a)
        
        self.worksheetQuestion = formatMathString(f"{a}x^2+{b}x+{c}=0")
        self.worksheetAnswer = formatMathString(f"x={round((d+e**(1/2))/2,1)}") + " and " + formatMathString(f"x={round((d-e**(1/2))/2,1)}")

        self.assessmentData = [{
            "text": True,
            "data": f"Solve for $x$ to the nearest \emph{{tenth}}: {self.worksheetQuestion}"
        }]     

#195
class Aug18Q30(Quadratics):
    #Initialize class with info to store in database, then we can dyamically add it to the database
    def __init__(self):
        super().__init__()
        #ID is topic + MAIN SKILL
        self.exam = "Aug2018"
        self.questionNumber = 30
        self.type = "SA"

        #This can get convoluted, so maybe don't worry about it so much right now
        self.skills = ["Complete the square"]

        """
        x = d +- sqrt(e)

        eq = x^2 - 2dx = e - d^2   
        """ 

        d = random.choice([x for x in range(-5,6) if x not in [0]])
        e = random.choice(notDivisibleByPerfectSquareList(50))
        
        self.worksheetQuestion = formatMathString(f"x^2+{-2*d}x={e-d**2}")
        self.worksheetAnswer = formatMathString(f"x={d}\pm\sqrt{e}")

        self.assessmentData = [{
            "text": True,
            "data": f"Solve the following equation by completing the square: {self.worksheetQuestion}"
        }]    

#196
class Jan19Q27(Quadratics):
    #Initialize class with info to store in database, then we can dyamically add it to the database
    def __init__(self):
        super().__init__()
        #ID is topic + MAIN SKILL
        self.exam = "Jan2019"
        self.questionNumber = 27
        self.type = "SA"

        #This can get convoluted, so maybe don't worry about it so much right now
        self.skills = ["Factor a trinomial with a = 1"]

        """
        x1 = -a
        x2 = -b

        x^2 + (a+b)x + ab = 0

        """ 

        a = random.choice([x for x in range(-10,11) if x not in [0]])
        b = random.choice([x for x in range(-10,11) if x not in [0] and x + a != 0])
        
        x1 = -a
        x2 = -b

        self.worksheetQuestion = formatMathString(f"x^2+{a+b}x+{a*b}=0")
        self.worksheetAnswer = formatMathString(f"x={x1}") + " and " + formatMathString(f"x={x2}")

        self.assessmentData = [{
            "text": True,
            "data": f"Solve {self.worksheetQuestion} algebraically. Explain the first step you used to solve the given equation."
        }]    

#197
class Jan19Q32(Quadratics):
    #Initialize class with info to store in database, then we can dyamically add it to the database
    def __init__(self):
        super().__init__()
        #ID is topic + MAIN SKILL
        self.exam = "Jan2019"
        self.questionNumber = 32
        self.type = "SA"

        #This can get convoluted, so maybe don't worry about it so much right now
        self.skills = ["Take square roots"]

        """
        ans = +- d sqrt(e)

        eq = fx^2 + g = fd^2e + g

        """ 

        g = random.choice([x for x in range(-5,6) if x not in [0]])
        f = random.randint(2,5)
        d = random.randint(2,5)
        e = random.choice([e for e in notDivisibleByPerfectSquareList(15) if e <= e*d**2*f])
        
        self.worksheetQuestion = formatMathString(f"{f}x^2+{g}={f*d**2*e+g}")
        self.worksheetAnswer = formatMathString(f"x=\pm{d}\sqrt{e}")

        self.assessmentData = [{
            "text": True,
            "data": f"Solve the quadratic equation below for the exact values of x: {self.worksheetQuestion}."
        }]    

#198
class June19Q28(Quadratics):
    #Initialize class with info to store in database, then we can dyamically add it to the database
    def __init__(self):
        super().__init__()
        #ID is topic + MAIN SKILL
        self.exam = "June2019"
        self.questionNumber = 28
        self.type = "SA"

        #This can get convoluted, so maybe don't worry about it so much right now
        self.skills = ["Take square roots"]

        """
        ans = +- d

        eq = ex^2 = ed^2

        """ 

        d = random.randint(2,9)
        e = random.choice([e for e in range(2,10) if e != 0 and abs(e*d**2) <= 180])
        
        self.worksheetQuestion = formatMathString(f"{e}x^2={e*d**2}")
        self.worksheetAnswer = formatMathString(f"x=\pm{d}")

        self.assessmentData = [{
            "text": True,
            "data": f"Solve {self.worksheetQuestion} algebraically"
        }]    

#199
class Aug19Q31(Quadratics):
    #Initialize class with info to store in database, then we can dyamically add it to the database
    def __init__(self):
        super().__init__()
        #ID is topic + MAIN SKILL
        self.exam = "Aug2019"
        self.questionNumber = 31
        self.type = "SA"

        #This can get convoluted, so maybe don't worry about it so much right now
        self.skills = ["Take square roots"]

        """
        ans = +- d

        eq = ex^2 - ed = 0

        """ 

        e = random.randint(2,9)
        d = random.choice(notDivisibleByPerfectSquareList(50))
        
        self.worksheetQuestion = formatMathString(f"{e}x^2-{e*d}=0")
        self.worksheetAnswer = formatMathString(f"x=\pm\sqrt{d}")

        self.assessmentData = [{
            "text": True,
            "data": f"Solve {self.worksheetQuestion} for the exact values of $x$."
        }]    

#200
class Jan20Q31(Quadratics):
    #Initialize class with info to store in database, then we can dyamically add it to the database
    def __init__(self):
        super().__init__()
        #ID is topic + MAIN SKILL
        self.exam = "Jan2020"
        self.questionNumber = 31
        self.type = "SA"

        #This can get convoluted, so maybe don't worry about it so much right now
        self.skills = ["Complete the square"]

        """
        ans = d +- sqrt(e)

        eq = x^2 - 2dx + d^2 - e = 0

        """ 

        d = random.choice([x for x in range(-9,10) if x not in [0]])
        e = random.choice(notDivisibleByPerfectSquareList(50))
        
        self.worksheetQuestion = formatMathString(f"x^2+{-2*d}x+{d**2-e}=0")
        self.worksheetAnswer = formatMathString(f"x={d}\pm\sqrt{e}")

        self.assessmentData = [{
            "text": True,
            "data": f"Use the method of completing the square to determine the exact values of $x$ for the equation {self.worksheetQuestion}."
        }]    

#201
class Aug14Q32(Quadratics):
    #Initialize class with info to store in database, then we can dyamically add it to the database
    def __init__(self):
        super().__init__()
        #ID is topic + MAIN SKILL
        self.exam = "Aug2014"
        self.questionNumber = 32
        self.type = "SA"

        #This can get convoluted, so maybe don't worry about it so much right now
        self.skills = ["Complete the square"]

        """
        ans = d +- sqrt(e)

        eq = x^2 - 2dx + d^2 - e = 0

        """ 

        d = random.choice([x for x in range(-9,10) if x not in [0]])
        e = random.choice(notDivisibleByPerfectSquareList(50))
        c = d**2-e

        self.worksheetQuestion = formatMathString(f"x^2+{-2*d}x+{d**2-e}=0")
        self.worksheetAnswer = formatMathString(f"x={d}\pm\sqrt{e}")

        self.assessmentData = [{
            "text": True,
            "data": f"A student was given the equation {self.worksheetQuestion} to solve by completing the square. The first step that was written is shown below."
        }, {
            "text": True,
            "data": f"{formatMathString(f'x^2+{-2*d}x={-1*(d**2-e)}')}"
        }, {
            "text": True,
            "data": f"The next step in the student's process was {formatMathString(f'x^2+{-2*d}x+c={-1*(d**2-e)}+c')}. State the value of $c$ that creates a perfect square trinomial. Explain how the value of $c$ is determined."
        }]    

        self.answer = f"$c$ is {d**2} by dividing {-2*d} by 2 and squaring it."

#202
class Jan16Q34(Quadratics):
    #Initialize class with info to store in database, then we can dyamically add it to the database
    def __init__(self):
        super().__init__()
        #ID is topic + MAIN SKILL
        self.exam = "Jan2016"
        self.questionNumber = 34
        self.type = "SA"

        #This can get convoluted, so maybe don't worry about it so much right now
        self.skills = ["Quadratic Formula"]

        """
        ans = d +- sqrt(e)/2

        eq = 4x^2 - 8dx + 4d^2-e = 0

        """ 

        d = random.choice([x for x in range(-5,6) if x not in [0]])
        e = random.choice(notDivisibleByPerfectSquareList(50))
        
        self.worksheetQuestion = formatMathString(f"4x^2+{-8*d}x+{4*d**2-e}=0")
        self.worksheetAnswer = formatMathString(f"x={round(d+e**(1/2)/2,1)}") + " and " + formatMathString(f"x={round(d-e**(1/2)/2,1)}")

        self.assessmentData = [{
            "text": True,
            "data": f"Fred's teacher gave the class the quadratic function"
        }, {
            "text": True,
            "data": f"{formatMathString(f'f(x) = 4x^2+{-8*d}x+{4*d**2-e}=0')}"
        }, {
            "text": True,
            "data": f"a) State two different methods Fred could use to solve the equation $f(x)=0$."
        }, {
            "text": True,
            "data": f"b) Using one of the methods stated in part $a$, solve $f(x)=0$ for $x$, to the nearest $tenth$."
        }]    

#203
class June16Q33(Quadratics):
    #Initialize class with info to store in database, then we can dyamically add it to the database
    def __init__(self):
        super().__init__()
        #ID is topic + MAIN SKILL
        self.exam = "June2016"
        self.questionNumber = 33
        self.type = "SA"

        #This can get convoluted, so maybe don't worry about it so much right now
        self.skills = ["Take square roots"]

        """
        ans = +- a

        eq = 0 = bx^2-ba^2

        """ 

        a = random.randint(3,9)
        b = random.choice([x for x in range(-20,-5) if x not in [0]])
        
        self.worksheetQuestion = formatMathString(f"0={b}x^2-{b*a**2}")
        self.worksheetAnswer = formatMathString(f"x={a}")

        englishIntegers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        
        englishInt = englishIntegers[a-2]
        englishInt2 = englishIntegers[a-1]

        self.assessmentData = [{
            "text": True,
            "data": f"The height, $H$, in feet, of an object dropped from the top of a building after $t$ seconds is given by {formatMathString(f'H(t)={b}x^2-{b*a**2}')}. How many feet did the object fall between {englishInt} and {englishInt2} seconds after it was dropped? Determine, algebraically, how many seconds it will take for the object to reach the ground."
        }]

        self.answer = f"It fell {(b*(a-2)**2-b*a**2)-(b*(a-1)**2-b*a**2)} feet," + " and " + formatMathString(f"x={a}")    

#204
class June16Q28(Quadratics):
    #Initialize class with info to store in database, then we can dyamically add it to the database
    def __init__(self):
        super().__init__()
        #ID is topic + MAIN SKILL
        self.exam = "June2016"
        self.questionNumber = 28
        self.type = "SA"

        #This can get convoluted, so maybe don't worry about it so much right now
        self.skills = ["Factor a trinomial with a > 1"]

        """
        ans = (x+d/2)(x+e)=0
        (2x+d)(x+e)=0

        eq = 2x^2-x(d+2e)+de=0

        """ 

        d = random.choice([x for x in range(-9,9,2) if x not in [0]])
        e = random.choice([x for x in range(-10,10,2) if x not in [0] and (2*x + d) != 0])
        
        b = d + 2*e
        c = d*e

        self.worksheetQuestion = formatMathString(f"2x^2+{b}x+{c}=0")
        self.worksheetAnswer = formatMathString(f"x={toLatexFraction(-d,2)} and x={-e}")

        self.assessmentData = [{
            "text": True,
            "data": f"Amy solved the equation {self.worksheetQuestion}. She stated that the solutions to the equations were {formatMathString(toLatexFraction(-d,2))} and {-e}. Do you agree with Amy's solutions? Explain why or why not."
        }]

        self.answer = f"Agree. The equation factors to be {formatMathString(f'(2x+{d})(x+{e})')}"

#205
class Aug16Q36(Quadratics):
    #Initialize class with info to store in database, then we can dyamically add it to the database
    def __init__(self):
        super().__init__()
        #ID is topic + MAIN SKILL
        self.exam = "Aug2016"
        self.questionNumber = 36
        self.type = "SA"

        #This can get convoluted, so maybe don't worry about it so much right now
        self.skills = ["Factor a trinomial with a > 1"]

        """
        d^2x^2+(f+e)dx+fe=0

        (dx+f)(dx+e)
        """ 

        d = random.randint(2,9)
        f = random.choice([x for x in range(-9,10) if x != 0 and x % d != 0 and d % x != 0])
        e = random.choice([x for x in range(-9,10) if x != 0 and x != -1*f and x % d != 0 and d % x != 0 and d % (x+f) != 0 and (x+f) % d != 0])

        a = d**2
        b = (f+e)*d
        c = f*e
        
        self.worksheetQuestion = formatMathString(f"0={a}x^2+{d*(f+e)}x+{f*e}")
        self.worksheetAnswer = formatMathString(f"x={toLatexFraction(-f,d)}") + " and " + formatMathString(f"x={toLatexFraction(-e,d)}")
        print(self.worksheetAnswer)
        self.assessmentData = [{
            "text": True,
            "data": f"Janice is asked to solve {self.worksheetQuestion}. She begins the problem by writing the following steps:"
        }, {
            "text": True,
            "data": f"Line 1  {self.worksheetQuestion}"
        }, {
            "text": True,
            "data": f"Line 2  {formatMathString(f'0=B^2+2B+{f*e}')}"
        },{
            "text": True,
            "data": f"Line 3  {formatMathString(f'(B+{f})(B+{e})')}"
        }, {
            "text": True,
            "data": f"Use Janice's procedure to solve the equation for $x$. Explain the method Janice used to solve the quadratic equation."
        }]

        self.answer = f"Factored and substituted. {self.worksheetAnswer}"

quadraticsQuestionsDict = {"Aug16Q36": Aug16Q36, "June16Q28": June16Q28, "June16Q33": June16Q33, "Jan16Q34": Jan16Q34, "Aug14Q32": Aug14Q32, "Jan20Q31": Jan20Q31, "Aug19Q31": Aug19Q31, "June19Q28": June19Q28, "Jan19Q32": Jan19Q32, "Jan19Q27": Jan19Q27, "Aug18Q30": Aug18Q30, "Jun18Q27": Jun18Q27, "Aug17Q32": Aug17Q32, "Jan16Q27": Jan16Q27, "Jan15Q29": Jan15Q29, "Aug14Q25": Aug14Q25, "June14Q33": June14Q33, "June15Q21": June15Q21, "June15Q18": June15Q18, 
"June19Q21": June19Q21, "Jan20Q15": Jan20Q15, "June18Q12": June18Q12, "Jan18Q14": Jan18Q14, "June17Q22": June17Q22, "Jan17Q02": Jan17Q02, "Jan17Q15": Jan17Q15, "Aug16Q19": Aug16Q19, "June16Q19": June16Q19, "Aug15Q23": Aug15Q23, "June15Q23": June15Q23, "Aug14Q03": Aug14Q03,  "June14Q10": June14Q10, 
"Jan19Q15": Jan19Q15, "Jan17Q22": Jan17Q22,  "Jan16Q14": Jan16Q14, "Jan15Q17": Jan15Q17, "Jan15Q03": Jan15Q03, "June14Q8": June14Q8}