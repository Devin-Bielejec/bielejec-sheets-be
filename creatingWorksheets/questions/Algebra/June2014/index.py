import random
import uuid
from pylatex import (Document, TikZ, TikZNode,
                     TikZDraw, TikZCoordinate,
                     TikZUserPath, TikZOptions)

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
        doc.append("Hi")


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
        self.standards = ["some string", "some other string"]
        self.state = "New York"
        self.exam = "June2014"
        self.topics = ["#4Topic", "#3Topic"]
        self.questionNumber = 2
        self.type = "MC"


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
            # add our sample drawings
        with doc.create(TikZ()) as pic:

            # options for our node
            node_kwargs = {'align': 'center',
                        'minimum size': '100pt',
                        'fill': 'black!20'}

            # create our test node
            box = TikZNode(text='My block',
                        handle='box',
                        options=TikZOptions('draw',
                                            'rounded corners',
                                            **node_kwargs))

            # add to tikzpicture
            pic.append(box)

            # draw a few paths
            pic.append(TikZDraw([TikZCoordinate(0, -6),
                                'rectangle',
                                TikZCoordinate(2, -8)],
                                options=TikZOptions(fill='red')))

            # show use of anchor, relative coordinate
            pic.append(TikZDraw([box.west,
                                '--',
                                '++(-1,0)']))

            # demonstrate the use of the with syntax
            with pic.create(TikZDraw()) as path:

                # start at an anchor of the node
                path.append(box.east)

                # necessary here because 'in' is a python keyword
                path_options = {'in': 90, 'out': 0}
                path.append(TikZUserPath('edge',
                                        TikZOptions('-latex', **path_options)))

                path.append(TikZCoordinate(1, 0, relative=True))


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
        doc.append("Hi")


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
