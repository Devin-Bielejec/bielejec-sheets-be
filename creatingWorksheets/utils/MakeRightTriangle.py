import math
import random
import sys
from .PolygonClasses import Point, Shape, LineSegment
from .LabelPolygon import CalcAndReturnLabelCoordsAsLists
from .CommonFunctions import ReturnPointCoordsAsLists, _Rad2D, _D2Rad, _Shuffled, _Frange

def MakeRightTriangle(xMinGraph, xMaxGraph, yMinGraph, yMaxGraph, mustHaveNoFlatSides = False, mustHaveIntPoints = False, size = "medium"):
    """
    returns Right Triangle as an object of the Shape class

    Params:
    xMinGraph, xMaxGraph, yMinGraph, yMaxGraph - these are the specifications for the graph size (the actual shape will be some fraction of this size based on the size param). Can be ints or floats.
    mustHaveNoFlatSides - boolean - if True, the shape can not have any vertical or horizontal lines in it. If False, it may or may not.
    mustHaveIntPoints - boolean - if True, the shape must have all integer points. If False, it may or may not (but it's very unlikely that it will)
    size - can be "small", "medium", "large", or a float between 0 and 1 that represents the approximate fraction of the area of the graph filled
    """
    gridSizeTries = set()
    if type(size) is str:
        if size == "small" or size == 's':
            fractionOfGraphFilled = .15
        elif size == "medium" or size == 'm':
            fractionOfGraphFilled = .25
        elif size == "large" or size == 'l':
            fractionOfGraphFilled = .5
        else:
            print("Invalid size parameter. Options are small, medium, or large")
    else:
        fractionOfGraphFilled = size
    return _DoMakeRightTriangle(fractionOfGraphFilled, mustHaveNoFlatSides, mustHaveIntPoints, xMinGraph, xMaxGraph, yMinGraph, yMaxGraph, gridSizeTries)

def _DoMakeRightTriangle(fractionOfGraphFilled, mustHaveNoFlatSides, mustHaveIntPoints, xMinGraph, xMaxGraph, yMinGraph, yMaxGraph, gridSizeTries):
    xMin, xMax, xRange, yMin, yMax, yRange = _RestrictShapeToProperSizeRectangle(fractionOfGraphFilled, mustHaveIntPoints, xMinGraph, xMaxGraph, yMinGraph, yMaxGraph, gridSizeTries)

    point1, sidesUsed = _PickPoint1(xMax, xMin, yMax, yMin)

    #pick point on different side to be second point. Will do this by starting from oppposite corner and moving down one side
    xCoordOppositeCorner = xMax if point1.x == xMin else xMin
    yCoordOppositeCorner = yMax if point1.y == yMin else yMin

    oppositeCorner = Point(xCoordOppositeCorner, yCoordOppositeCorner)
    moveInXDirection = bool(random.getrandbits(1))

    minimumRadOffFlat = _D2Rad(5) if mustHaveNoFlatSides else 0 #This is to prevent it from looking vertical / horizontal even if it is actually not
    minimumRadOffDiagonal = _D2Rad(5) #This is to prevent the triangle from having one very short side

    #This is the expression you get when you do out the trig. No point showing work here, you'll need a pad and paper to check
    smallXDistanceToAvoidDiagonal = (math.sqrt(xRange ** 2 + yRange ** 2) * math.sin(minimumRadOffDiagonal)) / (math.sin(_D2Rad(90) - math.atan(yRange / xRange) - minimumRadOffDiagonal))
    smallYDistanceToAvoidDiagonal = (math.sqrt(xRange ** 2 + yRange ** 2) * math.sin(minimumRadOffDiagonal)) / (math.sin(_D2Rad(90) - math.atan(xRange / yRange) - minimumRadOffDiagonal))
    
    smallXDistanceToAvoidVertical = yRange * math.tan(_D2Rad(minimumRadOffFlat))
    smallYDistanceToAvoidHorizontal = xRange * math.tan(_D2Rad(minimumRadOffFlat))
    maxXMovementAllowed = xRange - smallXDistanceToAvoidVertical
    maxYMovementAllowed = yRange - smallYDistanceToAvoidHorizontal

    if random.getrandbits(1):#flip a coin to decide whether to try moving in x direction first or y direction
        resultFromXDirection = _TryAllPointCombosForTheseRectDimensions(sidesUsed, smallXDistanceToAvoidDiagonal, maxXMovementAllowed, oppositeCorner, xMin, xMax, xRange, yMin, yMax, yRange, mustHaveIntPoints, point1, True)
        if type(resultFromXDirection) is not str:
            return resultFromXDirection
        resultFromYDirection = _TryAllPointCombosForTheseRectDimensions(sidesUsed, smallYDistanceToAvoidDiagonal, maxYMovementAllowed, oppositeCorner, xMin, xMax, xRange, yMin, yMax, yRange, mustHaveIntPoints, point1, False)
        if type(resultFromYDirection) is not str:
            return resultFromYDirection
    else:
        resultFromYDirection = _TryAllPointCombosForTheseRectDimensions(sidesUsed, smallYDistanceToAvoidDiagonal, maxYMovementAllowed, oppositeCorner, xMin, xMax, xRange, yMin, yMax, yRange, mustHaveIntPoints, point1, False)
        if type(resultFromYDirection) is not str:
            return resultFromYDirection
        resultFromXDirection = _TryAllPointCombosForTheseRectDimensions(sidesUsed, smallXDistanceToAvoidDiagonal, maxXMovementAllowed, oppositeCorner, xMin, xMax, xRange, yMin, yMax, yRange, mustHaveIntPoints, point1, True)
        if type(resultFromXDirection) is not str:
            return resultFromXDirection

    return _DoMakeRightTriangle(fractionOfGraphFilled, mustHaveNoFlatSides, mustHaveIntPoints, xMinGraph, xMaxGraph, yMinGraph, yMaxGraph, gridSizeTries)

def _TryAllPointCombosForTheseRectDimensions(sidesUsed, smallDistanceToAvoidDiagonal, maxMovementAllowed, oppositeCorner, xMin, xMax, xRange, yMin, yMax, yRange, mustHaveIntPoints, point1, moveXDirection):
    tempSidesUsed = sidesUsed.copy()
    #pre-update tempSidesUsed to include the side that p2 will use. This is because p2 is found in the for loop, but tempSidesUsed only needs to be updated once
    if moveXDirection:
        tempSidesUsed["top"] = True #one of them will already be used from the first point. The other will now be used
        tempSidesUsed["bottom"] = True
    else:
        tempSidesUsed["left"] = True #one of them will already be used from the first point. The other will now be used
        tempSidesUsed["right"] = True

    if mustHaveIntPoints:
        distanceOptions = _Shuffled(range(int(math.ceil(smallDistanceToAvoidDiagonal)), int(maxMovementAllowed + 1)))#shuffled so that all valid options are possible and roughly equally likely
    else:
        stepSize = xRange / 100.0 if moveXDirection else yRange / 100.0
        distanceOptions = _Shuffled(list(_Frange(smallDistanceToAvoidDiagonal, maxMovementAllowed, stepSize)))

    for distance in distanceOptions:
        #point2 will always move toward the used side, since it is on the opposite corner from point1
        if moveXDirection:
            if tempSidesUsed["left"]:
                point2 = Point(oppositeCorner.x - distance, oppositeCorner.y)
            elif tempSidesUsed["right"]:
                point2 = Point(oppositeCorner.x + distance, oppositeCorner.y)
            else:
                print("Error. Point1 should have used either left or right side.")
        else:
            if tempSidesUsed["top"]:
                point2 = Point(oppositeCorner.x, oppositeCorner.y + distance)
            elif tempSidesUsed["bottom"]:
                point2 = Point(oppositeCorner.x, oppositeCorner.y - distance)
            else:
                print("Error. Point1 should have used either top or bottom side.")
            
        point3 = _FindPoint3(oppositeCorner, point1, point2, tempSidesUsed, xMin, xMax, yMin, yMax)
        if type(point3) is str: #If point3 is invalid it will be string. Check for this
            continue
        if mustHaveIntPoints:
            if point3.intCoords() == point3:
                point3 = point3.intCoords()
            else:
                continue
        listOfPoints = [point1, point2, point3]
        shape = Shape(listOfPoints)
        return shape
    return "No valid solution found"

def _FindPoint3(opppositeCorner, point1, point2, sidesUsed, xMin, xMax, yMin, yMax):
    """find point on last side that is RA from point2 (point 1 is in corner so RA will not work from that point)"""
    lineSegment = LineSegment(point1, point2)
    if type(lineSegment.slope) is str or lineSegment.angleOfIncline == 0: #check if point2 is also on a corner (will result in vertical or horizontal line segment, since opposite corner is already ruled out)
        point3 = opppositeCorner
        return point3    

    angle = lineSegment.angleOfIncline + (math.pi  / 2)#add pi/2 to get right angle
    
    if not sidesUsed["left"]:
        newX = xMin
        newY = "calculate"
    elif not sidesUsed["right"]:
        newX = xMax
        newY = "calculate"
    elif not sidesUsed["bottom"]:
        newY = yMin
        newX = "calculate"
    elif not sidesUsed["top"]:
        newY = yMax
        newX = "calculate"
    else:
        print("Error. All sides are used")

    if (newY == "calculate"):
        newY = (newX - point2.x) * math.tan(angle) + point2.y #Check side of grid
        if newY <= yMax and newY >= yMin and newY != point2.y:
            point3 = Point(newX, newY)
            return point3
    
    if (newX == "calculate"):
        newX = (newY - point2.y) / math.tan(angle) + point2.x #Check top or bottom of grid
        if newX <= xMax and newX >= xMin and newX != point2.x:
            point3 = Point(newX, newY)
            return point3

    point3 = "Invalid point"
    return point3

def _PickPoint1(xMax, xMin, yMax, yMin):
    """pick random corner of small grid to be first point"""
    sidesUsed = {"top" : False, "bottom" : False, "left" : False, "right" : False}
    if bool(random.getrandbits(1)):#flip coin
        xCoordinate = xMin
        sidesUsed["left"] = True
    else:
        xCoordinate = xMax
        sidesUsed["right"] = True
    if bool(random.getrandbits(1)):
        yCoordinate = yMin
        sidesUsed["bottom"] = True
    else:
        yCoordinate = yMax
        sidesUsed["top"] = True
    
    point1 = Point(xCoordinate, yCoordinate)
    return point1, sidesUsed

def _CheckRightnessByPythagorean(points):
    """where the line from points[0] to points[2] is the hypotenuse"""
    legsAreBiggerThanHypotBy = points[0].distance(points[1]) ** 2 + points[1].distance(points[2]) ** 2 - points[0].distance(points[2]) ** 2
    if legsAreBiggerThanHypotBy < .05:
        print("Is a right triangle! Calculation error is", legsAreBiggerThanHypotBy)
    else:
        print("Isn't a right triangle. Legs squared are bigger than the hypotenuse squared by", legsAreBiggerThanHypotBy)

