from documentCreation import createPDFsnippet
import sys
import importlib
from pdf2image import convert_from_path
import os

def createSnippet(questionClass, questionKwargs, path):
    createPDFsnippet(path="./images/", nameOfDoc=path, questionClass=questionClass, questionKwargs = questionKwargs)

    #Convert to image
    pages = convert_from_path(f"./images/{path}.pdf", 500)
    for page in pages:
        page.save(f"./images/{path}.jpg", "JPEG")
    os.remove(f"./images/{path}.pdf")




