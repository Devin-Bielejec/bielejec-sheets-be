from documentCreation import createPDFsnippet
import sys
import importlib
from pdf2image import convert_from_path
import os

def createSnippet(questionID, questionClass, questionKwargs):
    createPDFsnippet(path="./images/", nameOfDoc=questionID, questionClass=questionClass, questionKwargs = questionKwargs)

    #add kwargs to path
    path = f"{questionID}-"
    for key in questionKwargs:
        path += key + "-" + questionKwargs[key] + "-"

    path = path[:-1]    

    #Convert to image
    pages = convert_from_path(f"./images/{path}.pdf", 500)
    for page in pages:
        page.save(f"./images/{path}.jpg", "JPEG")
    os.remove(f"./images/{path}.pdf")




