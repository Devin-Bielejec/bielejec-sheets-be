import sys
import importlib
import json
import inspect

sys.path.append('../')
from questions.Algebra.Quadratics import quadraticsQuestionsDict
from documentCreation import createPDFdocument

def updateQuestionsDict(questionsDict, newDict):
    questionsDict = {**questionsDict, **newDict}
    return questionsDict

questionsDict = {}
questionsDict = updateQuestionsDict(questionsDict, quadraticsQuestionsDict)


#Stuff above is to access the questions

#get questions for sys argv - for real
# documentOptions = json.loads(sys.argv[1])

newQuestions = []
for item in list(questionsDict.keys()):
    for n in range(10):
        newQuestions.append(item)

#Testing BELOW
documentOptions = {"ids": newQuestions, "nameOfDoc": "Tickles"}
questions = []
for questionID in documentOptions["ids"]:
    instance = questionsDict[questionID]()
    questions.append(instance)

createPDFdocument(path="pdfs/", nameOfDoc=documentOptions["nameOfDoc"], questions=questions, answers = True)
print('done testing')


#Testing^^^^

# questions = []
# for questionID in documentOptions["ids"]:
#     instance = questionsDict[questionID]()
#     questions.append(instance)

# createPDFdocument(path="./creatingWorksheets/pdfs/", nameOfDoc=documentOptions["nameOfDoc"], questions=questions)


