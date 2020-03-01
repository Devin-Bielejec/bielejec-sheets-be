class Template():
    #Initialize class with info to store in database, then we can dyamically add it to the database
    def __init__(self):
        #ID is topic + MAIN SKILL
        self.ID = "Randomly generated from SQL DB"
        self.standard = "some string"
        self.state = "New York"
        self.exam = "some string"
        self.topic = ["some top that majorly applies", "some topic that might also majorly apply"]

        #This can get convoluted, so maybe don't worry about it so much right now
        self.skills = ["some major skill", "some other major skill"]
    
    def addQuestion(self, doc = None):
        #Junk here where you add to the document

    def addAnswer(self, doc = None):
        #Junk here where you add to the document

    def addSolution(self, doc = None):
        #Junk here where you would add to the solution

