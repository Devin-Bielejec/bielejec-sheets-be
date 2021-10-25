import random
import math
from .PolygonClasses import Point

def ReturnPointCoordsAsLists(shape):
    xCoordinates = []
    yCoordinates = []
    for point in shape.points:
        xCoordinates.append(point.x)
        yCoordinates.append(point.y)
    return xCoordinates, yCoordinates

def _Shuffled(seq):
    if not isinstance(seq, list):
        shuffledList = list(seq)
    else:
        shuffledList = seq
    random.shuffle(shuffledList)
    return shuffledList

def _FollowAngle(angle, distance, point = "none"):
    """angle in radians"""
    xDispToFollowAngle = distance * math.cos(angle)
    yDispToFollowAngle = distance * math.sin(angle)

    if point == "none":
        return xDispToFollowAngle, yDispToFollowAngle

    tempPointX = point.x + xDispToFollowAngle
    tempPointY = point.y + yDispToFollowAngle
    tempPoint = Point(tempPointX, tempPointY)

    return tempPoint

def _SimplifyFraction(numerator, denominator):
    divisor = min(abs(numerator), abs(denominator))
    while divisor >= 2:
        if numerator % divisor == 0 and denominator % divisor == 0:
            numerator /= divisor
            denominator /= divisor
            return numerator, denominator
        else:
            divisor -= 1
    return numerator, denominator

def _Frange(start, stop, jump = 1):
    """float version of range(). Has roundoff error, but is useful if you don't need to be that exact"""
    while start < stop:
        yield start
        start += jump

def _D2Rad(degrees):
    return (degrees * math.pi) / 180

def _Rad2D(rads):
    return (180 * rads) / math.pi

def CalcApproxAreaOfShape(size, xMaxGraph, xMinGraph, yMaxGraph, yMinGraph):
    if type(size) is str:
        if size == "tiny" or size == 't':
            fractionOfGraphFilled = .05
        elif size == "small" or size == 's':
            fractionOfGraphFilled = .15
        elif size == "medium" or size == 'm':
            fractionOfGraphFilled = .25
        elif size == "large" or size == 'l':
            fractionOfGraphFilled = .5
        else:
            print("Invalid size parameter. Options are small, medium, or large")
    else:
        fractionOfGraphFilled = size 
    
    approxAreaOfShape = (xMaxGraph - xMinGraph) * (yMaxGraph - yMinGraph) * fractionOfGraphFilled
    return approxAreaOfShape

def SetDefaultXLengthAndYLength(maxXLength, maxYLength, xMaxGraph, xMinGraph, yMaxGraph, yMinGraph):
    if maxXLength == "default":
        maxXLength = xMaxGraph - xMinGraph
    if maxYLength == "default":
        maxYLength = yMaxGraph - yMinGraph
    return maxXLength, maxYLength
