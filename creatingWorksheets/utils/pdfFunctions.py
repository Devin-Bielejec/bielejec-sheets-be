from pylatex.base_classes import Environment, CommandBase, Arguments
from pylatex.package import Package
from pylatex import Document, Section, UnsafeCommand, TikZ, Command, Figure, VerticalSpace, NewPage, NewLine, SubFigure, HorizontalSpace, Center, Package
from pylatex import Document, PageStyle, Head, MiniPage, Foot, LargeText, MediumText, LineBreak, simple_page_number
import math
from pylatex.utils import NoEscape, escape_latex
import time
import random
from fractions import Fraction
import sys
sys.path.insert(0, '/home/devin/webapp/devins_project/Polygon')
from utils.PolygonClasses import Shape, Point
from utils.LabelPolygon import CalcAndReturnLabelCoordsAsLists

def circle(center, radius, label, options):
    options = str(options)
    center = str(center)
    radius = str(radius)
    label = str(label)
    doc.append(Command('draw[%s] %s node {%s} circle (%s);' % (options, center, label, radius)))
def grid(doc, xMin = -10, xMax = 10, yMin = -10, yMax = 10, axes = True, gridLines = True):  # always do square
    if gridLines == True:
        doc.append(Command('draw[thin,gray,step=1] (%d,%d) grid (%d,%d);' % (xMin, yMin, xMax, yMax)))
        #Grid
    if axes == True:
        doc.append(Command('draw[line width=.8, black, <->] (%g,0) -- (%g,0);' % (xMin - .5, xMax + .5)))
        #x-axis

        doc.append(Command('draw (%d,0) node {x};' % (xMax + 1)))
        #x axes label

        doc.append(Command('draw[line width=.8, black, <->] (0,%g) -- (0,%g);' % (yMin - .5, yMax + .5)))
        #y-axis

        doc.append(Command('draw (0,%d) node {y};' % (yMax + 1)))
        #y-axis label
def com(stuff, doc = None):
    if doc != None:
        doc.append(Command(stuff + ';'))

def sizingXY(minn, maxx, size):  # small, medium, large
    lengthOfGrid = maxx - minn
    # 8.5 x 11 = 21.59cm x 2.94cm subtract margins = 7.5 x 9.5 = 19.05cm x 24.13
    # small = 1/5 of whole width/length
    # medium = 2/5 of whole width/length
    # large = 3/5 of whole width/length
    squareLength = 2*maxx
    if size == 'small':
        squareLength = 1 / 5 * 19.05  # for now we're going to do square pictures, we can do rectangles in the future
    elif size == 'medium':
        squareLength = 2 / 5 * 19.05
    elif size == 'large':
        squareLength = 3 / 5 * 19.05
    xyLength = squareLength / lengthOfGrid
    return xyLength
def annotatePolygon(prime, vertices):
    import random

    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "O", "P", "R", "S", "T", "U", "V", "W",
               "X", "Y", "Z"]

    polygonName1 = []

    one = random.choice(letters)
    letters.remove(one)
    two = random.choice(letters)
    letters.remove(two)
    three = random.choice(letters)
    letters.remove(three)
    four = random.choice(letters)
    letters.remove(four)

    polygonName2 = []

    one2 = random.choice(letters)
    letters.remove(one2)
    two2 = random.choice(letters)
    letters.remove(two2)
    three2 = random.choice(letters)
    letters.remove(three2)
    four2 = random.choice(letters)
    letters.remove(four2)

    polygonName3 = []

    one3 = random.choice(letters)
    letters.remove(one3)
    two3 = random.choice(letters)
    letters.remove(two3)
    three3 = random.choice(letters)
    letters.remove(three3)
    four3 = random.choice(letters)
    letters.remove(four3)
    if vertices == 1:
        polygonName = [one]
    if vertices == 2:
        polygonName = [one, two]
    if vertices == 3:  # suitable for now
        polygonName = [one, two, three]
        if prime == True:
            polygonNamePrime = [one + '^{\prime}', two + '^{\prime}', three + '^{\prime}']
            polygonNameDoublePrime = [one + '^{\prime\prime}', two + '^{\prime\prime}', three + '^{\prime\prime}']
        if prime == False:
            polygonName1 = [one, two, three]
            polygonName2 = [one2, two2, three2]
            polygonName3 = [one3, two3, three3]
    if vertices == 4:
        polygonName = [one, two, three, four]
        polygonName2 = [one2, two2, three2, four2]
        polygonName3 = [one3, two3, three3, four3]
        if prime == True:
            polygonNamePrime = [one + '^{\prime}', two + '^{\prime}', three + '^{\prime}', four + '^{\prime}']
            polygonNameDoublePrime = [one + '^{\prime\prime}', two + '^{\prime\prime}', three + '^{\prime\prime}', four + '^{\prime\prime}']
    if prime == True:
        return polygonName, polygonNamePrime, polygonNameDoublePrime
    if prime == False:
        return polygonName, polygonName2, polygonName3

def pointsForDiagram():
    import random

    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "O", "P", "R", "S", "T", "U", "V", "W",
               "X", "Y", "Z"]

    lettersRandom = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "O", "P", "R", "S", "T", "U", "V", "W",
               "X", "Y", "Z"]
    random.shuffle(lettersRandom)
    pointsDict = {}

    for key, item in zip(letters, lettersRandom):
        pointsDict[key] = item
    return pointsDict
def polygon(minn, maxx, type, size):
    if size == 'smaller':
        maxAmount = (maxx - 1) // 3
    elif size == 'regular':
        maxAmount = (maxx - 1) // 2

    if type == 'scalene triangle':
        optionsX = list(range(-maxAmount, maxAmount + 1))
        optionsY = list(range(-maxAmount, maxAmount + 1))
        x1 = 0
        y1 = 0

        # eliminate 1 length triangles, two is the smallest
        optionsX.remove(-1)
        optionsX.remove(1)
        optionsY.remove(-1)
        optionsY.remove(1)

        x2 = random.choice(optionsX)
        if x2 == 0:  # so that x2 and y2 are not the same as x1 and y1
            optionsY.remove(0)
        y2 = random.choice(optionsY)

        if x2 in optionsX:
            optionsX.remove(x2)
        if y2 in optionsY:
            optionsY.remove(y2)

        # now we're going to remove items from optiosn that are within less than half the length of x or y
        stuffX = optionsX
        stuffY = optionsY

        for ox in optionsX:
            xDist = abs(x2 - x1)
            if x2 - xDist // 2 - 1 <= ox <= x2 + xDist // 2 + 1:
                stuffX.remove(ox)

        for oy in optionsY:
            yDist = abs(y2 - y1)
            if y2 - yDist // 2 - 1 <= oy <= y2 + yDist // 2 + 1:
                stuffY.remove(oy)
        x3 = random.choice(stuffX)
        y3 = random.choice(stuffY)

        xs = [x1, x2, x3]
        ys = [y1, y2, y3]
        return xs, ys
    elif type == 'right triangle':
        optionsXY = []
        minnMaxx = list(range(-maxAmount, maxAmount + 1))
        for x in minnMaxx:
            for y in minnMaxx:
                optionsXY.append([x, y])

        x1 = 0
        y1 = 0

        # eliminate 1 length triangles, two is the smallest
        optionsXY.remove([0, 1])
        optionsXY.remove([-1, 1])
        optionsXY.remove([-1, 0])
        optionsXY.remove([-1, -1])
        optionsXY.remove([0, -1])
        optionsXY.remove([1, -1])
        optionsXY.remove([1, 0])
        optionsXY.remove([1, 1])

        optionsXY.remove([x1, y1])

        choice2 = random.choice(optionsXY)
        x2 = choice2[0]
        y2 = choice2[1]

        optionsXY.remove(choice2)

        # rotate this line 90 cc or 90 ccw around either x2y2, or x1y1
        rotateOption = random.randint(1, 2)
        if rotateOption == 1:  # totate around 00 cc
            x3 = -y2
            y3 = x2
        elif rotateOption == 2:
            x3 = y2
            y3 = -x2
        elif rotateOption == 3:  # something's wrong...
            x3 = -(y1 - y2) + y2
            y3 = (x1 - x2) + x2
        elif rotateOption == 4:  # and here too
            x3 = (y1 - y2) + y2
            y3 = -(x1 - x2) + x2
        xs = [x1, x2, x3]
        ys = [y1, y2, y3]
        return xs, ys
def pointTriangle(center, P, A, B, C):
    import numpy

    v0 = numpy.subtract(C, A)
    v1 = numpy.subtract(B, A)
    v2 = numpy.subtract(P, A)

    dot00 = numpy.dot(v0, v0)
    dot01 = numpy.dot(v0, v1)
    dot02 = numpy.dot(v0, v2)
    dot11 = numpy.dot(v1, v1)
    dot12 = numpy.dot(v1, v2)

    invDenom = 1 / (dot00 * dot11 - dot01 * dot01)
    u = (dot11 * dot02 - dot01 * dot12) * invDenom
    v = (dot00 * dot12 - dot01 * dot02) * invDenom

    if ((u > 0) and (v > 0) and (u + v < 1)) == True:  # > < inside,
        if center == 'inside':
            return True
        else:
            return False
    elif ((u >= 0) and (v >= 0) and (u + v < 1)) == False:
        if center == 'outside':
            return True
        else:
            return False
    else:
        if center == 'on':
            return True
        else:
            return False
def getAnnotatedCoordinates(x = [1,2,3], y = [3,2,1], distanceAway = 1):
    #loop through each vertex (1,2,3) in this example
    #use coordinates on either side of verex (so consecutive)
    #average their y values and x values
    #then do their average - the given coordinate, so
    #itemX-averageX, and same with y's
    #then have a distance away from point
    #find my slope?
    #distance = ()**(1/2)
    #slope is a/b as fraction
    #find angle of right triangle that slope a/b would make
    #atan(a/b) = angle
    #a should be sin(angle)*dist, then make b whatever it should be
    #then add the current x and y points to their respecitve etc
    annoX = []
    annoY = []
    for indexItem in range(0, len(x)):
        print(len(x))
        print([x for x in range(0,len(x))])
        if indexItem == 0:
            previousX = x[len(x)-1]
            previousY = y[len(x)-1]
            nextX = x[indexItem+1]
            nextY = y[indexItem+1]
        elif indexItem == len(x)-1:
            previousX = x[len(x)-1]
            previousY = y[len(x)-1]
            nextX = x[0]
            nextY = y[0]
        else:
            previousX = x[indexItem-1]
            previousY = y[indexItem-1]
            nextX = x[indexItem+1]
            nextY = y[indexItem+1]

        avgX = (previousX+nextX)/2
        avgY = (previousY+nextY)/2

        xChange = x[indexItem]-avgX
        yChange = y[indexItem]-avgY
        if yChange == 0:
            yChange = -.01
        if xChange == 0:
            xChange = -.01

        if xChange == 0:
            annoX.append(x[indexItem])
            yChangeScaled = distanceAway*(yChange/abs(yChange))
            annoY.append(y[indexItem]+yChangeScaled)
        elif yChange == 0:
            annoY.append(y[indexItem])
            xChangeScaled = distanceAway*(xChange/abs(xChange))
            annoX.append(x[indexItem]+xChangeScaled)
        else:
            angle = math.atan(abs(yChange)/abs(xChange))
            yChangeScaled = math.sin(angle)*distanceAway*(yChange/abs(yChange))
            #yChangeScaled/yChange is how much xChange needs to multiply by
            xChangeScaled = xChange*(yChangeScaled/yChange)

            annoX.append(x[indexItem]+xChangeScaled)
            annoY.append(y[indexItem]+yChangeScaled)

    return annoX, annoY
def makeShapeObjectFromPoints(x, y):
    listOfPoints = []
    for itemX, itemY in zip(x, y):
        listOfPoints.append(Point(itemX, itemY))
    shape = Shape(listOfPoints)
    return shape

def graphPolygon(doc = None, x = [], y = [], annotations = [], color = 'black', distanceAway = .75):
    #function I was using to create a polygon before.
    if doc == None:
        print('NO DOC FOR GRAPH POLYGON')

    #START OF DRAWING POLYGON
    string = 'draw[line width = 1, %s]' % color #options for drawing

    for itemX, itemY in zip(x,y):
        string += ' (%g,%g) --' % (itemX, itemY) #draws from point to point.
        #com(doc, r'node [fill=white]  at (%g,%g) {$%s$}' % (itemX, itemY, n))
        
    string += ' cycle' #cycle back to first point.
    doc.append(Command(string+';'))
    #END OF DRAWING POLYGON

    if len(annotations) != 0:
        #START OF LABELING POLYGON
        annoX, annoY = getAnnotatedCoordinates(x = x, y = y, distanceAway = distanceAway )

        for itemX, itemY, n in zip(annoX, annoY, annotations):
            doc.append(Command(r'node at (%g,%g) {$%s$};' % (itemX, itemY, n)))

        #END OF LABELING POLYGON

def graphPoint(doc = None, x = [], y = [], annotations = [], color = 'black', distanceAway = .75):
    #function I was using to create a polygon before.
    if doc == None:
        print('NO DOC FOR GRAPH POLYGON')

    #START OF DRAWING POLYGON
    string = 'draw[black,fill=black] (%d,%d) circle (.5ex)' % (x, y)

    doc.append(Command(string+';'))
    #END OF DRAWING POLYGON

    doc.append(Command(r'node at (%g,%g) {$%s$};' % (x+distanceAway, y, annotations[0])))

        #END OF LABELING POLYGON
def graphAngle(x, y, nodes):
    import random
    minX = min(x)
    minY = min(y)
    maxX = max(x)
    maxY = max(y)

    string = 'draw[line width = 1.5]'
    counter = 0
    for itemX, itemY in zip(x, y):
        counter += 1
        print(counter)
        if counter > 2:
            string += ' (%d,%d);' % (itemX, itemY)
        else:
            string += ' (%d,%d) --' % (itemX, itemY)

    for itemX, itemY, itemN in zip(x, y, nodes):
        realXNodes = []
        realYNodes = []

        xTries = [1, 0, -1, -1, -1, 0, 1, 1]  # maybe eliminate some of these when axes are in play..??????
        yTries = [-1, -1, -1, 0, 1, 1, 1,
                  0]  # once this works, we can roll through corner pieces first as they will probably be more likely
        dist = .5

        for xT, yT in zip(xTries, yTries):
            xNode = itemX + dist * xT
            yNode = itemY + dist * yT

            p = [xNode, yNode]
            a = [x[0], y[0]]
            b = [x[1], y[1]]
            c = [x[2], y[2]]

            if pointTriangle('outside', p, a, b, c) == True:
                realXNodes.append(xNode)
                realYNodes.append(yNode)
                # could have it end here but would rather have multiple points
        xNode = random.choice(realXNodes)
        yNode = random.choice(realYNodes)
        com('node at (%g,%g) {%s}' % (xNode, yNode, itemN))
    com(string)
def graphLine(x, y, nodes):
    import random

    string = 'draw[line width = 1.5]'
    string += ' (%d,%d) -- (%d,%d)' % (x[0], y[0], x[1], y[1])

    # make a triangle with an angle of 180
    x.append(x[0])
    y.append(y[0])
    nodes.append('')
    counter = 0
    for itemX, itemY, itemN in zip(x, y, nodes):
        counter += 1
        realXNodes = []
        realYNodes = []

        xTries = [1, 0, -1, -1, -1, 0, 1, 1]  # maybe eliminate some of these when axes are in play..??????
        yTries = [-1, -1, -1, 0, 1, 1, 1,
                  0]  # once this works, we can roll through corner pieces first as they will probably be more likely
        dist = .5

        for xT, yT in zip(xTries, yTries):
            xNode = itemX + dist * xT
            yNode = itemY + dist * yT

            p = [xNode, yNode]
            a = [x[0], y[0]]
            b = [x[1], y[1]]
            c = [x[2], y[2]]

            if pointTriangle('outside', p, a, b, c) == True:
                realXNodes.append(xNode)
                realYNodes.append(yNode)
                # could have it end here but would rather have multiple points
        xNode = random.choice(realXNodes)
        yNode = random.choice(realYNodes)

        if counter != 3:
            com('node at (%g,%g) {%s}' % (xNode, yNode, itemN))
    com(string)