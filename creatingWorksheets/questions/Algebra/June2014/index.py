from pylatex import (Document, TikZ, TikZNode, Plot,
                     TikZDraw, TikZCoordinate, Axis, Tabular,
                     TikZUserPath, TikZOptions, Center, VerticalSpace, NewLine, Math, Alignat, Section, NewLine)
from pylatex.utils import (NoEscape, bold)
import sys
sys.path.insert(0, "F:/code/bielejec-sheets-be/creatingWorksheets/utils")
from questionFormatting import multipleChoice, multipleChoicePic
from equations import formatExpression, formatEquation
from docRelated import alignedEquations
from graphs import graphLinearFunction, shadeLinearInequality, axisOptions
import math, fractions, numpy, string, uuid, random

# __all__ = ["June2014_1", "June2014_12"]

class June2014_1():
    #Initialize class with info to store in database, then we can dyamically add it to the database
    def __init__(self):
        #ID is topic + MAIN SKILL
        self.subject = "Algebra"
        self.standards = ["some string", "some other string"]
        self.state = "New York"
        self.exam = "June2014"
        self.topics = ["#1Topic", "#2Topic"]
        self.questionNumber = 1
        self.type = "MC"

        self.id = "Algebra.NY.June2014.1"
        #This can get convoluted, so maybe don't worry about it so much right now
        self.skills = ["some major skill", "some other major skill"]

        self.correctAnswer = None

        self.solution = None

    def addQuestion(self, doc = None):
        #Junk here where you add to the document
        """
        When solving the equation A(Bx^2 + C) - D = Ex^2 + F, {name} wrote A(Bx^2 + C) = Ex^2 + F + D as her first step. Which property justifies {name}'s first step?
        A -> random numbeer between 2, 9
        B -> random number between 2, 9

        Choices:
        1) Addition property of equality
        2) commutative property of equality
        3) multiplication property of equality
        4) distributive property of equatlity
        """
        a = random.randint(2,9)
        b = random.randint(2,9)
        c = random.randint(2,9)
        d = random.randint(2,9)
        e = random.randint(2,9)
        f = random.randint(2,9)
        
        name = random.choice(["Emily", "David", "Jakim", "Joe", "John"])

        #Let's see if it works without anything in particular
        equation1 = formatEquation(data = [
            formatExpression([{"co": a}]),
            "(",
            formatExpression([
                {"co": b, "term": "x^2"},
                {"co": c}
                ]),
            ")",
            "-",
            formatExpression([{"co":d}]),
            "=",
            formatExpression([
                {"co": e,"term":"x^2"}, 
                {"co": f}
                ])
        ])
        
        equation2 = formatEquation(data = [
            formatExpression([
                {"co":a}
                ]),
            "(",
            formatExpression([
                {"co": b, "term": "x^2"},
                {"co": c}]),
            ")",
            "=",
            formatExpression([{"co": e, "term": "x^2"}, {"co": f+d}])
        ])
        
        wholeString = f"When solving the equation ${equation1}$, {name} wrote ${equation2}$, as their first step. Which property justifies {name}'s first step"

        #Choice 1 is always correct answer
        choice1 = "Addition property of equality"
        choice2 = "Commutative property of equality"
        choice3 = "Multiplication property of equality"
        choice4 = "Distributive property of equality"

        #Adds question
        doc.append(NoEscape(f"{wholeString}"))

        #Adds choices - returns correct answer
        self.correctAnswer = multipleChoice(choices = [choice1, choice2, choice3, choice4], doc = doc, math = False)

        self.explanation = f"Since we added {d} (+{d}) to both sides, it is Addition Property of Equality, which is Choice {self.correctAnswer}."
        
        solEquation1 = formatEquation([
            formatExpression([{"co":a}]),
            "(",
            formatExpression([{"co": b, "term": "x^2"},{"co": c}]),
            ")",
            formatExpression([{"align": True, "co": -d}]),
            "&&=",
            formatExpression([{"co": e, "term": "x^2"}, {"align": True, "co": f}])
        ])
    
        solEquation2 = formatEquation([formatExpression([
            {"co": a}
            ]),"(",formatExpression([{"co": b, "term": "x^2"},{"co":c}]),")","&=",formatExpression([{"co": e, "term": "x^2"}, {"co": f+d}])])

        self.solution = [[3, solEquation1, f"&+{d}&&=&&+{d}"], [2, solEquation2]]
        
    def addAnswer(self, doc = None):
        doc.append(NoEscape(f"{self.correctAnswer}"))
        
    
    def addSolution(self, doc = None):
        #Creates a subsection
        #Creates an aligned environment
        doc.append(NoEscape(f"({self.questionNumber})"))
        alignedEquations(self.solution, explanation=self.explanation, doc = doc)

class June2014_2():
    #Initialize class with info to store in database, then we can dyamically add it to the database
    def __init__(self):
        #ID is topic + MAIN SKILL
        self.subject = "Algebra"
        self.standards = ["some string", "some other string"]
        self.state = "New York"
        self.exam = "June2014"
        self.topics = ["#4Topic", "#3Topic"]
        self.questionNumber = 2
        self.type = "MC"


        self.id = "Algebra.NY.June2014.2"
        #This can get convoluted, so maybe don't worry about it so much right now
        self.skills = ["some major skill", "some other major skill"]
        self.correctAnswer = None
        self.solution = None

    def addQuestion(self, doc = None):
        #Junk here where you add to the document
        """
        Officials in a town use a function, {C}, to analyze traffic patterns.
        {C(n)} represents the rate of traffic through an intersection where
        {n} is the number of observed vehicles in a specified time interval.
        What would be the most appropriate domain for the function?
        1) {...-2, -1, 0, 1, 2, 3...} negative integer by 1's past 0 continuous
        2) {-2, -1, 0, 1, 2, 3} negative integers by 1's past 0 not continuous
        3) {0, 1/2, 1, 1 1/2, 2, 2 1/2} starting at 0, by fractions
        4) {0, 1, 2, 3...} starting at 0 by 1's continous
        
        """
        def setNotationList(values, continuousFront = False, continuousBack = False):
            #Continuous means ... in front
            if continuousFront:
                string = "\{..."
            else:
                string = "\{"
            for val in values:
                string += f"{val}, "
            #now there is a comma and space left over
            if continuousBack:
                string = string[:-2] + "...\}"
            else:
                string = string[:-2] + "\}"
            return string

        #correct answer, which is actually choice 4
        choice1List = [x for x in range(0, random.randint(4,6))]
        choice1 = setNotationList(choice1List, continuousBack = False, continuousFront = True)
        
        #choice 1 really
        choice2List = [x for x in range(-1*random.randint(2,3), random.randint(4,5))]
        choice2 = setNotationList(choice2List, continuousBack = True, continuousFront = True)
        
        #choice 2 really
        choice3List = [x for x in range(-1*random.randint(2,4), random.randint(4,5))]
        choice3 = setNotationList(choice3List)

        #choice 3 really
        choice4List = []
        denominator = random.randint(2,5)
        count = 6 #going to do only 6 values
        for wholeNumber in range(7):
            #0, 1, 2
            for numerator in range(denominator):
                #0 + 0, 0 + 1/4, 0 + 2/4, 0 + 3/4 etc 
                if wholeNumber == 0 and numerator != 0:
                    #single fractions
                    choice4List.append(fr"\frac{numerator}{denominator} ")
                elif numerator == 0:
                    #just do the whole number then
                    choice4List.append(f"{wholeNumber}")
                else:
                    #mixed number
                    choice4List.append(fr"{wholeNumber}\frac{numerator}{denominator} ")

        choice4 = setNotationList(choice4List[:count], continuousFront = True)
        
        functionName = random.choice(string.ascii_uppercase)
        variableName = random.choice([x for x in string.ascii_lowercase if x.upper() != functionName])

        questionString = f"Officials in a town use a function, {functionName}, to analyze traffic patterns. {functionName}({variableName}) represents the rate of traffic through an intersection where {variableName} is the number of observed vehicles in a specified time interval. What would be the most appropriate domain for the function?"
        
        doc.append(NoEscape(questionString))

        self.correctAnswer = multipleChoice(choices = [choice1, choice2, choice3, choice4], doc = doc)
        self.solution = f"The function {functionName}({variableName}) represents vehicles, which can only be whole numbers including 0. Also the '...' at the end means that there will be more cars coming."


    def addAnswer(self, doc = None):
        doc.append(NoEscape(f"{self.correctAnswer}"))
    
    def addSolution(self, doc = None):
        doc.append(NoEscape(self.solution))

class June2014_3():
    #Initialize class with info to store in database, then we can dyamically add it to the database
    def __init__(self):
        #ID is topic + MAIN SKILL
        self.subject = "Algebra"
        self.standards = ["some string", "some other string"]
        self.state = "New York"
        self.exam = "June2014"
        self.topics = ["#5Topic", "#6Topic"]
        self.questionNumber = 3
        self.type = "MC"


        self.id = "Algebra.NY.June2014.3"
        #This can get convoluted, so maybe don't worry about it so much right now
        self.skills = ["some major skill", "some other major skill"]

        self.solution = None
        self.correctAnswer = None

    def addQuestion(self, doc = None):
        """
        If A = a1x^2 + b1x + c1 and B = a2x^2 + b2x + c2, then A - B equals
        (a1, b1, etc can be negative, just not 0)
        and a1 and a2 cannot be opposites or same number
        (1) (a1-a2)x^2 + (b1-b2)x + (c1-c2) ****correct answer
        (2) (-a1+a2)x^2 + (-b1+b2)x + (-c1+c2)  
        (3) (-a1+a2)x^2 + (b1+b2)x + (c1+c2)
        (4) (a1-a2)x^2 + (b1+b2)x + (c1+c2)
        """
        coeffecientChoices = [x for x in range(-9,10) if x != 0]
        a1 = random.choice(coeffecientChoices)
        a2 = random.choice([x for x in coeffecientChoices if x != a1 or x != -a1])

        b1 = random.choice(coeffecientChoices)
        b2 = random.choice([x for x in coeffecientChoices if x != b1 or x != -b1])

        c1 = random.choice(coeffecientChoices)
        c2 = random.choice([x for x in coeffecientChoices if x != c1 or x != -c1])

        equation1Name = random.choice(string.ascii_uppercase)
        equation2Name = random.choice([x for x in string.ascii_uppercase if x != equation1Name])
        
        equation1 = formatEquation([
            formatExpression([{"co": 1, "term": equation1Name}]),
            "=",
            formatExpression([{"co": a1, "term": "x^2"}, {"co": b1, "term": "x"}, {"co": c1}])
        ])

        equation2 = formatEquation([
            formatExpression([{"co": 1, "term": equation2Name}]),
            "=",
            formatExpression([{"co": a2, "term": "x^2"}, {"co": b2, "term": "x"}, {"co": c2}])
        ])

        choice1 = formatExpression([{"co": a1-a2, "term": "x^2"}, {"co": b1-b2, "term": "x"}, {"co": c1-c2}])
        

        choice2 = formatExpression([{"co": -a1+a2, "term": "x^2"}, {"co": -b1+b2, "term": "x"}, {"co": -c1+c2}])
        

        choice3 = formatExpression([{"co": -a1+a2, "term": "x^2"}, {"co": b1+b2, "term": "x"}, {"co": c1+c2}])
        

        choice4 = formatExpression([{"co": a1-a2, "term": "x^2"}, {"co": b1+b2, "term": "x"}, {"co": c1+c2}])
        

        differenceEquation = formatEquation([
            formatExpression([{"co": 1, "term": equation1Name}, {"co": -1, "term": equation2Name}])
        ])

        questionString = f"If ${equation1}$ and ${equation2}$, then ${differenceEquation}$ equals"
        
        doc.append(NoEscape(questionString))
        
        self.correctAnswer = multipleChoice(choices = [choice1, choice2, choice3, choice4], doc = doc)
        
        solutionEquation1 = formatEquation([
            "&& ",
            formatExpression([{"align": True, "co": a1, "term": "x^2"}, {"align": True, "co": b1, "term": "x"}, {"align": True, "co": c1}])
        ])
        
        solutionEquation2 = formatEquation([
            "&&+  ",
            formatExpression([{"align": True, "co": -a2, "term": "x^2"}, {"align": True, "co": -b2, "term": "x"}, {"align": True, "co": -c2}])
        ])

        solutionEquation3 = formatEquation(["&&",
        formatExpression([{"align": True, "co": a1-a2, "term": "x^2"}, {"align": True, "co": b1-b2, "term": "x"}, {"align": True, "co": c1-c2}])
        ])

        self.solution = [
            [4,solutionEquation1, solutionEquation2],
            [4, solutionEquation3]
        ]
        self.explanation = f"({self.questionNumber}) For ${equation1Name}$ - ${equation2Name}$, we line the equations vertically. Then we keep the top equation, change the - to a +, and change all the signs for the bottom equation. Then add like terms."

    def addAnswer(self, doc = None):
        doc.append(f"{self.correctAnswer}")
    
    def addSolution(self, doc = None):
        alignedEquations(self.solution, explanation = self.explanation, doc = doc)

class June2014_4():
    #Initialize class with info to store in database, then we can dyamically add it to the database
    def __init__(self):
        #ID is topic + MAIN SKILL
        self.subject = "Algebra"
        self.standards = ["some string", "some other string"]
        self.state = "New York"
        self.exam = "June2014"
        self.topics = ["#5Topic", "#6Topic"]
        self.questionNumber = 3
        self.type = "MC"


        self.id = "Algebra.NY.June2014.4"
        #This can get convoluted, so maybe don't worry about it so much right now
        self.skills = ["some major skill", "some other major skill"]

        self.solution = None
        self.correctAnswer = None

    def addQuestion(self, doc = None):
        """
        Given: y + Ax > B
               y <= Cx - D

        Which graph shows the solution of the given set of inequalities?
        ##Notes: top equation is single step sovling, bottom equation is solved. one dashed one solid
        choice 1 - correct answer (really choice 2)
        choice 2 - (really choice 1) - same as correct but top equation NOT dashed
        choice 3 - (really choice 3) - both solid, reversed signs
        choice 4 - (really choice 4) - reversed signs 
        """
        choices = [x for x in range(-3,4) if x != 0]
        A = random.choice(choices)
        B = random.choice(choices)

        C = random.choice([item for item in choices if item != -1*A ])
        D = random.choice(choices)

        m1 = -A
        b1 = B
        m2 = C
        #forcing slops to be postive and negative
        if m1 > 0 and m2 > 0:
            m2 = -m2
        elif m1 < 0 and m2 < 0:
            m2 = -m2
        else:
            m2 = m2
        
        b2 = D

        #signs - ensuring that we always have one = and one greater than
        sign1 = random.choice(["<", ">"])
        if sign1 == "<":
            sign2 = ">="
        else:
            sign2 = "<="
        
        
        # doc.append(NoEscape(questionString))
        #Start of tikzpicture
        def choice1(doc = None):
            with doc.create(TikZ()) as pic:
                with pic.create(Axis(options=axisOptions())) as axis:
                    
                    graphLinearFunction(slope=m1, yIntercept=b1, dashed = True if sign1 == "<" or sign1 == ">" else False, axis = axis)
                    shadeLinearInequality(slope=m1, yIntercept=b1, greaterThan = True if sign1 == ">=" or sign1 == ">" else False, axis = axis)

                    graphLinearFunction(slope=m2, yIntercept=b2, axis = axis, dashed = True if sign2 == "<" or sign2 == ">" else False)
                    shadeLinearInequality(slope=m2, yIntercept=b2, greaterThan = True if sign2 == ">=" or sign2 == ">" else False, axis = axis)
        def choice2(doc = None):
            with doc.create(TikZ()) as pic:
                with pic.create(Axis(options=axisOptions())) as axis:
                    
                    #dashed is the reverse of dashed on choice 1
                    graphLinearFunction(slope=m1, yIntercept=b1, dashed = False if sign1 == "<" or sign1 == ">" else True, axis = axis)
                    shadeLinearInequality(slope=m1, yIntercept=b1, greaterThan = True if sign1 == ">=" or sign1 == ">" else False, axis = axis)

                    graphLinearFunction(slope=m2, yIntercept=b2, axis = axis, dashed = True if sign2 == "<" or sign2 == ">" else False)
                    shadeLinearInequality(slope=m2, yIntercept=b2, greaterThan = True if sign2 == ">=" or sign2 == ">" else False, axis = axis)

        def choice3(doc = None):
            with doc.create(TikZ()) as pic:
                with pic.create(Axis(options=axisOptions())) as axis:
                    
                    #Both lines are solid
                    #signs are reverse from original
                    graphLinearFunction(slope=m1, yIntercept=b1, dashed = False, axis = axis)
                    shadeLinearInequality(slope=m1, yIntercept=b1, greaterThan = False if sign1 == ">=" or sign1 == ">" else True, axis = axis)

                    #Both lines are solid
                    #signs are reverse from original
                    graphLinearFunction(slope=m2, yIntercept=b2, axis = axis, dashed = False)
                    shadeLinearInequality(slope=m2, yIntercept=b2, greaterThan = False if sign2 == ">=" or sign2 == ">" else True, axis = axis)

        def choice4(doc = None):
            with doc.create(TikZ()) as pic:
                with pic.create(Axis(options=axisOptions())) as axis:
                    #signs are reversed from original
                    graphLinearFunction(slope=m1, yIntercept=b1, dashed = True if sign1 == "<" or sign1 == ">" else False, axis = axis)
                    shadeLinearInequality(slope=m1, yIntercept=b1, greaterThan = False if sign1 == ">=" or sign1 == ">" else True, axis = axis)

                    #signs are reversed from original
                    graphLinearFunction(slope=m2, yIntercept=b2, axis = axis, dashed = True if sign2 == "<" or sign2 == ">" else False)
                    shadeLinearInequality(slope=m2, yIntercept=b2, greaterThan = False if sign2 == ">=" or sign2 == ">" else True, axis = axis)
        doc.append(NoEscape("Given:"))
        doc.append(NewLine())

        latexSignsDictionary = {
            "<": "<",
            ">": ">",
            "<=": " \leq ",
            ">=":" \geq "
        }

        inequality1 = formatEquation([
            formatExpression([
                {"co": 1, "term": "y"}, 
                {"co": A, "term": "x"}
                ]), 
                latexSignsDictionary[sign1], 
                formatExpression([{"co": B}])
                ])
        inequality2 = formatEquation([
            formatExpression([
                {"co": 1, "term": "y"}
                ]), 
                latexSignsDictionary[sign2], 
                formatExpression([{"co": C, "term":"x"}, {"co": D}])
                ])

        doc.append(NoEscape(f"${inequality1}$"))
        doc.append(NewLine())
        doc.append(NoEscape(f"${inequality2}$"))
        doc.append(NewLine())
        doc.append(NoEscape("Which graph shows the solution of the given set of inequalities?"))
        self.correctAnswer = multipleChoicePic(choices = [choice1, choice2, choice3, choice4], doc = doc)
        
        

        # self.solution = [
        #     [4,solutionEquation1, solutionEquation2],
        #     [4, solutionEquation3]
        # ]
        # self.explanation = f"({self.questionNumber}) For ${equation1Name}$ - ${equation2Name}$, we line the equations vertically. Then we keep the top equation, change the - to a +, and change all the signs for the bottom equation. Then add like terms."

    def addAnswer(self, doc = None):
        doc.append(f"{self.correctAnswer}")
        pass
    
    def addSolution(self, doc = None):
        # alignedEquations(self.solution, explanation = self.explanation, doc = doc)
        pass

class June2014_5():
    #Initialize class with info to store in database, then we can dyamically add it to the database
    def __init__(self):
        #ID is topic + MAIN SKILL
        self.subject = "Algebra"
        self.standards = ["some string", "some other string"]
        self.state = "New York"
        self.exam = "June2014"
        self.topics = ["#5Topic", "#6Topic"]
        self.questionNumber = 3
        self.type = "MC"


        self.id = "Algebra.NY.June2014.5"
        #This can get convoluted, so maybe don't worry about it so much right now
        self.skills = ["some major skill", "some other major skill"]

        self.solution = None
        self.correctAnswer = None

    def addQuestion(self, doc = None):
        """
        Which value of x satisfies the equation frac{a}{b}(x + {a2}{b2}) = c?
        
        (1) Correct answer c*b/a - a*a2/b*b2
        (2) C*b/a
        (3) C - a*a2/b*b2
        (4) C - a/b*a2/b2 * a / b - rounded to two decimals
        """
        coeffecientChoices = [x for x in range(2,8) if x != 0]

        #Start off with some random integer as C
        c = random.randint(10,30)

        #Now pick a multiple of c
        cFractionDenom = random.randint(2,5)
        cFractionNumer = c*cFractionDenom

        #now we have the fraction that represents the integer
        a = random.choice(coeffecientChoices)
        b = random.choice([x for x in coeffecientChoices if x % a != 0 and a % x != 0])

        #multA / a needs to equal cFractionDemon
        multA = cFractionDenom * a

        #multB / b needs to equal cFractionNumer
        multB = cFractionNumer * b

        #now we have the fraction that is the answer + multB/multA (x + multB/multA)

        #So we can find choices for the answer
        answerChoices = []
        remainingNumerators = []

        def is_repeating(fraction):
            denom = fraction.denominator
            while not (denom % 2):
                denom //= 2
            while not (denom % 5):
                denom //= 5
            return denom != 1

        for answer in range(1, multB):
            guess = answer/multA
            # fractions.Fraction instances are automatically put in lowest terms.
            ratio = fractions.Fraction(answer, multA)
            
            if not is_repeating(ratio) and ratio.denominator != 1: 
                answerChoices.append(guess)
                remainingNumerators.append(multB-answer)

        answerIndex = random.randint(0, len(answerChoices)-1)
        answer = answerChoices[answerIndex]
        remainingNumerator = remainingNumerators[answerIndex]

        #a/b(x + a2/b2) = c

        a2 = remainingNumerator
        b2 = multA

        #change fractions to lowest form
        firstFraction = fractions.Fraction(a,b)
        a = firstFraction.numerator
        b = firstFraction.denominator

        secondFraction = fractions.Fraction(a2,b2)
        a2 = secondFraction.numerator
        b2 = secondFraction.denominator

        questionEquation = formatEquation([
            f"\\frac{{{a}}}{{{b}}}(",
            f"x+\\frac{{{a2}}}{{{b2}}}",
            f")={c}"
        ])

        print(questionEquation)

        choice1 = f"{answer}"
        choice2 = f"{round(c*b/a,2)}"
        choice3 = f"{round(c-a*a2/b*b2,2)}"
        choice4 = f"{round(c-a/b*a2/b2*a/b, 2)}"
        
        print(a,b,a2,b2,c)
        questionString = f"Which value of x satisfies the equation ${questionEquation}$"
        
        doc.append(NoEscape(questionString))
        
        self.correctAnswer = multipleChoice(choices = [choice1, choice2, choice3, choice4], doc = doc)
        
        self.explanation = f"Plug left side into Y1, right side into Y2, Look in the table to see when they are the same."

    def addAnswer(self, doc = None):
        doc.append(f"{self.correctAnswer}")
    
    def addSolution(self, doc = None):
        doc.append(NoEscape(self.explanation))

class June2014_6():
    #Initialize class with info to store in database, then we can dyamically add it to the database
    def __init__(self):
        #ID is topic + MAIN SKILL
        self.subject = "Algebra"
        self.standards = ["some string", "some other string"]
        self.state = "New York"
        self.exam = "June2014"
        self.topics = ["#5Topic", "#6Topic"]
        self.questionNumber = 3
        self.type = "MC"


        self.id = "Algebra.NY.June2014.6"
        #This can get convoluted, so maybe don't worry about it so much right now
        self.skills = ["some major skill", "some other major skill"]

        self.solution = None
        self.correctAnswer = None

    def addQuestion(self, doc = None):
        """
        The table below shows the average yearly balance in a saving account where interest is compounded annulay. No money is deposited or withdrawn after the initial amount is deposited.

        table with YEAR BALANCE,IN DOLLARS
        0,10,20,30,40,50
        etc etc

        Which type of function best models the given data?
        1) exponential growth function
        2) linear function with a positive rate of change
        3) linear function with a negative rate of change
        4) exponential decay function

        year 0 increase by something other than 1
        principal 1000 to 1500
        percent for increase 3%
        P(1+.03)^years
        """
        years = [x for x in range(0,100, random.randint(2,10))]
        principal = random.randint(1000,1501)
        rate = 0.03

        balances = [round(principal*(1.03)**(y),2) for y in years]


        choice1 = "exponential growth function"
        choice2 = "exponential decay function"
        choice3 = "linear function with a positive rate of change"
        choice4 = "linear function with a negative rate of change"

        questionString = "The table below shows the average yearly balance in a saving account where interest is compounded annulay. No money is deposited or withdrawn after the initial amount is deposited."
    
        doc.append(NoEscape(questionString))
        doc.append(NewLine())

        with doc.create(Center()) as centered:
            with centered.create(Tabular("c c")) as tbl:
                header_row = ["Years", "Balance, in dollars"]
                tbl.add_row(header_row, mapper=[bold])
                tbl.add_hline()
                for x in range(5):
                    tbl.add_row([years[x], balances[x]])
                    tbl.add_hline()
        
        doc.append(VerticalSpace("1in"))
        doc.append(NoEscape("Which type of function best models the given data?"))

        self.correctAnswer = multipleChoice(choices = [choice1, choice2, choice3, choice4], doc = doc, math = False)
        
        self.explanation = f"The money is going up, so positive. The money is NOT going up by a constant amount, so exponential"

    def addAnswer(self, doc = None):
        doc.append(f"{self.correctAnswer}")
    
    def addSolution(self, doc = None):
        doc.append(NoEscape(self.explanation))

class June2014_7():
    #Initialize class with info to store in database, then we can dyamically add it to the database
    def __init__(self):
        #ID is topic + MAIN SKILL
        self.subject = "Algebra"
        self.standards = ["some string", "some other string"]
        self.state = "New York"
        self.exam = "June2014"
        self.topics = ["#5Topic", "#6Topic"]
        self.questionNumber = 3
        self.type = "MC"


        self.id = "Algebra.NY.June2014.7"
        #This can get convoluted, so maybe don't worry about it so much right now
        self.skills = ["some major skill", "some other major skill"]

        self.solution = None
        self.correctAnswer = None

    def addQuestion(self, doc = None):
        """
        A company that manufactures radios first pays a start-up cost, and then spends a certain amoun of money to manufacture each radio. If the cost of manufacturing r radios is given by the function c(r) = 5.25r + 125, then the value of 5.25 best represents

        (1) the amount spent to manufacture each radio
        (2) the profit earned to manufacture one radio
        (3) the start-up cost
        (4) the average number of radios manufactured

        rate = random.choice([x/100 for x in range(505, 600, 5)])
        yIntercept = random.randint(100,150)

        items = ["radios", ""] etc
        first letter of thing is variable

        """
        rate = random.choice([x/100 for x in range(505, 600, 5)])
        yIntercept = random.randint(100,150)

        items = ["radios", "toys", "baskets", "alarm clocks"]
        itemPlural = random.choice(items)
        itemSingle = itemPlural[:-1]
        variableName = itemPlural[0]


        choice1 = f"the amount spent to manufacture each {itemSingle}"
        choice2 = f"the profit earned to manufacture one {itemSingle}"
        choice3 = f"the start-up cost"
        choice4 = f"the average number of {itemPlural} manufactured"

        questionString = f"A company that manufactures {itemPlural} first pays a start-up cost, and then spends a certain amoun of money to manufacture each {itemSingle}. If the cost of manufacturing ${variableName}$ {itemPlural} is given by the function $c({variableName}) = {rate}{variableName} + {yIntercept}$, then the value of {rate} best represents"
    
        doc.append(NoEscape(questionString))
        
        self.correctAnswer = multipleChoice(choices = [choice1, choice2, choice3, choice4], doc = doc, math = False)
        
        self.explanation = f"{rate} is next to the variable {variableName}, so it's slope/rate. We want to find words like 'EACH', 'EVERY', 'PER'"

    def addAnswer(self, doc = None):
        doc.append(f"{self.correctAnswer}")
    
    def addSolution(self, doc = None):
        doc.append(NoEscape(self.explanation))

class June2014_8():
    #Initialize class with info to store in database, then we can dyamically add it to the database
    def __init__(self):
        #ID is topic + MAIN SKILL
        self.subject = "Algebra"
        self.standards = ["some string", "some other string"]
        self.state = "New York"
        self.exam = "June2014"
        self.topics = ["#5Topic", "#6Topic"]
        self.questionNumber = 8
        self.type = "MC"


        self.id = "Algebra.NY.June2014.8"
        #This can get convoluted, so maybe don't worry about it so much right now
        self.skills = ["some major skill", "some other major skill"]

        self.solution = None
        self.correctAnswer = None

    def addQuestion(self, doc = None):
        """
        Which equation has the same solution as x^2 - 6x - 12 = 0?
        (1) (x + (b/2))^2 = -C + (b/2)^2
        (2) (x - (b/2))^2 = -C + (b/2)^2
        (3) (x + (b/2))^2 = -C - (b/2)^2
        (4) (x - (b/2))^2 = -C - (b/2)^2
        x^2 - 6x = 12
        x^2 - 6x + (b/2)^2 = 12 + (b/2)^2
        (x - b/2)^2 = 12 + (b/2)^2

        b needs to be even
        c is positive

        """
        b = random.choice([x for x in range(2,17,2)])
        c = -1*random.randint(1,20)

        questionEquation = formatEquation([
            formatExpression([
                {"co":1, "term":"x^2"},
                {"co":b, "term":"x"},
                {"co":c}
            ]),
            "=0"
        ])

        choice1 = formatEquation([
            "(",
            formatExpression([
            {"co": 1, "term": "x"},
            {"co": (b//2)}
            ]),
            ")^{2}=",
            f"{-c+(b//2)**2}"])

        choice2 = formatEquation([
            "(",
            formatExpression([
            {"co":1,"term": "x"},
            {"co": -1*(b//2)}
            ]),
            ")^{2}=",
            f"{-c+(b//2)**2}"]) 

        choice3 = formatEquation([
            "(",
            formatExpression([
            {"co": 1,"term": "x"},
            {"co": 1*(b//2)}
            ]),
            ")^{2}=",
            f"{-c-(b//2)**2}"])

        choice4 = formatEquation([
            "(",
            formatExpression([
            {"co":1,"term": "x"},
            {"co": -1*(b//2)}
            ]),
            ")^{2}=",
            f"{-c-(b//2)**2}"])      

        questionString = f"Which equation has the same solution as ${questionEquation}$?"
    
        doc.append(NoEscape(questionString))
        
        self.correctAnswer = multipleChoice(choices = [choice1, choice2, choice3, choice4], doc = doc, math = True)
        
        self.explanation = f"Move {c} to the other side. Add $({b}/2)^{2}$ to both sides. Factor the left side into a binomial squared"

    def addAnswer(self, doc = None):
        doc.append(f"{self.correctAnswer}")
    
    def addSolution(self, doc = None):
        doc.append(NoEscape(self.explanation))

class June2014_9():
    #Initialize class with info to store in database, then we can dyamically add it to the database
    def __init__(self):
        #ID is topic + MAIN SKILL
        self.subject = "Algebra"
        self.standards = ["some string", "some other string"]
        self.state = "New York"
        self.exam = "June2014"
        self.topics = ["#5Topic", "#6Topic"]
        self.questionNumber = 9
        self.type = "MC"


        self.id = "Algebra.NY.June2014.9"
        #This can get convoluted, so maybe don't worry about it so much right now
        self.skills = ["some major skill", "some other major skill"]

        self.solution = None
        self.correctAnswer = None

    def addQuestion(self, doc = None):
        """
        A ball is thrown into the air from the edge of a {48}-foot-high cliff so that it eventually lands on the ground. The graph below shows the height, {y}, of the ball from the ground after {x} seconds.

        //Graph//
        First quadrant
        -x^2+{48}
        -(x-2.5)^2+{V}={48}

        key aspects: horiztonal shift is directly inbetween integers
        decreasing parabola
        x-axis counts for .5
        y-axis goes up by not 1's


        For which interval is the ball's height always <i>descreasing<i>?
        (1)
        (2)
        (3)
        (4)
        """
        b = random.choice([x for x in range(2,17,2)])
        c = -1*random.randint(1,20)

        questionEquation = formatEquation([
            formatExpression([
                {"co":1, "term":"x^2"},
                {"co":b, "term":"x"},
                {"co":c}
            ]),
            "=0"
        ])

        choice1 = formatEquation([
            "(",
            formatExpression([
            {"co": 1, "term": "x"},
            {"co": (b//2)}
            ]),
            ")^{2}=",
            f"{-c+(b//2)**2}"])

        choice2 = formatEquation([
            "(",
            formatExpression([
            {"co":1,"term": "x"},
            {"co": -1*(b//2)}
            ]),
            ")^{2}=",
            f"{-c+(b//2)**2}"]) 

        choice3 = formatEquation([
            "(",
            formatExpression([
            {"co": 1,"term": "x"},
            {"co": 1*(b//2)}
            ]),
            ")^{2}=",
            f"{-c-(b//2)**2}"])

        choice4 = formatEquation([
            "(",
            formatExpression([
            {"co":1,"term": "x"},
            {"co": -1*(b//2)}
            ]),
            ")^{2}=",
            f"{-c-(b//2)**2}"])      

        questionString = f"Which equation has the same solution as ${questionEquation}$?"
    
        doc.append(NoEscape(questionString))
        
        self.correctAnswer = multipleChoice(choices = [choice1, choice2, choice3, choice4], doc = doc, math = True)
        
        self.explanation = f"Move {c} to the other side. Add $({b}/2)^{2}$ to both sides. Factor the left side into a binomial squared"

    def addAnswer(self, doc = None):
        doc.append(f"{self.correctAnswer}")
    
    def addSolution(self, doc = None):
        doc.append(NoEscape(self.explanation))

questionsAlgebraJune2014Dict = {
    "Algebra.NY.June2014.2": June2014_2,
    "Algebra.NY.June2014.1": June2014_1,
    "Algebra.NY.June2014.3": June2014_3,
    "Algebra.NY.June2014.4": June2014_4,
    "Algebra.NY.June2014.5": June2014_5,
    "Algebra.NY.June2014.6": June2014_6,
    "Algebra.NY.June2014.7": June2014_7,
    "Algebra.NY.June2014.8": June2014_8,
}
