import sys
from fractions import Fraction
sys.path.insert(0, "./creatingWorksheets/utils")
from utils.equations import formatMathString, toLatexFraction, randomBetweenNot
from utils.shapes import triangleCoordinates
from utils.pdfFunctions import annotatePolygon
from utils.transformations import rotation
import math
import string
import random

class _14():
    def __init__(self, prime = True, center = "origin", variation = "90 cw", overlap = False):
        self.kwargs = {
            "prime": True,
            "overlap": False,
            "center": ["origin", "other"],
            "variation": ["90 cw", "90 ccw", "180"]
        }

        self.toolTips = {
            "overlap": "Will Overlap",
            "prime": "Prime Notation",
            "center": "Center point of rotation",
            "variation": "Degrees and direction of rotation"
        }

        if variation == "90 cw":
            degrees = 90
            direction = "clockwise"
        elif variation == "90 ccw":
            degrees = 90
            direction = "counterclockwise"
        else:
            degrees = 180

        graphFactor = 10
        
        xMinGraph = -graphFactor
        xMaxGraph = graphFactor
        yMinGraph = -graphFactor
        yMaxGraph = graphFactor

        polygonTypeChosen = "right triangle"
        polygonSizeChosen = "small"

        x, y = triangleCoordinates()

        x, y, rotX, rotY, center, degrees, direction = rotation(center = center, overlap = overlap, degrees = degrees, direction =direction, x = x, y = y)

        ABC, DEF, blah = annotatePolygon(vertices = len(x), prime = prime)
        shapeName = ''
        for letter in [ABC[x] for x in range(0, len(x))]:
            shapeName += letter
        shapeName2 = ''
        for letter in [DEF[x] for x in range(0, len(x))]:
            shapeName2 += letter
        
        if center == [0,0]:
            centerString = "the origin"
        else:
            centerString = rf"the point $({center[0]},{center[1]})$"

        questionString = fr'Given $\bigtriangleup {shapeName}$ on the set of axes below, graph $\bigtriangleup {shapeName2}$ after a rotation of ${degrees}^\circ$ {direction} around {centerString}.'
        
        self.directions = "Perform the rotation: "

        self.question = [{"text": questionString}, {"graph": {"grid": True, "annotations": [ABC[0], ABC[1], ABC[2]], "x": x, "y": y, "color": "black"}}]

        self.duplicateCheck = f"xmingraph{xMinGraph}xMaxGraph{xMaxGraph}yminGraph{yMinGraph}yMaxGraph{yMaxGraph}{x}{y}{rotX}{rotY}"

        self.answer = [{"graph": {"grid": True, "annotations": [ABC[0], ABC[1], ABC[2]], "x": x, "y": y, "color": "black"}},{"graph": {"grid": True, "annotations": [DEF[0], DEF[1], DEF[2]], "x": x, "y": y, "color": "red"}}]
		
        

