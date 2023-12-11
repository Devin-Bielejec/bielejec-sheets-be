import sys
from fractions import Fraction
sys.path.insert(0, "./creatingWorksheets/utils")
from utils.equations import formatMathString, toLatexFraction, randomBetweenNot
from utils.shapes import triangleCoordinates
from utils.pdfFunctions import annotatePolygon
from utils.transformations import reflection
import math
import string
import random

class _13():
    def __init__(self, line = "x=not0",overlap = False, prime = True):
        self.kwargs = {
            "overlap": False,
            "prime": True,
            "line": ['x=not0','y=not0','yaxis','xaxis','x=0','y=0']
        }

        self.toolTips = {
            "overlap": "Will Overlap",
            "prime": "Prime Notation",
            "line": "Line to relfect over"
        }
        graphFactor = 10
        
        xMinGraph = -graphFactor
        xMaxGraph = graphFactor
        yMinGraph = -graphFactor
        yMaxGraph = graphFactor

        polygonTypeChosen = "right triangle"
        polygonSizeChosen = "small"

        x, y = triangleCoordinates()

        x, y, rX, rY, refVal, refValString = reflection(nameOfReflection=line, overlap = overlap, x = x, y = y)

        ABC, DEF, blah = annotatePolygon(vertices = len(x), prime = prime)
        shapeName = ''
        for letter in [ABC[x] for x in range(0, len(x))]:
            shapeName += letter
        shapeName2 = ''
        for letter in [DEF[x] for x in range(0, len(x))]:
            shapeName2 += letter

        questionString = rf'Given $\bigtriangleup {shapeName}$ on the set of axes below, graph $\bigtriangleup {shapeName2}$ after a reflection over the {refValString}'#graph polygon
        
        self.directions = "Perform the reflection: "

        
        self.question = [{"text": questionString}, {"graph": {"grid": True, "annotations": [ABC[0], ABC[1], ABC[2]], "x": x, "y": y, "color": "black"}}]

        self.duplicateCheck = f"xmingraph{xMinGraph}xMaxGraph{xMaxGraph}yminGraph{yMinGraph}yMaxGraph{yMaxGraph}{x}{y}{rX}{rY}"

        self.answer = [{"graph": {"grid": True, "annotations": [ABC[0], ABC[1], ABC[2]], "x": x, "y": y, "color": "black"}},{"graph": {"grid": True, "annotations": [DEF[0], DEF[1], DEF[2]], "x": x, "y": y, "color": "red"}}]
		
        

