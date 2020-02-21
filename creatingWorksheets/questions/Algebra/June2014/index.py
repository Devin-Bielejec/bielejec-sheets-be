import random
import uuid

# __all__ = ["June2014_1", "June2014_12"]

class June2014_1():
    #Initialize class with info to store in database, then we can dyamically add it to the database
    def __init__(self):
        #ID is topic + MAIN SKILL
        self.subject = "Algebra"
        self.standard = "some string"
        self.state = "New York"
        self.exam = "June2014"
        self.topics = ["#1Topic", "#2Topic"]
        self.questionNumber = 1

        self.id = "Algebra.NY.June2014.1"
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


    def addAnswer(self, doc = None):
        #Junk here where you add to the document
        pass
    
    def addSolution(self, doc = None):
        pass
        #Junk here where you would add to the solution

class June2014_2():
    #Initialize class with info to store in database, then we can dyamically add it to the database
    def __init__(self):
        #ID is topic + MAIN SKILL
        self.subject = "Algebra"
        self.standard = "some string"
        self.state = "New York"
        self.exam = "June2014"
        self.topics = ["#4Topic", "#3Topic"]
        self.questionNumber = 2

        self.id = "Algebra.NY.June2014.2"
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


    def addAnswer(self, doc = None):
        #Junk here where you add to the document
        pass
    
    def addSolution(self, doc = None):
        pass
        #Junk here where you would add to the solution

class June2014_3():
    #Initialize class with info to store in database, then we can dyamically add it to the database
    def __init__(self):
        #ID is topic + MAIN SKILL
        self.subject = "Algebra"
        self.standard = "some string"
        self.state = "New York"
        self.exam = "June2014"
        self.topics = ["#5Topic", "#6Topic"]
        self.questionNumber = 3

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
