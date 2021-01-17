import sys
import importlib
import json
import inspect

sys.path.append('../')
from questions.Algebra.Quadratics import quadraticsQuestionsDict
from documentCreation import createWorksheet, createAssessment

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
    if item == "June14Q8":
        for n in range(20):
            newQuestions.append(item)

#Testing BELOW
documentOptions = {"ids": newQuestions, "nameOfDoc": "Quadratics-Completing The Square Easy"}
questions = []

#Testing for duplicates
hash = {}
for questionID in documentOptions["ids"]:
    print(questionID)
    duplicate = True
    loop = 0
    while duplicate:
        loop += 1
        if loop == 100:
            break
        instance = questionsDict[questionID]()

        if instance.worksheetQuestion+questionID not in hash:
            hash[instance.worksheetQuestion+questionID] = True
            questions.append(instance)
            duplicate = False

createWorksheet(path="pdfs/", nameOfDoc=documentOptions["nameOfDoc"], questions=questions, answers = True)
print('done testing')


#Testing^^^^

# questions = []
# for questionID in documentOptions["ids"]:
#     instance = questionsDict[questionID]()
#     questions.append(instance)

# createPDFdocument(path="./creatingWorksheets/pdfs/", nameOfDoc=documentOptions["nameOfDoc"], questions=questions)


