import random
import uuid

__all__ = ["June2014_1"]

class June2014_1():
    #Initialize class with info to store in database, then we can dyamically add it to the database
    def __init__(self):
        #ID is topic + MAIN SKILL
        self.id = uuid.uuid4()
        self.standard = "some string"
        self.state = "New York"
        self.exam = "some string"
        self.topic = ["some top that majorly applies", "some topic that might also majorly apply"]

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
