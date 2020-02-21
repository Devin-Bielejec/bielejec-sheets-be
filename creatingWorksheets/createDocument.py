#Adding questions to a cache

#Adding those same questions to the database

import sys
import importlib

from questions.Algebra.June2014 import *

questionsDict = {}

def updateQuestionsDict(questionsDict, newDict):
    questionsDict = {**questionsDict, **newDict}
    return questionsDict

questionsDict = updateQuestionsDict(questionsDict, questionsAlgebraJune2014Dict)

questionsList = []
for key in questionsDict:
    instance = questionsDict[key]()

    questionList.append({"id": instance.id})

print(questionsList)