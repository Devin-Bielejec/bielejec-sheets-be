from .pdfFunctions import com, graphPolygon
from pylatex import VerticalSpace, NewLine, Center, TikZ
import math
import random
from .transformations import rotateCoordinatesAsList
'''
cone (upright, sideways left, sideways right, upside down) - angle of rotation

radius labeled
diameter labeled
height labeled
::with what label

points of diameter labeled
points of radius labeled
(4 points total)
LETTERS

height(altitude) drawn with right angle
radius drawn
diameter drawn

'''

def rectangleCoordinates(typeOfRectangle = ['rectangle','square'], polygonSize = ['small','medium','large'], xMaxGraph = 10, yMaxGraph = 10, xMinGraph = -10, yMinGraph = -10, evenSided = True, unevenCenterOption = False):
	polygonSizeChosen = random.choice(polygonSize)
	typeOfTriangleChosen = random.choice(typeOfRectangle)
	if polygonSizeChosen == 'small':
		sizeFactor = 1/3
	elif polygonSizeChosen == 'medium':
		sizeFactor = 1/2
	elif polygonSizeChosen == 'large':
		sizeFactor = 1/1.5

	sideSize = min([xMaxGraph, yMaxGraph]) - max([xMinGraph, yMinGraph])
	sideSize = sideSize*sizeFactor
	if evenSided == True:
		if sideSize % 2 != 0:
			sideSize -= 1 # so that it will be even
	#going from bottom left counterclockwise
	#going to make the square first, then translate it anywhere, yada
	x1 = xMinGraph
	y1 = yMinGraph

	x2 = xMinGraph
	y2 = y1 + sideSize

	x3 = x2 + sideSize
	y3 = y2

	x4 = x3
	y4 = y1

	xs = [int(x1), int(x2), int(x3), int(x4)]
	ys = [int(y1), int(y2), int(y3), int(y4)]
	centerX = (max(xs)+min(xs))/2
	centerY = (max(ys)+min(ys))/2
	#translate yo
	newX = []
	newY = []
	xChange = random.randint(xMinGraph-min(xs), xMaxGraph-max(xs))
	yChange = random.randint(yMinGraph-min(ys), yMaxGraph-max(ys))
	if unevenCenterOption == True:
		while (xChange+centerX) == (yChange+centerY):
			print('WOAHOWAHo')
			xChange = random.randint(xMinGraph-min(xs), xMaxGraph-max(xs))
			yChange = random.randint(yMinGraph-min(ys), yMaxGraph-max(ys))
	for itemX, itemY in zip(xs, ys):
		newX.append(itemX+xChange)
		newY.append(itemY+yChange)

	return newX, newY
def arc(doc = None, dashed = False, startDegrees = 0, endDegrees = 0, xRadius = 2, yRadius = .4, startPoint = '(0,0)'):
	if dashed == True:
		dashedString = '[dashed]'
	else:
		dashedString = ''
	com('draw ' + dashedString + startPoint + 'arc (%d:%d:%g and %g)' % (startDegrees, endDegrees, xRadius, yRadius), doc = doc)

def triangleCoordinates():
	xMaxGraph = 10
	xMinGraph = -10
	yMaxGraph = 10
	yMinGraph = -10

	changeChoices = [x for x in range(1, int((xMaxGraph-xMinGraph)/4-1))] 
	
	firstXChange = random.choice(changeChoices)
	firstYChange = random.choice([x for x in changeChoices if x not in [firstXChange, -1*firstXChange]]) #makes it not isosceles and prevents both being 0
	
	secondXChange = firstYChange
	secondYChange = -firstXChange
	
	xs = x1, x2, x3 = [0, 0 + firstXChange, firstXChange + secondXChange]
	ys = y1, y2, y3 = [0, 0 + firstYChange, firstYChange + secondYChange] 
	print(xs,ys)
	newX = []
	newY = []
	xChange = random.randint(xMinGraph-min(xs),xMaxGraph-max(xs))
	yChange = random.randint(yMinGraph-min(ys),yMaxGraph-max(ys))
	for itemX, itemY in zip(xs,ys):
		newX.append(itemX+xChange)
		newY.append(itemY+yChange)

	return newX, newY

def parallelogram(doc = None, verticesLabels = [], baseAngle = 30, baseDistance = 3, sideLength = 2):
	x4 = 0
	y4 = 0

	x3 = baseDistance
	y3 = 0

	x1 = -math.cos(math.radians(180-baseAngle))*sideLength
	y1 = math.sin(math.radians(180-baseAngle))*sideLength

	x2 = x1 + baseDistance
	y2 = y1

	com('draw (%g,%g) -- (%g,%g) -- (%g,%g) -- (%g,%g) -- cycle' % (x1,y1, x2, y2, x3, y3, x4, y4), doc = doc)
	return [x1, x2, x3, x4], [y1, y2, y3, y4]
def rectangle(doc = None, lengthValue = 10, widthValue = 4, labeled = True, rotate = 0):
	with doc.create(TikZ(options='rotate=%d' % rotate)):
		lengthScaled = 4 #cm
		widthScaled = widthValue * 4 / lengthValue
		if labeled == False:
			lengthValue = ""
			widthValue = ""

		if lengthValue == widthValue: #SQUARE - only label one side.
			com('draw (0,0) -| (%d,%d) node[pos=.25,below] {%d} node[pos=.75,right] {} -| (0,0)' % (lengthScaled, widthScaled, lengthValue), doc = doc)
		else:
			com('draw (0,0) -| (%d,%d) node[pos=.25,below] {%d} node[pos=.75,right] {%d} -| (0,0)' % (lengthScaled, widthScaled, lengthValue, widthValue), doc = doc)
		x1 = 0
		y1 = 0
		x2 = lengthScaled
		y2 = 0
		x3 = lengthScaled
		y3 = widthScaled
		com('coordinate (A) at (%g,%g) {}' % (x1,y1), doc = doc)
		com('coordinate (B) at (%g,%g) {}' % (x2,y2), doc = doc)
		com('coordinate (C) at (%g,%g) {}' % (x3,y3), doc = doc)
		com('tkzMarkRightAngle[draw=black,size=.2](A,B,C)', doc = doc)
def rightTriangle(doc = None, lengthValue = 10, widthValue = 4, labeled = True, rotate = 0, verticesLabels = []):
	print('rotate is', rotate)
	with doc.create(TikZ(options='rotate=%d' % rotate)):
		lengthScaled = 2 #cm #height
		widthScaled = widthValue * lengthScaled / lengthValue #base

		#for right angle
		x1 = 0
		y1 = 0
		x2 = widthScaled
		y2 = 0
		x3 = widthScaled
		y3 = lengthScaled
		com('coordinate (A) at (%g,%g) {}' % (x1,y1), doc = doc)
		com('coordinate (B) at (%g,%g) {}' % (x2,y2), doc = doc)
		com('coordinate (C) at (%g,%g) {}' % (x3,y3), doc = doc)
		com('tkzMarkRightAngle[draw=black,size=.2](A,B,C)', doc = doc)

		if labeled == False:
			lengthValue = ""
			widthValue = ""
		graphPolygon(doc = doc, x = [x1,x2,x3], y = [y1,y2,y3], annotations = verticesLabels, color = 'black', distanceAway = .5)
	

def determineConeVertices(radius, height, size = 'small'):
	#left point, center, right, height assuming 0 degrees
	leftPointX = 0
	leftPointY = 0
	if size == 'small':
		scaleFactor = 1
	elif size == "medium":
		scaleFactor = 2
	#let's dilate the figure so it's a certain height of 4cm, originalHeight * x = 4cm, so 4cm/originalHeight
	#new radius = originalHeight * x = 4, so scale factor is 4/originalHeight
	scaledHeight = scaleFactor
	scaledRadius = radius*scaleFactor/height

	rightPointX = leftPointX + scaledRadius*2
	rightPointY = 0

	centerPointX = leftPointX + scaledRadius
	centerPointY = 0

	heightPointX = centerPointX
	heightPointY = centerPointY + scaledHeight

	coordinates = {'left':[leftPointX, leftPointY], 
	'right':[rightPointX, rightPointY], 
	'center':[centerPointX, centerPointY], 
	'height':[heightPointX, heightPointY]
	}

	return coordinates

def determineCylinderVertices(radius, height, size = 'small'):
	#left point, center, right, height assuming 0 degrees
	leftPointX = 0
	leftPointY = 0
	if size == 'small':
		scaleFactor = 1
	elif size == "medium":
		scaleFactor = 2

	#let's dilate the figure so it's a certain height of 4cm, originalHeight * x = 4cm, so 4cm/originalHeight
	#new radius = originalHeight * x = 4, so scale factor is 4/originalHeight
	scaledHeight = scaleFactor
	scaledRadius = radius*scaleFactor/height

	rightPointX = leftPointX + scaledRadius*2
	rightPointY = 0

	centerPointX = leftPointX + scaledRadius
	centerPointY = 0

	heightPointX = centerPointX
	heightPointY = centerPointY + scaledHeight

	topLeftPointX = leftPointX
	topLeftPointY = leftPointY + heightPointY

	topRightPointX = rightPointX
	topRightPointY = rightPointY + heightPointY

	coordinates = {'left':[leftPointX, leftPointY], 
	'right':[rightPointX, rightPointY], 
	'center':[centerPointX, centerPointY], 
	'height':[heightPointX, heightPointY],
	'topLeft':[topLeftPointX, topLeftPointY],
	'topRight':[topRightPointX, topRightPointY]
	}

	return coordinates

def determineSphereVertices(radius, size = 'small'):
	#left point, center, right, height assuming 0 degrees
	leftPointX = 0
	leftPointY = 0
	if size == 'small':
		scaleFactor = 1
	elif size == "medium":
		scaleFactor = 2
	#let's dilate the figure so it's a certain height of 4cm, originalHeight * x = 4cm, so 4cm/originalHeight
	#new radius = originalHeight * x = 4, so scale factor is 4/originalHeight
	scaledRadius = scaleFactor
	scaledDiameter = 2 * scaledRadius

	rightPointX = leftPointX + scaledRadius*2
	rightPointY = 0

	centerPointX = leftPointX + scaledRadius
	centerPointY = 0

	coordinates = {'left':[leftPointX, leftPointY], 
	'right':[rightPointX, rightPointY], 
	'center':[centerPointX, centerPointY], 
	}

	return coordinates	

def determinePrismVertices(length = 5, width = 10, height = 15, typeOfPrism = 'rectangle', size = 'small'):
  #start on front face bottom left corner with a front facing look

  if size == 'small':
    scaleFactor = 1
  elif size == "medium":
    scaleFactor = 2

  #original length = scale factor, so 
  #Original length * anotherFactor = scale Factor
  #scaleFactor/orignal length is what we multiply everything else by 
  scaledLength = scaleFactor
  scaledWidth = scaleFactor / length * width
  scaledHeight = scaleFactor / length * height

  if typeOfPrism == 'cube':
    scaledWidth = scaledLength
    scaledHeight = scaledLength

  coordinates = {}

  coordinates['scaledLength'] = scaledLength
  #Testing *2 to make it look more cube like
  coordinates['scaledWidth'] = scaledWidth
  coordinates['scaledHeight'] = scaledHeight

  #Make rectangle on paper length and height
  coordinates[1] = (0,0)
  coordinates[2] = (scaledLength, 0) #X is length
  coordinates[3] = (scaledLength, scaledHeight) #Z is width
  coordinates[4] = (0, scaledHeight)

  #xPush and yPush are "essentially" the width
  #same as 1,2,3,4 but pushed farther back but with an angle of 45 degrees
  #cos(45) and sin(45) = sqrt(2)/2
  xPush = (2**(1/2)/2)*scaledWidth
  yPush = (2**(1/2)/2)*scaledWidth

  #back and up
  coordinates[5] = (-1*xPush, yPush) #this is the tip
  coordinates[6] = (scaledLength-xPush, yPush)
  coordinates[7] = (scaledLength-xPush, scaledHeight+yPush)
  coordinates[8] = (-1*xPush, scaledHeight+yPush)

  return coordinates

def determinePyramidVertices(typeOfPyramid = 'rectangle', length = 10, width = 10, height = 10, size = 'small'):
	#start on front face bottom left corner with a front facing look

	if size == 'small':
		scaleFactor = 1
	elif size == "medium":
		scaleFactor = 2

	#originalLength * x = scaleFactor, so 
	scaledLength = scaleFactor
	scaledWidth = scaleFactor / length * width
	scaledHeight = scaleFactor / length * height

	if typeOfPyramid == 'square':
		scaledWidth = scaledLength
		scaledHeight = scaledLength

	coordinates = {}

	coordinates['scaledLength'] = scaledLength
	#Testing *2 to make it look more cube like
	coordinates['scaledWidth'] = scaledWidth
	coordinates['scaledHeight'] = scaledHeight

	if scaledHeight < 2*scaledLength:
		scaledHeight *= 2

	#draw slanted base with length and width
	coordinates[1] = (0,0)
	coordinates[2] = (scaledLength, 0) #X is length
	coordinates[3] = (scaledLength, scaledWidth) #Z is width
	coordinates[4] = (0,scaledWidth)

	#top of pyramid
	coordinates[5] = (scaledLength/2, scaledHeight)

	#center of bottom shape
	coordinates[6] = (scaledLength/2,scaledWidth/2)

	#ending coordinate for altitude right angle
	coordinates[7] = (0, scaledWidth/2)
	return coordinates

def lineSegment(x1, y1, x2, y2, dashed = False, doc = None):
	if dashed == True:
		dashedString = '[dashed]'
	else:
		dashedString = ""
	com('draw %s (%g,%g) -- (%g,%g)' % (dashedString, x1, y1, x2, y2), doc = doc)

def rightAngle(x1,y1,x2,y2,x3,y3, size = .2, doc = None):
	#requires \usetikzlibrary{calc}
	#\usepackage{tkz-euclide}
	#\usetkzobj{all}
	com('coordinate (A) at (%g,%g) {}' % (x1,y1), doc = doc)
	com('coordinate (B) at (%g,%g) {}' % (x2,y2), doc = doc)
	com('coordinate (C) at (%g,%g) {}' % (x3,y3), doc = doc)
	com('tkzMarkRightAngle[draw=black,size=%g](A,B,C)' % (size), doc = doc)

def node(x1, y1, label, position = '', doc = None):
	nodeXChange = 0
	nodeYChange = 0
	
	nodeDist = .1
	if position == "below":
		nodeYChange = -1 * nodeDist
	elif position == "above":
		nodeYChange = 1 * nodeDist
	elif position == "left":
		nodeXChange = -1 * nodeDist
	elif position == "right":
		nodeXChange = 1 * nodeDist

	nodeX = x1 + nodeXChange
	nodeY = y1 + nodeYChange
	com('node at (%g,%g) {\small $%s$}' % (nodeX, nodeY, label), doc = doc)

def circle(centerX, centerY, radius, doc = None, type = 'circle'):
	if type == 'circle':
		com('draw (%g,%g) circle (%g)' % (centerX, centerY, radius), doc = doc)
	elif type == 'semi':
		com('clip (%g,%g) rectangle (%g,%g)' % (centerX-radius, centerY, centerX+radius, centerX+radius), doc = doc)
		com('draw (%g,%g) circle (%g)' % (centerX, centerY, radius), doc = doc)
		com('draw (%g,%g) -- (%g,%g)' % (centerX-radius, centerY, centerX+radius, centerY), doc = doc)

def slope(x1, y1, x2, y2):
	numerator = y2 - y1
	denominator = x2 - x1
	return numerator, denominator

def midpoint(x1, y1, x2, y2):
	midX = (x2 - x1)/2
	midY = (y2 - y1)/2
	return midX, midY

def point(x1, y1, doc = None):
	com('draw[black,fill=black] (%g,%g) circle (.1ex)' % (x1, y1), doc = doc)

def labelWholeSide(x1, y1, x2, y2, nodePosition, nodeLabel, doc = None):
	#braces are drawn always up starting at first point, so will face upleft if (0,0) -- (4,4)
	#but down if (4,4) -- (0,0)

	nodeXChange = 0
	nodeYChange = 0
	
	nodeDist = .1
	if nodePosition == "below":
		nodeYChange = -1 * nodeDist
	elif nodePosition == "above":
		nodeYChange = 1 * nodeDist
	elif nodePosition == "left":
		nodeXChange = -1 * nodeDist
	elif nodePosition == "right":
		nodeXChange = 1 * nodeDist

	nodeX = (x1 + x2)/2 + nodeXChange
	nodeY = (y1+y2)/2 + nodeYChange
	# com('draw[|-|] (%g,%g) -- (%g,%g) node [midway, %s] {%s}' % (x1, y1, x2, y2, nodePosition, nodeLabel), doc = doc)
	com('draw[|-|] (%g,%g) -- (%g,%g)' % (x1, y1, x2, y2), doc = doc)
	com('node at (%g,%g) {%s}' % (nodeX, nodeY, nodeLabel), doc=doc)


def roundGivenString(string = 'tenth', value = 0):
	if string == 'tenth':
		return round(value,1)
	elif string == 'hundredth':
		return round(value,2)
	elif string == 'thousandth':
		return round(value,3)
	elif string == 'whole number':
		return int(round(value,0))
	elif string == 'in terms of pi':
		#fractions etc???
		return value/math.pi

def cone(options = 'rotate=0, scale=1', doc = None, wholeFigureRotation = 0, heightDrawn = True, radiusDrawn = True, diameterDrawn = False, radiusLabeledOnDiagram = True, heightLabeledOnDiagram = True, diameterLabeledOnDiagram = False, radiusValue = 2, diameterValue = 4, heightValue = 4, slantHeightLabeledOnDiagram = False):
	'''
	wholeFigureRotation = 0, 90, 180, 270 counterclockwise orientation of whole figure
	ADD THIS OPTION TO TIKZ rotate=wholeFigureRotation
	radius/diameter/height Labeled - a value is placed next to them
	radius/diameter/height value - their value is placed next to them if not default, will also use to determine placements
	radius/diameter/height drawn - they are drawn on the figure
	'''
	with doc.create(TikZ(options=options)): # length, length makes the graph square
		#define 4 points - use radius, height etc - maybe have minimum etc
		conePoints = determineConeVertices(radius = radiusValue, height = heightValue, size = 'small')

		#scale height 4cm
		scaledRadius = conePoints['center'][0] - conePoints['left'][0]
		scaledHeight = conePoints['height'][1] - conePoints['center'][1]
		slantHeight = int(heightValue + 1) #not realistic but good enough

		#create forward dark arc
		arc(dashed = False, startDegrees = 180, endDegrees = 360, xRadius = scaledRadius, yRadius = .2*scaledRadius, startPoint = '(0,0)', doc = doc)

		#create backward dashed arc
		arc(dashed = True, startDegrees = 180, endDegrees = 0, xRadius = scaledRadius, yRadius = .2*scaledRadius, startPoint = '(0,0)', doc = doc)

		#create slants
		lineSegment(x1 = conePoints['left'][0], y1 = conePoints['left'][1], x2 = conePoints['height'][0], y2 = conePoints['height'][1], doc = doc)
		lineSegment(x1 = conePoints['right'][0], y1 = conePoints['right'][1], x2 = conePoints['height'][0], y2 = conePoints['height'][1], doc = doc)

		if heightDrawn == True:
			#create height
			lineSegment(x1 = conePoints['height'][0], y1 = conePoints['height'][1], x2 = conePoints['center'][0], y2 = conePoints['center'][1], dashed = True, doc = doc)

			#create right angle, random between left and right, rightAngle will do the correct size
			rightAngleDirection = random.choice(['left','right'])
			rightAngle(x1 = conePoints['height'][0], y1 = conePoints['height'][1], x2 = conePoints['center'][0], y2 = conePoints['center'][1], x3 = conePoints[rightAngleDirection][0], y3 = conePoints[rightAngleDirection][1], doc = doc)

		if radiusDrawn == True:
			#create radius dashed, could do left radius at some point
			radiusDirection = random.choice(['left','right'])
			lineSegment(x1 = conePoints['center'][0], y1 = conePoints['center'][1], x2 = conePoints[radiusDirection][0], y2 = conePoints[radiusDirection][1], dashed = True, doc = doc)

		if radiusLabeledOnDiagram == True:
			#label radius midway - coordinate of point that is midway but higher
			if radiusDirection == 'left':
				labelWholeSide(x2 = conePoints['left'][0], x1 = conePoints['center'][0], y2 = conePoints['left'][1] - .2*scaledRadius -.2, y1 = conePoints['center'][1] - .2*scaledRadius-.2, nodePosition = 'below', nodeLabel = str(diameterValue), doc = doc)
			else:
				labelWholeSide(x2 = conePoints['center'][0], x1 = conePoints['right'][0], y2 = conePoints['center'][1] - .2*scaledRadius -.2, y1 = conePoints['right'][1] - .2*scaledRadius-.2, nodePosition = 'below', nodeLabel = str(diameterValue), doc = doc)

		if slantHeightLabeledOnDiagram == True:
			#label slant height left or right
			slantDirection = random.choice(['left','right'])
			node(x1 = ( conePoints[slantDirection][0] + conePoints['height'][0] ) / 2, y1 = ( conePoints[slantDirection][1] + conePoints['height'][1] ) / 2, label = str(slantHeight), position = slantDirection, doc = doc)

		if diameterLabeledOnDiagram == True:
			#label diameter with another arc or thingy - coordinate of point that is midway(so center) and lower cause height is in way
			labelWholeSide(x2 = conePoints['left'][0], x1 = conePoints['right'][0], y2 = conePoints['left'][1] - .2*scaledRadius -.2, y1 = conePoints['right'][1] - .2*scaledRadius-.2, nodePosition = 'below', nodeLabel = str(diameterValue), doc = doc)

		if diameterDrawn == True:
			#create diameter dashed
			lineSegment(x1 = conePoints['left'][0], y1 = conePoints['left'][1], x2 = conePoints['right'][0], y2 = conePoints['right'][1], dashed = True, doc = doc)
			
		if heightLabeledOnDiagram == True:
			#label height midway - coordinate of point that is midway and right
			node(x1 = conePoints['center'][0], y1 = scaledHeight/2, label = str(heightValue), position  = 'right', doc = doc)

def cylinderHemisphere(options = 'rotate=0, scale=1', doc = None, wholeFigureRotation = 0, radiusDrawn = True, diameterDrawn = False, radiusLabeledOnDiagram = True, heightLabeledOnDiagram = True, diameterLabeledOnDiagram = False, radiusValue = 2, diameterValue = 4, heightValue = 4):
	'''
	wholeFigureRotation = 0, 90, 180, 270 counterclockwise orientation of whole figure
	ADD THIS OPTION TO TIKZ rotate=wholeFigureRotation
	drawn...thing is drawn
	value is used to make the picture to scale
	'''
	with doc.create(TikZ(options=options)): # length, length makes the graph square
		#define 4 points - use radius, height etc - maybe have minimum etc
		cylinderPoints = determineCylinderVertices(radius = radiusValue, height = heightValue, size = 'small')
		spherePoints = determineSphereVertices(radius = radiusValue)

		#translate sphere coordinates to top of cylinder, so left will go up height
		spherePoints['left'][1] = cylinderPoints['topLeft'][1]
		spherePoints['right'][1] = cylinderPoints['topRight'][1]
		spherePoints['center'][1] = cylinderPoints['topLeft'][1]

		#scale height 4cm
		scaledRadius = cylinderPoints['center'][0] - cylinderPoints['left'][0]
		scaledHeight = cylinderPoints['height'][1] + scaledRadius

		#create forward dark arc - BOTTOM, counterclockwise
		arc(dashed = False, startDegrees = 180, endDegrees = 360, xRadius = scaledRadius, yRadius = .2*scaledRadius, startPoint = '(0,0)', doc = doc)

		#create backward dashed arc - BOTTOM
		arc(dashed = True, startDegrees = 180, endDegrees = 0, xRadius = scaledRadius, yRadius = .2*scaledRadius, startPoint = '(0,0)', doc = doc)

		#create forward dark arc on TOP
		arc(dashed = True, startDegrees = 180, endDegrees = 360, xRadius = scaledRadius, yRadius = .2*scaledRadius, startPoint = '(0,%g)' % (scaledHeight-scaledRadius), doc = doc)

		#create forward dark arc on TOP
		arc(dashed = True, startDegrees = 180, endDegrees = 0, xRadius = scaledRadius, yRadius = .2*scaledRadius, startPoint = '(0,%g)' % (scaledHeight-scaledRadius), doc = doc)

		#create heights left and right
		lineSegment(x1 = cylinderPoints['left'][0], y1 = cylinderPoints['left'][1], x2 = cylinderPoints['topLeft'][0], y2 = cylinderPoints['topLeft'][1], doc = doc)
		lineSegment(x1 = cylinderPoints['right'][0], y1 = cylinderPoints['right'][1], x2 = cylinderPoints['topRight'][0], y2 = cylinderPoints['topRight'][1], doc = doc)

		#create top arc of hemisphere, semi circle
		arc(startDegrees = 180, endDegrees = 0, xRadius = scaledRadius, yRadius = scaledRadius, startPoint = '(0,%g)' % (scaledHeight-scaledRadius), doc = doc)

		if radiusDrawn == True:
			#create radius dashed, could do left radius at some point
			radiusDirection = random.choice(['left','right'])
			lineSegment(x1 = cylinderPoints['center'][0], y1 = cylinderPoints['center'][1], x2 = cylinderPoints[radiusDirection][0], y2 = cylinderPoints[radiusDirection][1], dashed = True, doc = doc)
			point(x1 = cylinderPoints['center'][0], y1 = cylinderPoints['center'][1], doc = doc)


		if radiusLabeledOnDiagram == True:
			#label radius midway - coordinate of point that is midway but higher
			if radiusDirection == 'left':
				node(x1 = cylinderPoints['left'][0], y1 = 0, label = str(radiusValue), position = 'below', doc = doc)
			else:
				node(x1 = cylinderPoints['right'][0], y1 = 0, label = str(radiusValue), position = 'below', doc = doc)

		#height labeled
		if heightLabeledOnDiagram == True:
			heightSide = random.choice(['right'])
			labelWholeSide(x2 = cylinderPoints[heightSide][0]+scaledRadius*.2, x1 = cylinderPoints[heightSide][0]+.2*scaledRadius, y2 = cylinderPoints[heightSide][1]+scaledHeight, y1 = cylinderPoints[heightSide][1], nodePosition = heightSide, nodeLabel = str(heightValue), doc = doc)

		if diameterLabeledOnDiagram == True:
			#label diameter with another arc or thingy - coordinate of point that is midway(so center) and lower cause height is in way
			labelWholeSide(x2 = cylinderPoints['left'][0], x1 = cylinderPoints['right'][0], y2 = cylinderPoints['left'][1] - .2*scaledRadius-.2, y1 = cylinderPoints['right'][1] - .2*scaledRadius-.2, nodePosition = 'below', nodeLabel = str(diameterValue), doc = doc)

		if diameterDrawn == True:
			#create diameter dashed
			lineSegment(x1 = cylinderPoints['left'][0], y1 = cylinderPoints['left'][1], x2 = cylinderPoints['right'][0], y2 = cylinderPoints['right'][1], dashed = True, doc = doc)

def cylinder(options = 'rotate=0, scale=1', doc = None, wholeFigureRotation = 0, radiusDrawn = True, diameterDrawn = False, radiusLabeledOnDiagram = True, heightLabeledOnDiagram = True, diameterLabeledOnDiagram = False, radiusValue = 2, diameterValue = 4, heightValue = 4):
	'''
	wholeFigureRotation = 0, 90, 180, 270 counterclockwise orientation of whole figure
	ADD THIS OPTION TO TIKZ rotate=wholeFigureRotation
	drawn...thing is drawn
	value is used to make the picture to scale
	'''
	with doc.create(TikZ(options=options)): # length, length makes the graph square
		#define 4 points - use radius, height etc - maybe have minimum etc
		cylinderPoints = determineCylinderVertices(radius = radiusValue, height = heightValue, size = 'small')

		#scale height 4cm
		scaledRadius = cylinderPoints['center'][0] - cylinderPoints['left'][0]
		scaledHeight = cylinderPoints['height'][1] - cylinderPoints['center'][1]

		#create forward dark arc - BOTTOM, counterclockwise
		arc(dashed = False, startDegrees = 180, endDegrees = 360, xRadius = scaledRadius, yRadius = .2*scaledRadius, startPoint = '(0,0)', doc = doc)

		#create backward dashed arc - BOTTOM
		arc(dashed = True, startDegrees = 180, endDegrees = 0, xRadius = scaledRadius, yRadius = .2*scaledRadius, startPoint = '(0,0)', doc = doc)

		#create forward dark arc on TOP
		arc(dashed = False, startDegrees = 180, endDegrees = 360, xRadius = scaledRadius, yRadius = .2*scaledRadius, startPoint = '(0,%g)' % scaledHeight, doc = doc)

		#create forward dark arc on TOP
		arc(dashed = False, startDegrees = 180, endDegrees = 0, xRadius = scaledRadius, yRadius = .2*scaledRadius, startPoint = '(0,%g)' % scaledHeight, doc = doc)

		#create heights left and right
		lineSegment(x1 = cylinderPoints['left'][0], y1 = cylinderPoints['left'][1], x2 = cylinderPoints['topLeft'][0], y2 = cylinderPoints['topLeft'][1], doc = doc)
		lineSegment(x1 = cylinderPoints['right'][0], y1 = cylinderPoints['right'][1], x2 = cylinderPoints['topRight'][0], y2 = cylinderPoints['topRight'][1], doc = doc)

		if radiusDrawn == True:
			#create radius dashed, could do left radius at some point
			radiusDirection = random.choice(['left','right'])
			lineSegment(x1 = cylinderPoints['center'][0], y1 = cylinderPoints['center'][1], x2 = cylinderPoints[radiusDirection][0], y2 = cylinderPoints[radiusDirection][1], dashed = True, doc = doc)
			point(x1 = cylinderPoints['center'][0], y1 = cylinderPoints['center'][1], doc = doc)


		if radiusLabeledOnDiagram == True:
			if radiusDirection == 'left':
				labelWholeSide(x2 = cylinderPoints['left'][0], x1 = cylinderPoints['center'][0], y2 = cylinderPoints['left'][1] - .2*scaledRadius-.2, y1 = cylinderPoints['center'][1] - .2*scaledRadius-.2, nodePosition = 'below', nodeLabel = str(radiusValue), doc = doc)
			else:
				labelWholeSide(x2 = cylinderPoints['right'][0], x1 = cylinderPoints['center'][0], y2 = cylinderPoints['right'][1] - .2*scaledRadius-.2, y1 = cylinderPoints['center'][1] - .2*scaledRadius-.2, nodePosition = 'below', nodeLabel = str(radiusValue), doc = doc)

		#height labeled
		if heightLabeledOnDiagram == True:
			heightSide = random.choice(['left','right'])
			node(x1 = cylinderPoints[heightSide][0], y1 = cylinderPoints[heightSide][1] + scaledHeight/2, label = str(heightValue), position = heightSide, doc = doc)

		if diameterLabeledOnDiagram == True:
			#label diameter with another arc or thingy - coordinate of point that is midway(so center) and lower cause height is in way
			labelWholeSide(x2 = cylinderPoints['left'][0], x1 = cylinderPoints['right'][0], y2 = cylinderPoints['left'][1] - .2*scaledRadius-.2, y1 = cylinderPoints['right'][1] - .2*scaledRadius-.2, nodePosition = 'below', nodeLabel = str(diameterValue), doc = doc)

		if diameterDrawn == True:
			#create diameter dashed
			lineSegment(x1 = cylinderPoints['left'][0], y1 = cylinderPoints['left'][1], x2 = cylinderPoints['right'][0], y2 = cylinderPoints['right'][1], dashed = True, doc = doc)
			

def sphere(options = 'rotate=0, scale=1', doc = None, wholeFigureRotation = 0, radiusDrawn = True, diameterDrawn = False, radiusLabeledOnDiagram = True, diameterLabeledOnDiagram = False, radiusValue = 2, diameterValue = 4):
	'''
	wholeFigureRotation = 0, 90, 180, 270 counterclockwise orientation of whole figure
	ADD THIS OPTION TO TIKZ rotate=wholeFigureRotation
	radius/diameter/height Labeled - a value is placed next to them
	radius/diameter/height value - their value is placed next to them if not default, will also use to determine placements
	radius/diameter/height drawn - they are drawn on the figure
	'''
	with doc.create(TikZ(options=options)): # length, length makes the graph square
		#define 4 points - use radius, height etc - maybe have minimum etc
		spherePoints = determineSphereVertices(radius = radiusValue, size = 'small')

		#scale height 4cm
		scaledRadius = spherePoints['center'][0] - spherePoints['left'][0]

		#create forward dark arc - middle
		arc(dashed = False, startDegrees = 180, endDegrees = 360, xRadius = scaledRadius, yRadius = .2*scaledRadius, startPoint = '(0,0)', doc = doc)

		#create backward dashed arc - middle
		arc(dashed = True, startDegrees = 180, endDegrees = 0, xRadius = scaledRadius, yRadius = .2*scaledRadius, startPoint = '(0,0)', doc = doc)


		circle(centerX = spherePoints['center'][0], centerY = 0, radius = scaledRadius, doc = doc)

		#center
		point(x1 = spherePoints['center'][0], y1 = 0)

		if radiusDrawn == True:
			#create radius dashed, could do left radius at some point
			radiusDirection = random.choice(['left','right'])
			lineSegment(x1 = spherePoints['center'][0], y1 = spherePoints['center'][1], x2 = spherePoints[radiusDirection][0], y2 = spherePoints[radiusDirection][1], dashed = True, doc = doc)

		if radiusLabeledOnDiagram == True:
			#label radius midway - coordinate of point that is midway but higher
			if radiusDirection == 'left':
				node(x1 = spherePoints['left'][0] + scaledRadius*.5, y1 = 0, label = str(radiusValue), position = 'below', doc = doc)
			else:
				node(x1 = spherePoints['right'][0] - scaledRadius*.5, y1 = 0, label = str(radiusValue), position = 'below', doc = doc)

		if diameterLabeledOnDiagram == True:
			#label diameter with another arc or thingy - coordinate of point that is midway(so center) and lower cause height is in way
			node(x1 = spherePoints['left'][0] + scaledRadius, y1 = spherePoints["left"][1], label = str(diameterValue), position = 'below', doc = doc)

		if diameterDrawn == True:
			#create diameter dashed
			lineSegment(x1 = spherePoints['left'][0], y1 = spherePoints['left'][1], x2 = spherePoints['right'][0], y2 = spherePoints['right'][1], dashed = True, doc = doc)

def rectangularPrism(options = 'rotate=0, scale=1', doc = None, wholeFigureRotation = 0, widthValue = 3, widthLabeledOnDiagram = True, heightValue = 30, heightLabeledOnDiagram = True, lengthValue = 30, lengthLabeledOnDiagram = True, baseRotation = 0):
	'''
	wholeFigureRotation = 0, 90, 180, 270 counterclockwise orientation of whole figure
	ADD THIS OPTION TO TIKZ rotate=wholeFigureRotation
	'''
	with doc.create(TikZ(options=options)): # length, length makes the graph square
		prismCoords = determinePrismVertices(length = lengthValue, width = widthValue, height = heightValue, typeOfPrism = 'rectangle')
		#Draw bottom shape, draw top shape, connect with 4 lines
		com('draw %s -- %s -- %s -- %s -- cycle' % (str(prismCoords[1]), str(prismCoords[2]), str(prismCoords[3]), str(prismCoords[4])), doc = doc)
		com('draw %s -- %s -- %s -- %s -- cycle' % (str(prismCoords[5]), str(prismCoords[6]), str(prismCoords[7]), str(prismCoords[8])), doc = doc)
		com('draw %s -- %s' % (str(prismCoords[1]), str(prismCoords[5])), doc = doc)
		com('draw %s -- %s' % (str(prismCoords[2]), str(prismCoords[6])), doc = doc)
		com('draw %s -- %s' % (str(prismCoords[3]), str(prismCoords[7])), doc = doc)
		com('draw %s -- %s' % (str(prismCoords[4]), str(prismCoords[8])), doc = doc)

		if lengthLabeledOnDiagram == True: #X
			# com('draw %s -- node[below,sloped]{%s}%s' % (str(prismCoords[4]), str(lengthValue), str(prismCoords[3])), doc = doc)
			node(x1 = (prismCoords[1][0] + prismCoords[2][0])/2 , y1 = (prismCoords[1][1] + prismCoords[2][1])/2, position = "below", label = str(lengthValue), doc=doc)
			
		if widthLabeledOnDiagram == True: #Z
			# com('draw %s -- node[below,sloped]{%s}%s' % (str(prismCoords[3]), str(widthValue), str(prismCoords[2])), doc = doc)
			node(x1 = (prismCoords[1][0] + prismCoords[5][0])/2 , y1 = (prismCoords[1][1] + prismCoords[5][1])/2, position = "left", label = str(widthValue),doc=doc)
		
		if heightLabeledOnDiagram == True: #Y
			# com('draw %s -- node[below,sloped]{%s}%s' % (str(prismCoords[2]), str(heightValue), str(prismCoords[6]) ), doc = doc)
			node(x1 = (prismCoords[2][0] + prismCoords[3][0])/2 , y1 = (prismCoords[2][1] + prismCoords[3][1])/2, position = "right", label = str(heightValue),doc=doc)
		
def cube(options = 'rotate=0, scale=1', doc = None, wholeFigureRotation = 0, sideValue = 10, sideLabeledOnDiagram = True, baseRotation = 0):
	'''
	wholeFigureRotation = 0, 90, 180, 270 counterclockwise orientation of whole figure
	ADD THIS OPTION TO TIKZ rotate=wholeFigureRotation
	'''	
	with doc.create(TikZ(options=options)): # length, length makes the graph square
		prismCoords = determinePrismVertices(length = sideValue, width = sideValue, height = sideValue, typeOfPrism = 'cube')

		#Draw bottom shape, draw top shape, connect with 4 lines

		com('draw %s -- %s -- %s -- %s -- cycle' % (str(prismCoords[1]), str(prismCoords[2]), str(prismCoords[3]), str(prismCoords[4])), doc = doc)
		com('draw %s -- %s -- %s -- %s -- cycle' % (str(prismCoords[5]), str(prismCoords[6]), str(prismCoords[7]), str(prismCoords[8])), doc = doc)

		com('draw %s -- %s' % (str(prismCoords[1]), str(prismCoords[5])), doc = doc)
		com('draw %s -- %s' % (str(prismCoords[2]), str(prismCoords[6])), doc = doc)
		com('draw %s -- %s' % (str(prismCoords[3]), str(prismCoords[7])), doc = doc)
		com('draw %s -- %s' % (str(prismCoords[4]), str(prismCoords[8])), doc = doc)

		'''
		com('draw %s -- %s -- %s -- %s -- %s -- %s %s -- %s -- %s -- %s -- %s -- %s' % (coordA, coordB, coordC, coordG, coordF, coordB, coordA, coordE, coordF, coordG, coordH, coordE), doc = doc)
		com('draw %s -- %s -- %s %s -- %s' % (coordA, coordD, coordC, coordD, coordH), doc = doc)
		'''
		if sideLabeledOnDiagram == True:
			sideToLabel = random.choice([1,2,3])

			if sideToLabel == 1: #X
				node(x1 = (prismCoords[1][0]+prismCoords[2][0])/2, y1 = (prismCoords[1][1]+prismCoords[2][1])/2, label = f"{sideValue}", position="below", doc=doc)
			elif sideToLabel == 2: #Z
				node(x1 = (prismCoords[2][0]+prismCoords[3][0])/2, y1 = (prismCoords[2][1]+prismCoords[3][1])/2, label = f"{sideValue}", position="right", doc=doc)
			elif sideToLabel == 3: #Y
				node(x1 = (prismCoords[1][0]+prismCoords[5][0])/2, y1 = (prismCoords[1][1]+prismCoords[5][1])/2, label = f"{sideValue}", position="left", doc=doc)
		
def regularPyramid(options = 'rotate=90, scale=1', doc = None, wholeFigureRotation = 0, heightValue = 30, heightLabeledOnDiagram = True, sideValue = 10, sideLabeledOnDiagram = True):

	with doc.create(TikZ(options=options)): # length, length makes the graph square
		pyramidCoords = determinePyramidVertices(length = sideValue, width = sideValue, height = heightValue, typeOfPyramid = 'square')
		
		#Draw bottom shape, draw in height with right angle, draw 4 connecting lines
		
		#BOTTOM SHAPE
		com('draw %s -- %s -- %s -- %s -- cycle' % (str(pyramidCoords[1]), str(pyramidCoords[2]), str(pyramidCoords[3]), str(pyramidCoords[4])), doc = doc)

		#draw 4 lines to height
		com('draw %s -- %s' % (str(pyramidCoords[1]), str(pyramidCoords[5])), doc = doc)
		com('draw %s -- %s' % (str(pyramidCoords[2]), str(pyramidCoords[5])), doc = doc)
		com('draw %s -- %s' % (str(pyramidCoords[3]), str(pyramidCoords[5])), doc = doc)
		com('draw %s -- %s' % (str(pyramidCoords[4]), str(pyramidCoords[5])), doc = doc)

		#draw height with right angle - top of pyramid directly down
		com('draw[dash pattern=on 3pt off 5pt] %s -- %s' % (str(pyramidCoords[5]), str(pyramidCoords[6])), doc = doc)

		#right angle
		com('coordinate (A) at %s {}' % (str(pyramidCoords[5])), doc = doc)
		com('coordinate (B) at %s {}' % (str(pyramidCoords[6])), doc = doc)
		com('coordinate (C) at %s {}' % (str(pyramidCoords[7])), doc = doc)
		com('tkzMarkRightAngle[draw=black, size = .1](A,B,C)', doc = doc)
		com('draw[dash pattern=on 3pt off 5pt] %s -- %s' % (str(pyramidCoords[6]), str(pyramidCoords[7])), doc=doc)

		if heightLabeledOnDiagram == True:
			com('draw[dash pattern=on 3pt off 5pt] %s -- %s' % (str(pyramidCoords[5]), str(pyramidCoords[6])), doc = doc)
			node(x1 = (pyramidCoords[5][0] + pyramidCoords[6][0])/2, y1 = (pyramidCoords[5][1] + pyramidCoords[6][1])/2, label = str(heightValue), position = "right", doc=doc)

		if sideLabeledOnDiagram == True:
			sideToLabel = random.choice([1,2])

			if sideToLabel == 1: #X
				# com('draw %s -- %s' % (str(pyramidCoords[1]), str(pyramidCoords[2])), doc = doc)
				node(x1 = (pyramidCoords[1][0] + pyramidCoords[2][0])/2, y1 = (pyramidCoords[1][1] + pyramidCoords[2][1])/2, label = str(sideValue), position = "below", doc=doc)
			
			elif sideToLabel == 2: #Z
				# com('draw %s -- %s' % (str(pyramidCoords[1]), str(pyramidCoords[2])), doc = doc)
				node(x1 = (pyramidCoords[2][0] + pyramidCoords[3][0])/2, y1 = (pyramidCoords[2][1] + pyramidCoords[3][1])/2, label = str(sideValue), position = "right", doc=doc)
			
def rectangularPyramid(options = 'rotate=0, scale=1', doc = None, wholeFigureRotation = 0, heightValue = 30, heightLabeledOnDiagram = True, lengthValue = 10, lengthLabeledOnDiagram = True, widthValue = 10, widthLabeledOnDiagram = True):
	with doc.create(TikZ(options=options)): # length, length makes the graph square
		pyramidCoords = determinePyramidVertices(length = lengthValue, width = widthValue, height = heightValue, typeOfPyramid = 'rectangle')
		
		#Draw bottom shape, draw in height with right angle, draw 4 connecting lines
		
		#BOTTOM SHAPE
		com('draw %s -- %s -- %s -- %s -- cycle' % (str(pyramidCoords[1]), str(pyramidCoords[2]), str(pyramidCoords[3]), str(pyramidCoords[4])), doc = doc)

		#draw 4 lines to height
		com('draw %s -- %s' % (str(pyramidCoords[1]), str(pyramidCoords[5])), doc = doc)
		com('draw %s -- %s' % (str(pyramidCoords[2]), str(pyramidCoords[5])), doc = doc)
		com('draw %s -- %s' % (str(pyramidCoords[3]), str(pyramidCoords[5])), doc = doc)
		com('draw %s -- %s' % (str(pyramidCoords[4]), str(pyramidCoords[5])), doc = doc)

		#draw height with right angle
		com('draw[dash pattern=on 3pt off 5pt] %s -- %s' % (str(pyramidCoords[5]), str(pyramidCoords[6])), doc = doc)

		#right angle
		com('coordinate (A) at %s {}' % (str(pyramidCoords[5])), doc = doc)
		com('coordinate (B) at %s {}' % (str(pyramidCoords[6])), doc = doc)
		com('coordinate (C) at %s {}' % (str(pyramidCoords[7])), doc = doc)
		com('tkzMarkRightAngle[size = .1](A,B,C)', doc = doc)

		if heightLabeledOnDiagram == True:
			com('draw[dash pattern=on 3pt off 5pt] %s -- node[right]{%s}%s' % (str(pyramidCoords[5]), str(heightValue), str(pyramidCoords[6])), doc = doc)

		if widthLabeledOnDiagram == True:
			com('draw %s -- node[below,sloped]{%s}%s' % (str(pyramidCoords[2]), str(widthValue), str(pyramidCoords[3])), doc = doc)
		
		if lengthLabeledOnDiagram == True:
				com('draw %s -- node[below,sloped]{%s}%s' % (str(pyramidCoords[3]), str(lengthValue), str(pyramidCoords[4])), doc = doc)
		
def triangularPyramid(options = 'rotate=0, scale=1', doc = None, wholeFigureRotation = 0, heightValue = 30, heightLabeledOnDiagram = True, lengthValue = 10, lengthLabeledOnDiagram = True, widthValue = 10, widthLabeledOnDiagram = True):
	with doc.create(TikZ(options=options)): # length, length makes the graph square
		pyramidCoords = determinePyramidVertices(length = lengthValue, width = widthValue, height = heightValue, typeOfPyramid = 'triangle')
		
		#Draw bottom shape, draw in height with right angle, draw 4 connecting lines
		
		#BOTTOM SHAPE
		com('draw %s -- %s -- %s -- cycle' % (str(pyramidCoords[1]), str(pyramidCoords[2]), str(pyramidCoords[3])), doc = doc)

		#draw 3 lines to height
		com('draw %s -- %s' % (str(pyramidCoords[1]), str(pyramidCoords[5])), doc = doc)
		com('draw %s -- %s' % (str(pyramidCoords[2]), str(pyramidCoords[5])), doc = doc)
		com('draw %s -- %s' % (str(pyramidCoords[3]), str(pyramidCoords[5])), doc = doc)

		#draw right angle with the length and width of triangle aka little height
		com('coordinate (D) at %s {}' % (str(pyramidCoords[1])), doc = doc)
		com('coordinate (E) at %s {}' % (str(pyramidCoords[2])), doc = doc)
		com('coordinate (F) at %s {}' % (str(pyramidCoords[3])), doc = doc)
		com('tkzMarkRightAngle[size = .1](D,E,F)', doc = doc)

		#draw height/altitude right angle
		com('draw[dash pattern=on 3pt off 5pt] %s -- %s' % (str(pyramidCoords[5]), str(pyramidCoords[6])), doc = doc)

		#right angle
		com('coordinate (A) at %s {}' % (str(pyramidCoords[5])), doc = doc)
		com('coordinate (B) at %s {}' % (str(pyramidCoords[6])), doc = doc)
		com('coordinate (C) at %s {}' % (str(pyramidCoords[7])), doc = doc)
		com('tkzMarkRightAngle[size = .1](A,B,C)', doc = doc)

		if heightLabeledOnDiagram == True:
			com('draw[dash pattern=on 3pt off 5pt] %s -- node[right]{%s}%s' % (str(pyramidCoords[5]), str(heightValue), str(pyramidCoords[6])), doc = doc)

		if widthLabeledOnDiagram == True:
			com('draw %s -- node[below,sloped]{%s}%s' % (str(pyramidCoords[2]), str(widthValue), str(pyramidCoords[3])), doc = doc)
		
		if lengthLabeledOnDiagram == True:
			com('draw %s -- node[above,sloped]{%s}%s' % (str(pyramidCoords[1]), str(lengthValue), str(pyramidCoords[2])), doc = doc)

def triangularPrism(options = 'rotate=0, scale=1', doc = None, wholeFigureRotation = 0, widthValue = 3, widthLabeledOnDiagram = True, heightValue = 30, heightLabeledOnDiagram = True, lengthValue = 30, lengthLabeledOnDiagram = True, baseRotation = 0):
	with doc.create(TikZ(options=options)): # length, length makes the graph square
		prismCoords = determinePrismVertices(length = lengthValue, width = widthValue, height = heightValue, typeOfPrism = 'triangle')
		
		#Draw bottom shape, draw top shape, connect all 3
		
		#BOTTOM SHAPE
		com('draw %s -- %s -- %s -- cycle' % (str(prismCoords[1]), str(prismCoords[2]), str(prismCoords[3])), doc = doc)

		#TOP SHAPE
		com('draw %s -- %s -- %s -- cycle' % (str(prismCoords[5]), str(prismCoords[6]), str(prismCoords[7])), doc = doc)

		#draw 3 lines connecting vertices on top and bottom
		com('draw %s -- %s' % (str(prismCoords[1]), str(prismCoords[5])), doc = doc)
		com('draw %s -- %s' % (str(prismCoords[2]), str(prismCoords[6])), doc = doc)
		com('draw %s -- %s' % (str(prismCoords[3]), str(prismCoords[7])), doc = doc)

		#draw right angle with the length and width of triangle aka little height
		com('coordinate (D) at %s {}' % (str(prismCoords[1])), doc = doc)
		com('coordinate (E) at %s {}' % (str(prismCoords[2])), doc = doc)
		com('coordinate (F) at %s {}' % (str(prismCoords[3])), doc = doc)
		com('tkzMarkRightAngle[size = .1](D,E,F)', doc = doc)

		#Label right angle between height and lenght/width
		com('coordinate (A) at %s {}' % (str(prismCoords[5])), doc = doc)
		com('coordinate (B) at %s {}' % (str(prismCoords[1])), doc = doc)
		com('coordinate (C) at %s {}' % (str(prismCoords[2])), doc = doc)
		com('tkzMarkRightAngle[size = .1](A,B,C)', doc = doc)

		if heightLabeledOnDiagram == True:
			com('draw[dash pattern=on 3pt off 5pt] %s -- node[right]{%s}%s' % (str(prismCoords[5]), str(heightValue), str(prismCoords[1])), doc = doc)

		if widthLabeledOnDiagram == True:
			com('draw %s -- node[below,sloped]{%s}%s' % (str(prismCoords[2]), str(widthValue), str(prismCoords[3])), doc = doc)
		
		if lengthLabeledOnDiagram == True:
			com('draw %s -- node[above,sloped]{%s}%s' % (str(prismCoords[1]), str(lengthValue), str(prismCoords[2])), doc = doc)

def hemisphere(options = 'rotate=0, scale=1', doc = None, wholeFigureRotation = 0, radiusDrawn = True, diameterDrawn = False, radiusLabeledOnDiagram = True, diameterLabeledOnDiagram = False, radiusValue = 2, diameterValue = 4):
	'''
	wholeFigureRotation = 0, 90, 180, 270 counterclockwise orientation of whole figure
	ADD THIS OPTION TO TIKZ rotate=wholeFigureRotation
	radius/diameter/height Labeled - a value is placed next to them
	radius/diameter/height value - their value is placed next to them if not default, will also use to determine placements
	radius/diameter/height drawn - they are drawn on the figure
	'''
	with doc.create(TikZ(options=options)): # length, length makes the graph square
		#define 4 points - use radius, height etc - maybe have minimum etc
		spherePoints = determineSphereVertices(radius = radiusValue, size = 'small')

		#scale height 4cm
		scaledRadius = spherePoints['center'][0] - spherePoints['left'][0]

		#create forward dark arc - middle
		arc(dashed = False, startDegrees = 180, endDegrees = 360, xRadius = scaledRadius, yRadius = .2*scaledRadius, startPoint = '(0,0)', doc = doc)

		#create backward dashed arc - middle
		arc(dashed = True, startDegrees = 180, endDegrees = 0, xRadius = scaledRadius, yRadius = .2*scaledRadius, startPoint = '(0,0)', doc = doc)

		#semi circle
		arc(startDegrees = 180, endDegrees = 0, xRadius = scaledRadius, yRadius = scaledRadius, startPoint = '(0,0)', doc = doc)

		#center
		point(x1 = spherePoints['center'][0], y1 = 0)

		if radiusDrawn == True:
			#create radius dashed, could do left radius at some point
			radiusDirection = random.choice(['left','right'])
			lineSegment(x1 = spherePoints['center'][0], y1 = spherePoints['center'][1], x2 = spherePoints[radiusDirection][0], y2 = spherePoints[radiusDirection][1], dashed = True, doc = doc)

		if radiusLabeledOnDiagram == True:
			#label radius midway - coordinate of point that is midway but higher
			if radiusDirection == 'left':
				node(x1 = spherePoints['left'][0] + scaledRadius*.5, y1 = 0, label = str(radiusValue), position = 'below', doc = doc)
			else:
				node(x1 = spherePoints['right'][0] - scaledRadius*.5, y1 = 0, label = str(radiusValue), position = 'below', doc = doc)

		if diameterLabeledOnDiagram == True:
			#label diameter with another arc or thingy - coordinate of point that is midway(so center) and lower cause height is in way
			labelWholeSide(x2 = spherePoints['left'][0], x1 = spherePoints['right'][0], y2 = spherePoints['left'][1] - .2*scaledRadius-.2, y1 = spherePoints['right'][1] - .2*scaledRadius-.2, nodePosition = 'below', nodeLabel = str(diameterValue), doc = doc)

		if diameterDrawn == True:
			#create diameter dashed
			lineSegment(x1 = spherePoints['left'][0], y1 = spherePoints['left'][1], x2 = spherePoints['right'][0], y2 = spherePoints['right'][1], dashed = True, doc = doc)

def halfcylinder(options = 'rotate=0, scale=1', doc = None, wholeFigureRotation = 0, radiusDrawn = True, diameterDrawn = False, radiusLabeledOnDiagram = True, heightLabeledOnDiagram = True, diameterLabeledOnDiagram = False, radiusValue = 2, diameterValue = 4, heightValue = 4):
	'''
	wholeFigureRotation = 0, 90, 180, 270 counterclockwise orientation of whole figure
	ADD THIS OPTION TO TIKZ rotate=wholeFigureRotation
	drawn...thing is drawn
	value is used to make the picture to scale
	'''
	with doc.create(TikZ(options=options)): # length, length makes the graph square
		#define 4 points - use radius, height etc - maybe have minimum etc
		cylinderPoints = determineCylinderVertices(radius = radiusValue, height = heightValue, size = 'small')

		#scale height 4cm
		scaledRadius = cylinderPoints['center'][0] - cylinderPoints['left'][0]
		scaledHeight = cylinderPoints['height'][1] - cylinderPoints['center'][1]

		#create forward dark arc - BOTTOM, counterclockwise
		arc(dashed = False, startDegrees = 180, endDegrees = 360, xRadius = scaledRadius, yRadius = .2*scaledRadius, startPoint = '(0,0)', doc = doc)

		#create forward dark arc on TOP
		arc(dashed = False, startDegrees = 180, endDegrees = 360, xRadius = scaledRadius, yRadius = .2*scaledRadius, startPoint = '(0,%g)' % scaledHeight, doc = doc)

		#DRAW TOP LINE - DIAMETER
		lineSegment(x1 = cylinderPoints['left'][0], y1 = cylinderPoints['left'][1]+scaledHeight, x2 = cylinderPoints['right'][0], y2 = cylinderPoints['right'][1]+scaledHeight, doc = doc)

		#create heights left and right
		lineSegment(x1 = cylinderPoints['left'][0], y1 = cylinderPoints['left'][1], x2 = cylinderPoints['topLeft'][0], y2 = cylinderPoints['topLeft'][1], doc = doc)
		lineSegment(x1 = cylinderPoints['right'][0], y1 = cylinderPoints['right'][1], x2 = cylinderPoints['topRight'][0], y2 = cylinderPoints['topRight'][1], doc = doc)

		if radiusDrawn == True:
			#create radius dashed, could do left radius at some point
			radiusDirection = random.choice(['left','right'])
			lineSegment(x1 = cylinderPoints['center'][0], y1 = cylinderPoints['center'][1], x2 = cylinderPoints[radiusDirection][0], y2 = cylinderPoints[radiusDirection][1], dashed = True, doc = doc)
			point(x1 = cylinderPoints['center'][0], y1 = cylinderPoints['center'][1], doc = doc)

		if radiusLabeledOnDiagram == True:
			#label radius midway - coordinate of point that is midway but higher
			if radiusDirection == 'left':
				node(x1 = cylinderPoints['left'][0] + scaledRadius*.5, y1 = 0, label = str(radiusValue), position = 'below', doc = doc)
			else:
				node(x1 = cylinderPoints['right'][0] - scaledRadius*.5, y1 = 0, label = str(radiusValue), position = 'below', doc = doc)

		#height labeled
		if heightLabeledOnDiagram == True:
			heightSide = random.choice(['left','right'])
			node(x1 = cylinderPoints[heightSide][0], y1 = cylinderPoints[heightSide][1] + scaledHeight/2, label = str(heightValue), position = heightSide, doc = doc)

		if diameterLabeledOnDiagram == True:
			#label diameter with another arc or thingy - coordinate of point that is midway(so center) and lower cause height is in way
			labelWholeSide(x2 = cylinderPoints['left'][0], x1 = cylinderPoints['right'][0], y2 = cylinderPoints['left'][1] - .2*scaledRadius-.2, y1 = cylinderPoints['right'][1] - .2*scaledRadius-.2, nodePosition = 'below', nodeLabel = str(diameterValue), doc = doc)

		if diameterDrawn == True:
			#create diameter dashed
			lineSegment(x1 = cylinderPoints['left'][0], y1 = cylinderPoints['left'][1], x2 = cylinderPoints['right'][0], y2 = cylinderPoints['right'][1], dashed = True, doc = doc)

def draw3DShape(shape, **kwargs):
	shape = shape.lower()
	if shape == 'halfcylinder':
		halfcylinder(**kwargs)
	elif shape == 'hemisphere':
		hemisphere(**kwargs)
	elif shape == 'triangular prism':
		triangularPrism(**kwargs)
	elif shape == 'triangular pyramid':
		trianglePyramid(**kwargs)
	elif shape == 'rectangular pyramid':
		rectangularPyramid(**kwargs)
	elif shape == 'rectangular prism':
		rectangularPrism(**kwargs)
	elif shape == 'sphere':
		sphere(**kwargs)
	elif shape == 'cube':
		cube(**kwargs)
	elif shape == 'regular square pyramid':
		regularPyramid(**kwargs)
	elif shape == 'cylinder':
		cylinder(**kwargs)
	elif shape == 'cone':
		cone(**kwargs)
