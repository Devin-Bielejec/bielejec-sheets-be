import math
import random
import sys
from .PolygonClasses import Shape, Point
import utils.CommonFunctions
from .LabelPolygon import CalcAndReturnLabelCoordsAsLists

def MakeRectangle(xMinGraph, xMaxGraph, yMinGraph, yMaxGraph, hasFlatSides = False, mustHaveIntPoints = False, size = "medium", maxXRange = "default", maxYRange = "default", minXRange = 0, minYRange = 0):
    """
    returns a new (non-square) Rectangle as [listofX, listofY], [labelsListofX, labelsListofY]

    Params:
    xMinGraph, xMaxGraph, yMinGraph, yMaxGraph - these are the specifications for the graph size (the actual shape will be some fraction of this size based on the size param). Can be ints or floats.
    hasFlatSides - boolean - if True, the shape has all horizontal/vertical sides. If False, it has none
    mustHaveIntPoints - boolean - if True, the shape must have all integer points. If False, it may or may not (but it's very unlikely that it will)
    size - can be "tiny", "small", "medium", "large", or a float between 0 and 1 that represents the approximate fraction of the area of the graph filled
    maxXLength, maxYLength, minXLength, minYLength - Determines the maximum and minimum ranges of X and Y values. XLength is max(XCoord) - min(XCoord)
    """
    maxXRange, maxYRange = CommonFunctions.SetDefaultXLengthAndYLength(maxXRange, maxYRange, xMaxGraph, xMinGraph, yMaxGraph, yMinGraph)
    approxAreaOfShape = CommonFunctions.CalcApproxAreaOfShape(size, xMaxGraph, xMinGraph, yMaxGraph, yMinGraph)
    percentAcceptableError = .10 #The area can be off by this percent in either direction. It's in decimal form, so .50 means the area will be [-50%, +50%] of the calculated area
    maxAcceptableError = percentAcceptableError * approxAreaOfShape

    widthOptions = _DetermineWidthOptions(xMinGraph, xMaxGraph, yMinGraph, yMaxGraph, mustHaveIntPoints, hasFlatSides, approxAreaOfShape, maxAcceptableError, True)
    rectangle = _FindWidthThatWorksAndReturnShape(xMinGraph, xMaxGraph, yMinGraph, yMaxGraph, mustHaveIntPoints, widthOptions, approxAreaOfShape, maxAcceptableError, hasFlatSides, maxXRange, maxYRange, minXRange, minYRange, True)
    
    return CommonFunctions.ReturnPointCoordsAsLists(rectangle), CalcAndReturnLabelCoordsAsLists(rectangle)

def _DetermineWidthOptions(xMinGraph, xMaxGraph, yMinGraph, yMaxGraph, mustHaveIntPoints, hasFlatSides, approxAreaOfShape, maxAcceptableError, isRectangle):
    if not isRectangle:
        approxAreaOfShape *= 2 #A right triangle will have half the area of a rectangle, so need to compensate for this

    minAcceptableWidth = (xMaxGraph - xMinGraph) * (yMaxGraph - yMinGraph) / 200 #The bigger the graph, the bigger the smallest side has to be for it to not look too small
    maxAcceptableWidth = math.sqrt(approxAreaOfShape + maxAcceptableError) #width can't be more than length

    if mustHaveIntPoints:
        if hasFlatSides:
            minAcceptableWidth = math.ceil(minAcceptableWidth) #If flat and int points, width must be int
            maxAcceptableWidth = math.floor(maxAcceptableWidth)
        else:
            minAcceptableWidth =  math.sqrt(math.ceil(minAcceptableWidth ** 2)) #Since side^2 will always be an int, we round up to the next width that makes side^2 an int
            maxAcceptableWidth = math.sqrt(math.floor(maxAcceptableWidth ** 2)) #Round down for max width

    width = minAcceptableWidth

    if mustHaveIntPoints:
        if hasFlatSides:
            widthOptions = CommonFunctions._Shuffled([x for x in range(minAcceptableWidth, maxAcceptableWidth + 1)]) #width must be int in this case
        else:
            widthOptions = CommonFunctions._Shuffled([math.sqrt(x) for x in CommonFunctions._Frange(minAcceptableWidth ** 2, maxAcceptableWidth ** 2 + 1)]) #loops randomly, incrementing side^2 by one (which must be an int if mustHaveIntPoints)
    else:
        numberOfWidthsToTry = 100.0
        increment = (maxAcceptableWidth - minAcceptableWidth) / (numberOfWidthsToTry - 1) #the -1 avoids off-by-one error, since we include both the start and end in our range
        widthOptions = CommonFunctions._Shuffled(CommonFunctions._Frange(minAcceptableWidth, maxAcceptableWidth + increment, increment))

    return widthOptions

def _FindWidthThatWorksAndReturnShape(xMinGraph, xMaxGraph, yMinGraph, yMaxGraph, mustHaveIntPoints, widthOptions, approxAreaOfShape, maxAcceptableError, hasFlatSides, maxXRange, maxYRange, minXRange, minYRange, isRectangle):
    for width in widthOptions:
        dispXP1ToP2, dispYP1ToP2, realWidth = _FindDisplacementBetweenP1AndP2(mustHaveIntPoints, width, hasFlatSides, maxXRange, maxYRange, minXRange, minYRange)
        if realWidth == 0:
            continue
        dispXP2ToP3, dispYP2ToP3, error = _FindDisplacementBetweenP2AndP3(dispXP1ToP2, dispYP1ToP2, realWidth, approxAreaOfShape, mustHaveIntPoints, isRectangle, maxXRange, maxYRange, minXRange, minYRange)
        if math.fabs(error) <= maxAcceptableError:
            points = _CalculatePoints(xMinGraph, xMaxGraph, yMinGraph, yMaxGraph, dispXP1ToP2, dispYP1ToP2, dispXP2ToP3, dispYP2ToP3, mustHaveIntPoints, isRectangle)
            if points:
                shape = Shape(points)
                return shape
    print("Error. No rectangle can be made with these parameters.")
    sys.exit()

def _AdjustMaxAndMinXDispsForMaxXAndYLengths(chosenWidth, maxDisplacementX, maxXRange, maxYRange, minDisplacementX):
    if maxDisplacementX < 0:
        maxDisplacementX = max(maxDisplacementX, -maxXRange)
    else:
        maxDisplacementX = min(maxDisplacementX, maxXRange)
    if maxYRange < chosenWidth:#This if is necessary to prevent a negative sqrt. If maxYLength is >= chosenWidth, none of this is necessary
        if minDisplacementX < 0:
            minDisplacementX = min(minDisplacementX, -math.sqrt(chosenWidth ** 2 - maxYRange ** 2)) #Have to also account for maxYLength. Adjusting minX up if needed to be the X that will create the maxY
        else:
            minDisplacementX = max(minDisplacementX, math.sqrt(chosenWidth ** 2 - maxYRange ** 2))
    return maxDisplacementX, minDisplacementX

def _FindDisplacementBetweenP1AndP2(mustHaveIntPoints, chosenWidth, hasFlatSides, maxXRange, maxYRange, minXRange, minYRange):
    if mustHaveIntPoints:
        distX = max(1, minXRange)

        minError = 1e9 #just picking a large number to initalize it, so any reasonable error will override it
        xDistWithMinError = 0 #if this remains 0, there is a problem. But it should be overridden
        yDistWithMinError = 0
        realWidth = 0

        while distX <= maxXRange and distX <= chosenWidth:
            distY = 0 if hasFlatSides else max(round(math.sqrt(chosenWidth ** 2 - distX ** 2)), 1)
            realWidth = distX if hasFlatSides else math.sqrt(distY ** 2 + distX ** 2)
            error = realWidth - chosenWidth  #negative error if below chosen width
            if error <= minError:
                if error != minError or bool(random.getrandbits(1)): #If equal, flip a coin as to whether this error is better than the previous one or not
                    minError = error
                    xDistWithMinError = distX
                    yDistWithMinError = distY
            distX += 1
        xDispWithMinError = -xDistWithMinError if bool(random.getrandbits(1)) else xDistWithMinError #To get the full 360 degree possibility needed, we need to have a possibility of -x and -y displacement
        yDispWithMinError = -yDistWithMinError if bool(random.getrandbits(1)) else yDistWithMinError
        return xDispWithMinError, yDispWithMinError, realWidth
    else:
        if hasFlatSides:
            if (bool(random.getrandbits(1))):
                dispY = 0
                dispX = -chosenWidth if (bool(random.getrandbits(1))) else chosenWidth
            else:
                dispX = 0
                dispY = -chosenWidth if (bool(random.getrandbits(1))) else chosenWidth
            realWidth = chosenWidth
        else:
            minAngleOffFlat = 5 #in degrees
            minDisplacementX = math.sin(CommonFunctions._D2Rad(minAngleOffFlat)) * chosenWidth #in order to make sure it's at least minAngleOffFlat degrees off flat
            maxDisplacementX = math.cos(CommonFunctions._D2Rad(minAngleOffFlat)) * chosenWidth
            maxDisplacementX, minDisplacementX = _AdjustMaxAndMinXDispsForMaxXAndYLengths(chosenWidth, maxDisplacementX, maxXRange, maxYRange, minDisplacementX)

            distX = random.random() * (maxDisplacementX - minDisplacementX) + minDisplacementX
            distY = math.sqrt(chosenWidth ** 2 - distX ** 2)

            dispX = -distX if bool(random.getrandbits(1)) else distX #To get the full 360 degree possibility needed, we need to have a possibility of -x and -y displacement
            dispY = -distY if bool(random.getrandbits(1)) else distY
            realWidth = math.sqrt(distY ** 2 + distX ** 2)
        return dispX, dispY, realWidth
            
def _FindDisplacementBetweenP2AndP3(dispXP1ToP2, dispYP1ToP2, realWidth, approxAreaOfShape, mustHaveIntPoints, isRectangle, maxXRange, maxYRange, minXRange, minYRaneg):
    """Finds the displacement between Point 2 and Point3 that has the least error, compared to the area we want. Returns changeinX, changeinY"""
    slopeDenom, slopeNum = CommonFunctions._SimplifyFraction(dispYP1ToP2, dispXP1ToP2) #slope of P2ToP3 will be negative recipricol of slope from P1toP2 because 90 degree angle
    if bool(random.getrandbits(1)): #decide randomly if top or bottom of slope gets the negative (must be negative recipricol) #TODO: For Right Triangle, could try both instead of deciding randomly
        slopeDenom *= -1
    else:
        slopeNum *= -1

    minRatioOfLenToWid = 1.10 if isRectangle else 1 #The length must be at least this width * this in order for the shape to not look like a square. Doesn't matter for right triangle
    minLength = realWidth * minRatioOfLenToWid

    #TODO: This will be slightly different for Right Triangle, since there is no 4th point
    largestAcceptableDistX = maxXRange - abs(dispXP1ToP2)
    largestAcceptableDistY = maxYRange - abs(dispYP1ToP2)
    smallestAcceptableDistX = minXRange - abs(dispXP1ToP2) #negative should be fine, just means min doesn't affect the distance
    smallestAcceptableDistY = minYRaneg - abs(dispYP1ToP2)

    if mustHaveIntPoints:
        minError = 9e9
        intMultipleWithMinError = 1
        integerMultiple = 1 #we know the slope of the line, but the integer multiple tells us how far we follow that line. Must be an int multiple, since we need int points
        while True:
            realLength = math.sqrt((slopeNum * integerMultiple) ** 2 + (slopeDenom * integerMultiple) ** 2)
            error = realLength * realWidth - approxAreaOfShape
            currDispX = slopeDenom * integerMultiple
            currDispY = slopeNum * integerMultiple
            if abs(currDispX) < smallestAcceptableDistX or abs(currDispY) < smallestAcceptableDistY:
                integerMultiple += 1
                continue
            if abs(currDispX) > largestAcceptableDistX or abs(currDispY) > largestAcceptableDistY:
                break
            if math.fabs(error) <= math.fabs(minError) and realLength >= minLength:
                if math.fabs(error) != math.fabs(minError) or bool(random.getrandbits(1)): #If Errors are equal, flip a coin to decide if the new one overrides the old
                    minError = error
                    intMultipleWithMinError = integerMultiple
            if error > 0: #Error will only get worse from here, since the length is always increasing
                break
            integerMultiple += 1
        bestDispX = slopeDenom * intMultipleWithMinError
        bestDispY = slopeNum * intMultipleWithMinError
        error = minError
    else:
        targetLength = max(approxAreaOfShape / realWidth, minLength)
        if slopeDenom == 0: #To prevent division by zero
            if slopeNum > 0:
                angleOfSlope = CommonFunctions._D2Rad(90)
            if slopeNum < 0:
                angleOfSlope = CommonFunctions._D2Rad(-90)
        else:
            angleOfSlope = math.atan(slopeNum / slopeDenom)
        bestDispX, bestDispY = CommonFunctions._FollowAngle(angleOfSlope, targetLength)
        
        adjustedTargetLength = targetLength
        if abs(bestDispX) > largestAcceptableDistX:
            ratio = largestAcceptableDistX / abs(bestDispX)
            adjustedTargetLength = targetLength * ratio
        if abs(bestDispY) > largestAcceptableDistY:
            ratio = largestAcceptableDistY / abs(bestDispY)
            if targetLength * ratio < adjustedTargetLength: #Want to adjust the target length only if it's lower than what the XDisp was adjusting it to
                adjustedTargetLength = targetLength * ratio
        if abs(bestDispX) < smallestAcceptableDistX:
            ratio = smallestAcceptableDistX / abs(bestDispX)
            if adjustedTargetLength < targetLength:
                return 1, 1, 9e9 #Return a large error, since this will not work. Cannot adjust the length to be both larger and smaller
            else:
                adjustedTargetLength = targetLength * ratio
        if abs(bestDispY) < smallestAcceptableDistY:
            ratio = smallestAcceptableDistX / abs(bestDispX)
            if adjustedTargetLength < targetLength:
                return 1, 1, 9e9 #Return a large error, since this will not work. Cannot adjust the length to be both larger and smaller
            elif adjustedTargetLength < targetLength * ratio:
                adjustedTargetLength = targetLength * ratio

        bestDispX, bestDispY = CommonFunctions._FollowAngle(angleOfSlope, adjustedTargetLength)
        error = realWidth * math.sqrt(bestDispX ** 2 + bestDispY ** 2) - approxAreaOfShape
    return bestDispX, bestDispY, error

def _CalculatePoints(xMinGraph, xMaxGraph, yMinGraph, yMaxGraph, dispXP1ToP2, dispYP1ToP2, dispXP2ToP3, dispYP2ToP3, mustHaveIntPoints, isRectangle):
    prelimPoint1 = Point(0,0) #We have preliminary points so that we can put the shape on the graph, and then slide it into the desired position
    prelimPoint2 = Point(dispXP1ToP2, dispYP1ToP2)
    prelimPoint3 = Point(prelimPoint2.x + dispXP2ToP3, prelimPoint2.y + dispYP2ToP3)

    if isRectangle:#This function is also used for RightTriangle
        prelimPoint4 = Point(dispXP2ToP3, dispYP2ToP3) #Will be the same relationship to Point1 (0,0) as Point2 was to Point3
        pointList = [prelimPoint1, prelimPoint2, prelimPoint3, prelimPoint4]
    else:
        pointList = [prelimPoint1, prelimPoint2, prelimPoint3]

    xMin = 0
    xMax = 0
    yMin = 0
    yMax = 0
    for point in pointList:
        if point.x < xMin:
            xMin = point.x
        if point.x > xMax:
            xMax = point.x
        if point.y < yMin:
            yMin = point.y
        if point.y > yMax:
            yMax = point.y

    minXMovementAllowed = xMinGraph - xMin
    maxXMovementAllowed = xMaxGraph - xMax
    minYMovementAllowed = yMinGraph - yMin
    maxYMovementAllowed = yMaxGraph - yMax

    if maxXMovementAllowed < minXMovementAllowed or maxYMovementAllowed < minYMovementAllowed:
        #print("Error. Shape too large for graph")
        return False

    if mustHaveIntPoints:
        xMovement = random.randrange(minXMovementAllowed, maxXMovementAllowed + 1)
        yMovement = random.randrange(minYMovementAllowed, maxYMovementAllowed + 1)
    else:
        xMovement = random.random() * (maxXMovementAllowed - minXMovementAllowed) + minXMovementAllowed
        yMovement = random.random() * (maxYMovementAllowed - minYMovementAllowed) + minYMovementAllowed

    for point in pointList:
        point.x += xMovement
        point.y += yMovement

    return pointList


