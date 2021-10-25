import sys
from fractions import gcd, Fraction
sys.path.insert(0, "F:/code/bielejec-sheets-be/creatingWorksheets/utils")
from utils.equations import formatMathString, toLatexFraction, randomBetweenNot
from utils.shapes import triangleCoordinates
from utils.pdfFunctions import annotatePolygon
from utils.transformations import translation
import math
import string
import random

class _12():
    def __init__(self, xyChange = "++", overlap = False, prime = True, algebraic = False):
        self.kwargs = {
            "xyChange": ["0+", "0-", "+0", "-0", "++", "+-", "--", "-+"],
            "overlap": False,
            "prime": True,
            "algebraic": False
        }

        self.toolTips = {
            "xyChange": "Amount of x Change followed by amount of y change",
            "overlap": "Will Overlap",
            "prime": "Prime Notation",
            "algebraic": "Algebraic Notation"}

        xChangeAmount = xyChange[0]
        yChangeAmount = xyChange[1]

        graphFactor = 10
        
        xMinGraph = -graphFactor
        xMaxGraph = graphFactor
        yMinGraph = -graphFactor
        yMaxGraph = graphFactor

        polygonTypeChosen = "right triangle"
        polygonSizeChosen = "small"

        x, y = triangleCoordinates()

        x, y, newX, newY, xTransVal, yTransVal = translation(xMinGraph = xMinGraph, xMaxGraph = xMaxGraph, yMinGraph = yMinGraph, yMaxGraph = yMaxGraph, xChangeAmount = xChangeAmount, yChangeAmount = yChangeAmount, overlap = overlap, x = x, y = y)

        ABC, DEF, blah = annotatePolygon(vertices = len(x), prime = prime)
        shapeName = ''
        for letter in [ABC[x] for x in range(0, len(x))]:
            shapeName += letter
        shapeName2 = ''
        for letter in [DEF[x] for x in range(0, len(x))]:
            shapeName2 += letter

        #graph polygon
        if xTransVal < 0:
            transXString = '%d left' % abs(xTransVal)
            transXStringA = '(x-%d,' % abs(xTransVal)
        elif xTransVal > 0:
            transXString = '%d right' % abs(xTransVal)
            transXStringA = '(x+%d,' % abs(xTransVal)
        else:
            transXString = ''
            transXStringA = '(x,'

        if yTransVal < 0:
            transYString = '%d down' % abs(yTransVal)
            transYStringA = 'y-%d)' % abs(yTransVal)
        elif yTransVal > 0:
            transYString = '%d up' % abs(yTransVal)
            transYStringA = 'y+%d)' % abs(yTransVal)
        else:
            transYString = ''
            transYStringA = 'y)'

        if algebraic:
            transString = r'${(x,y)\rightarrow%s}$' % (transXStringA+transYStringA) 
        else:
            if xTransVal == 0:
                transString = transYString
            elif yTransVal == 0:
                transString = transXString
            else:
                transString = transXString + ' and ' + transYString
        self.directions = "Perform the translations: "

        questionString = fr'Given {polygonTypeChosen} ${shapeName}$, graph {polygonTypeChosen} ${shapeName2}$ after a translation {transString}.'

        self.question = [{"text": questionString}, {"graph": {"grid": True, "annotations": [ABC[0], ABC[1], ABC[2]], "x": x, "y": y, "color": "black"}}]

        self.duplicateCheck = f"xmingraph{xMinGraph}xMaxGraph{xMaxGraph}yminGraph{yMinGraph}yMaxGraph{yMaxGraph}{x}{y}{newX}{newY}"

        self.answer = [{"graph": {"grid": True, "annotations": [ABC[0], ABC[1], ABC[2]], "x": x, "y": y, "color": "black"}},{"graph": {"grid": True, "annotations": [DEF[0], DEF[1], DEF[2]], "x": x, "y": y, "color": "red"}}]
		
        

