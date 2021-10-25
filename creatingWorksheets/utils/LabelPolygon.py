import math
from utils.CommonFunctions import _FollowAngle
from utils.PolygonClasses import *

def CalcAndReturnLabelCoordsAsLists(shape, labelSize = 2, labelDist = 1.5):
    """
    returns label coordinates as a list of Xs and list of Ys

    Params:
    shape - the shape that is being labeled, using the Shape class
    labelSize - the length of one side of the label (label is assumed to be square)
    labelDist - the distance from any given shape point to the edge of its label, following an angle directly toward the center of the label
    """
    _LabelPolygon(shape, labelSize, labelDist)
    return _ReturnLabelCoordsAsLists(shape)

def _LabelPolygon(shape, labelSize = 2, labelDist = 1.5):
    for i in range(0, len(shape.points)):
        currPoint = Point(shape.points[i].x, shape.points[i].y)

        segment1 = shape.lineSegments[(i + len(shape.points) - 1) % len(shape.points)] #will wrap around to get previous line segment
        segment2 = shape.lineSegments[i]
        incline1 = segment1.angleOfIncline
        incline2 = segment2.angleOfIncline

        if incline1 == incline2:
            print ("Error, two segments are the same")
            return

        anglesInShape = []#hold all midpointOfAngles that yield a test point in the shape
        anglesOutOfShape = []

        for num in range(4):
            #test the 4 angles that the two lines make to determine what direction to put the label
            midpointOfAngles = _GetMidpointOfAcuteAngle(incline1, incline2)

            testPoint = _FollowAngle(midpointOfAngles, 0.1, currPoint)#follow angle in a short line

            if _IsPointInShape(testPoint, shape):
                anglesInShape.append(midpointOfAngles)
            else:
                anglesOutOfShape.append(midpointOfAngles)

            if num % 2 == 0:#alternate which incline is flipping
                incline1 = _FlipAngle(incline1)
            else:
                incline2 = _FlipAngle(incline2)

        if len(anglesInShape) == 1:#outward pointing point
            oppositeAngle = (anglesInShape[0] + math.pi) % (2 * math.pi)
            _PlaceLabel(i, labelDist, labelSize, oppositeAngle, shape)
        elif len(anglesOutOfShape) == 1:#inward pointing point
            _PlaceLabel(i, labelDist, labelSize, anglesOutOfShape[0], shape)
        else:
            print("Error. Do not know what to do with", len(anglesInShape), "angles in shape and", len(anglesOutOfShape), "angles out of shape.")

def _PlaceLabel(i, labelDist, labelSize, angle, shape):
    #use labelDist to find point on edge of label's square
    xDisplacementToLabelEdge = labelDist * math.cos(angle)
    yDisplacementToLabelEdge = labelDist * math.sin(angle)

    #add extra x and y to find center of label based on labelSize
    referenceAngle = _GetReferenceAngle(angle)

    extraXToGetToLabelCenter = labelSize / 2.0 if referenceAngle <= math.pi / 4 else (labelSize / 2.0) / math.tan(referenceAngle)
    extraYToGetToLabelCenter = labelSize / 2.0 if referenceAngle >= math.pi / 4 else math.tan(referenceAngle) * labelSize / 2.0
    if xDisplacementToLabelEdge < 0:
        extraXToGetToLabelCenter *= -1
    if yDisplacementToLabelEdge < 0:
        extraYToGetToLabelCenter *= -1

    labelPointx = shape.points[i].x + xDisplacementToLabelEdge + extraXToGetToLabelCenter
    labelPointy = shape.points[i].y + yDisplacementToLabelEdge + extraYToGetToLabelCenter
    
    shape.points[i].label = Label(labelPointx, labelPointy, labelSize)

def _GetReferenceAngle(angle):
    angle %= math.pi * 2
    refAngle = angle
    if angle <= math.pi / 2:
        refAngle = angle
    elif angle <= math.pi:
        refAngle = math.pi - angle
    elif angle <= 3 * math.pi / 2:
        refAngle = angle - math.pi
    elif angle < 2 * math.pi:
        refAngle = 2 * math.pi - angle

    return refAngle
    
def _FlipAngle(angle):
    return (angle + math.pi) % (2 * math.pi)

def _GetMidpointOfAcuteAngle(incline1, incline2):
    bigIncline = max(incline1, incline2)
    smallIncline = min(incline1, incline2)
    angle = bigIncline - smallIncline

    bottomIncline = smallIncline

    if angle > math.pi:
        angle = 2 * math.pi - angle #get acute angle
        bottomIncline = bigIncline

    midpoint = angle / 2.0 + bottomIncline
    return midpoint

def _IsPointInShape(point, shape):
    """Make ray from point and see how many times it intersects shape"""
    #for ease, we will choose a vertical ray pointing up from point
    interceptCount = 0
    for segment in shape.lineSegments:
        xValueIsInRange = point.x >= segment.minX and point.x < segment.maxX
        if not xValueIsInRange:
            continue

        if segment.slope == "vertical":
            if segment.minY > point.y:
                interceptCount += 1
                continue
            elif segment.maxY >= point.y:
                print("Error. Point should never be on line")
                return True
            else:
                continue

        pointIsOnLine = point.y == segment.slope * point.x + segment.yIntercept
        if pointIsOnLine:
            print("Error. Point should never be on line")
            return True

        yValueIsBelowLine = point.y < segment.slope * point.x + segment.yIntercept
        if yValueIsBelowLine:
            interceptCount += 1
    if interceptCount % 2 == 0:
        return False
    else:
        return True

def _PrintShapeAndLabels(shape):
    print("Shape points:")
    for point in shape.points:
        print("(", point.x, ",", point.y, ")")

    print("Label points")
    for point in shape.points:
        print("(", point.label.x, ",", point.label.y, ")")

def _ReturnLabelCoordsAsLists(shape):
    xLabelCoordinates = []
    yLabelCoordinates = []
    for point in shape.points:
        xLabelCoordinates.append(point.label.x)
        yLabelCoordinates.append(point.label.y)
    return xLabelCoordinates, yLabelCoordinates


