#Adding questions to a cache

#Adding those same questions to the database

import sys
import importlib
import json
from questions.Algebra.June2014 import *

questionsDict = {}

def updateQuestionsDict(questionsDict, newDict):
    questionsDict = {**questionsDict, **newDict}
    return questionsDict

questionsDict = updateQuestionsDict(questionsDict, questionsAlgebraJune2014Dict)

questionsList = []

#each key is an id for the classes
for key in questionsDict:
    instanceOfClass = questionsDict[key]()
    currentListToAdd = []
    #in our seed file, we'll specifiy the attributes we need for the particular table
    for arg in sys.argv[1:]:    
        #Get value of property from the class
        instanceOfClassProperty = getattr(instanceOfClass, arg)
        
        #spread in current list into templist
        tempList = [*currentListToAdd]
        
        #Reset current list to empty, so we can add items to it
        currentListToAdd = []    

        for curDict in tempList or [{}]:
            if type(instanceOfClassProperty) == list:
                for item in instanceOfClassProperty:
                    #we have to remove last name of argument, so we get TOPIC instead of TOPIC(S) - no s                    
                    currentListToAdd.append({**curDict, **{arg[:-1]: item}})    
            else:
                #Add property to each dictionary already exisiting
                currentListToAdd.append({**curDict, **{arg: instanceOfClassProperty}})

    #For each of the class questions, we're spreading in the objects that we need
    questionsList = [*questionsList, *currentListToAdd]

questionsList = json.dumps(questionsList)
print(questionsList)
