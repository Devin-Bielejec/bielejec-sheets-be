import random
import uuid
from pylatex import (Document, TikZ, TikZNode,
                     TikZDraw, TikZCoordinate,
                     TikZUserPath, TikZOptions, VerticalSpace, NewLine)
from pylatex.utils import (NoEscape)
import sys
sys.path.insert(0, "creatingWorksheets/utils")
from questionFormatting import multipleChoice
import string

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
        equation1 = rf"${a}({b}x^{2}+{c})-{d}={e}x^{2}+{f}$"
        equation2 = rf"${a}({b}x^{2}+{c})={e}x^{2}+{f+d}$"
        
        wholeString = f"When solving the equation {equation1}, {name} wrote {equation2}, as their first step. Which property justifies {name}'s first step"

        #Choice 1 is always correct answer
        choice1 = "Addition property of equality"
        choice2 = "Commutative property of equality"
        choice3 = "Multiplication property of equality"
        choice4 = "Distributive property of equality"

        #Adds question
        doc.append(NoEscape(wholeString))

        #Adds choices - returns correct answer
        self.correctAnswer = multipleChoice(choices = [choice1, choice2, choice3, choice4], doc = doc)
        self.solution = f"Starting with: {equation1}, we add {d} (+{d}) to both sides. This gives us {equation2}. Since we added, it is Addition Property of Equality."

    def addAnswer(self, doc = None):
        doc.append(NoEscape(self.correctAnswer))
        pass
    
    def addSolution(self, doc = None):
        doc.append(NoEscape(self.solution))
        pass
        #Junk here where you would add to the solution

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
                string = "{..."
            else:
                string = "{"
            for val in values:
                string += f"{val}, "
            #now there is a comma and space left over
            if continuousBack:
                string[-2] = "...}"
            else:
                string[-2] = "}"
            return string

        #correct answer, which is actually choice 4
        choice1List = [x for x in range(0, random.randint(4,6))]
        choice1 = setNotationList(choice1List, continuousBack = True, continuousFront = True)
        
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
            if count == 0:
                break
            for numerator in range(denominator):
                #0 + 0, 0 + 1/4, 0 + 2/4, 0 + 3/4 etc 
                if count == 0:
                    break
                if wholeNumber == 0 and numerator != 0:
                    #single fractions
                    choice4List.append(f"$\frac{numerator}{denominator}$")
                elif numerator == 0:
                    #just do the whole number then
                    choice4List.append(f"{wholeNumber}")
                else:
                    #mixed number
                    choice4List.append(f"{wholeNumber}$\frac{numerator}{denominator}$")
                count += 1

        choice4 = setNotationList(choice4List, continuousFront = True)
        
        functionName = random.choice(string.ascii_uppercase))
        variableName = random.choice([x for x in string.ascii_lowercase if x.isUpper() != functionName]))

        questionString = f"Officials in a town use a function, {functionName}, to analyze traffic patterns.
        {functionName}({variableName}) represents the rate of traffic through an intersection where
        {variableName} is the number of observed vehicles in a specified time interval.
        What would be the most appropriate domain for the function?"
        
        doc.append(questionString)
        doc.append(NewLine())
        doc.append(VerticalSpace('.05in'))
        self.correctAnswer = multipleChoice(choices = [choice1, choice2, choice3, choice4], doc = doc)
        self.solution = f"The function {functionName}({variableName}) represents vehicles, which can only be whole numbers including 0. Also the '...' at the end means that there will be more cars coming."


    def addAnswer(self, doc = None):
        doc.append(NoEscape(self.correctAnswer))
        pass
    
    def addSolution(self, doc = None):
        doc.append(NoEscape(self.solution))
        pass
        #Junk here where you would add to the solution

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

    def addQuestion(self, doc = None):
        #Junk here where you add to the document
        """
        When solving the equation A(Bx^2 + C) - D = Ex^2 + F, {name} wrote A(Bx^2 + C) = Ex^2 + F + D as her first step. Which property justifies {name}'s first step?
        A -> random numbeer between 2, 9
        B -> random number between 2, 9
        """
        a = random.randint(2,9)
        b = random.randint(2,9)
        c = random.randint(2,9)
        d = random.randint(2,9)
        e = random.randint(2,9)
        f = random.randint(2,9)
        
        name = random.choice(["Emily", "David", "Jakim", "Joe", "John"])

        #Let's see if it works without anything in particular
        equationString = rf"{a}(x^{2}+{c})-{d}={e}x^{2}"
        doc.append("Hid from you")


    def addAnswer(self, doc = None):
        #Junk here where you add to the document
        pass
    
    def addSolution(self, doc = None):
        pass
        #Junk here where you would add to the solution

questionsAlgebraJune2014Dict = {
    "Algebra.NY.June2014.2": June2014_2,
    "Algebra.NY.June2014.1": June2014_1,
    "Algebra.NY.June2014.3": June2014_3
}
