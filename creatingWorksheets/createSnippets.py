from documentCreation import createPDFsnippet
import sys
import importlib
#import specific questions from whatever module you just finished
from questions.Algebra.June2014 import *
from pdf2image import convert_from_path
import os

questionsDict = {}

def updateQuestionsDict(questionsDict, newDict):
    questionsDict = {**questionsDict, **newDict}
    return questionsDict

questionsDict = updateQuestionsDict(questionsDict, questionsAlgebraJune2014Dict)

print(questionsDict)
for key in questionsDict:
    print(key)
    instance = questionsDict[key]()

    createPDFsnippet(path="./images/", nameOfDoc=key, questions=[instance])

    #Convert to image
    pages = convert_from_path(f"./images/{key}.pdf", 500)
    for page in pages:
        page.save(f"./images/{key}.jpg", "JPEG")
    os.remove(f"./images/{key}.pdf")


