from documentCreation import createPDFsnippet
import sys
import importlib
from pdf2image import convert_from_path
import os


import sys
sys.path.append('../')

from creatingWorksheets.questions.Algebra import questionsDict

def createSnippet(questionID, questionClass, questionKwargs):
    createPDFsnippet(path="./images/", nameOfDoc=questionID, questionClass=questionClass, questionKwargs = questionKwargs)

    #Convert to image
    pages = convert_from_path(f"./images/{questionID}.pdf", 500)
    for page in pages:
        page.save(f"./images/{questionID}.jpg", "JPEG")
    os.remove(f"./images/{questionID}.pdf")

for key in questionsDict:
    i = questionsDict[key]()

    createSnippet(i.id, questionsDict[key], {})


