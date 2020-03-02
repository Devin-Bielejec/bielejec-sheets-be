#Adding questions to a cache

#Adding those same questions to the database

import sys
import importlib
import json

from questions.Algebra.June2014 import *
from documentCreation import createPDFdocument

questionsDict = {}

def updateQuestionsDict(questionsDict, newDict):
    questionsDict = {**questionsDict, **newDict}
    return questionsDict

questionsDict = updateQuestionsDict(questionsDict, questionsAlgebraJune2014Dict)


#Stuff above is to access the questions

#get questions for sys argv
documentOptions = json.loads(sys.argv[1])
#Testing

questions = []
for questionID in documentOptions["ids"]:
    instance = questionsDict[questionID]()
    questions.append(instance)

createPDFdocument(path="pdfs/", nameOfDoc=documentOptions["nameOfDoc"], questions=questions)
print('done')

#TESTING