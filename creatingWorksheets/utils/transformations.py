from .MakeRectangle import MakeRectangle
from .CommonFunctions import ReturnPointCoordsAsLists
from .MakeRightTriangle import MakeRightTriangle
from .pdfFunctions import makeShapeObjectFromPoints
import random
import math

'''
for sequences: ideal do one transformation, take in set of coordinates to do another transformation etc etc using the pre-existing functions

thinking****

translation reflection
translation no overlap CHECK
if xLength is 5, if there is (5,6,7,8) between the first and second, then there won't be a vertical line to flip over, maybe in these cases we just make the grid larger???

'''

def translation(xMinGraph = -10, xMaxGraph = 10, yMinGraph = -10, yMaxGraph = 10, xChangeAmount = ['+','-','0'], yChangeAmount = ['+','-','0'], overlap = False, x = [], y = []):
	
	xLength = max(x) - min(x)
	yLength = max(y) - min(y)

	#####add something in incase the size of the shape is tooo small // / / / ask bryan

	#User will select which checkboxes and will randomize which ones selected
	#If random for both, we don't want 0,0 because that would be pointless, only do it if the user picks it
	if xChangeAmount == ['+', '-', '0'] and yChangeAmount == ['+', '-', '0']:
		chosen = random.randint(1,2)
		if chosen == 1:
			xChangeAmount.remove('0')
		else:
			yChangeAmount.remove('0')
	
	xChangeAmount = random.choice(xChangeAmount)
	yChangeAmount = random.choice(yChangeAmount)
	print('made it here')
	if xChangeAmount == '+':  # going to move triangle somewhere on grid so that it can afterwards go some amount to the right
		xChange = random.randint(xMinGraph - min(x), (xMaxGraph - (xLength + 1)) - max(
			x))  # can add 0 up til maxx - xLength then - 1 so that future translation doesn't overlap
	elif xChangeAmount == '-':
		xChange = random.randint(xMinGraph - (min(x) - (xLength + 1)), xMaxGraph - max(x))
	elif xChangeAmount == '0':
		xChange = 0
	print('3')
	if yChangeAmount == '+':  # going to move triangle somewhere on grid so that it can afterwards go some amount to the right
		yChange = random.randint(yMinGraph - min(y), (yMaxGraph - (yLength + 1)) - max(
			y))  # can add 0 up til maxx - xLength then - 1 so that future translation doesn't overlap
	elif yChangeAmount == '-':
		yChange = random.randint(yMinGraph - (min(y) - (yLength + 1)), yMaxGraph - max(y))
	elif yChangeAmount == '0':
		yChange = 0
	xs = []
	ys = []
	print('4')
	for itemX, itemY in zip(x, y):
		xs.append(itemX + xChange)
		ys.append(itemY + yChange)

	x = xs
	y = ys
	print('5')
	if overlap == False:
		print('overlap is false')
		if xMinGraph + xLength < min(x):
			leftChange = xMinGraph - min(x)  # plus one so that the translation does not overlap at all
			leftChoices = list(range(leftChange, -xLength - 1 + 1))  # the most we could add negatively is xLength+1
		else:
			leftChoices = []

		if xMaxGraph - xLength > max(x):
			rightChange = xMaxGraph - max(x)
			rightChoices = list(range(xLength + 1, rightChange + 1))  # smallest we can do is xLength +1
		else:
			rightChoices = []

		xChoices = leftChoices + rightChoices
		print('6')
		if yMinGraph + yLength < min(y):
			downChange = yMinGraph - min(y)  # plus one so that the translation does not overlap at all
			downChoices = list(range(downChange, -yLength - 1 + 1))
		else:
			downChoices = []
		if yMaxGraph - yLength > max(y):
			upChange = yMaxGraph - max(y)
			upChoices = list(range(yLength + 1, upChange + 1))
		else:
			upChoices = []

		yChoices = downChoices + upChoices
		print('7')
		#if yChangeAmount == 'random':
			#yTrans = random.choice(yChoices)
		if yChangeAmount == "+":
			yTrans = random.choice(upChoices)
		elif yChangeAmount == '-':
			yTrans = random.choice(downChoices)
		elif yChangeAmount == '0':
			yTrans = 0
		else:
			yTrans = random.choice(yChoices)

		#if xChangeAmount == 'random':
			#xTrans = random.choice(xChoices)
		if xChangeAmount == "+":
			xTrans = random.choice(rightChoices)
		elif xChangeAmount == '-':
			xTrans = random.choice(leftChoices)
		elif xChangeAmount == '0':
			xTrans = 0
		else:
			xTrans = random.choice(xChoices)

	elif overlap == True:  #
		print('overlap is true')
		if min(x) - xLength >= xMinGraph:
			leftChoices = list(range(-xLength, 1))  # the most we could add negatively is xLength+1
		else:
			leftChange = xMinGraph - min(x)
			leftChoices = list(range(leftChange, 1))

		if max(x) + xLength <= xMaxGraph:
			rightChoices = list(range(0, xLength + 1))  # smallest we can do is xLength +1
		else:
			rightChange = xMaxGraph - max(x)
			rightChoices = list(range(0, rightChange))

		xChoices = leftChoices + rightChoices

		if min(y) - yLength >= yMinGraph:
			downChoices = list(range(-yLength, 1))  # the most we could add negatively is xLength+1
		else:
			downChange = yMinGraph - min(y)
			downChoices = list(range(downChange, 1))

		if max(y) + yLength <= yMaxGraph:
			upChoices = list(range(0, yLength + 1))  # smallest we can do is xLength +1
		else:
			upChange = yMaxGraph - max(y)
			upChoices = list(range(0, upChange))

		yChoices = downChoices + upChoices
	print(xChoices, yChoices)
	#if yChangeAmount == 'random':
	#yTrans = random.choice(yChoices)
	if yChangeAmount == "+":
		yTransVal = random.choice(upChoices)
	elif yChangeAmount == '-':
		yTransVal = random.choice(downChoices)
	elif yChangeAmount == '0':
		yTransVal = 0
	else:
		yTransVal = random.choice(yChoices)

	#if xChangeAmount == 'random':
		#xTrans = random.choice(xChoices)
	if xChangeAmount == "+":
		xTransVal = random.choice(rightChoices)
	elif xChangeAmount == '-':
		xTransVal = random.choice(leftChoices)
	elif xChangeAmount == '0':
		xTransVal = 0
	else:
		xTransVal = random.choice(xChoices)

	if yTransVal == 0 and xTransVal == 0:  # so a translation will actually happen
		if len(yChoices) > 1:
			yChoices.remove(0)
			yTransVal = random.choice(yChoices)
		elif len(xChoices) > 1:
			xChoices.remove(0)
			xTransVal = random.choice(xChoices)
		print('Identity Translation fixed')

	transXs = []
	transYs = []
	for itemX in x:
		transXs.append(itemX + xTransVal)
	for itemY in y:
		transYs.append(itemY + yTransVal)
	return x, y, transXs, transYs, xTransVal, yTransVal
def reflection(x = [], y = [], xMinGraph = -10, xMaxGraph = 10, yMinGraph = -10, yMaxGraph = 10, nameOfReflectionList = ['x=not0','y=not0','yaxis','xaxis','x=','y=','x=0','y=0'], overlap = False):  # assuming triangle to start
	import random
	# nameOfReflection: x=, y=, x= not 0, y= not 0, x=0, y=0, xaxis, yaxis
	# overlap = 'no' or 'yes'

	if nameOfReflectionList == 'random':
		nameOfReflection = random.choice(['xaxis','yaxis','x=', 'y=', 'x=not0', 'y=not0', 'x=0', 'y=0'])
	else:
		nameOfReflection = random.choice(nameOfReflectionList)

	if overlap == 'random':
		overlap = random.choice([True,False])
	
	# just like translation, need to move current triangle to somewhere so it can do then be reflected
	xLength = max(x) - min(x)
	yLength = max(y) - min(y)
	#in case not square, smaller max - larger min
	gridSize = min([xMaxGraph, yMaxGraph]) - max([xMinGraph, yMinGraph])

	if nameOfReflection == 'x=' or nameOfReflection == 'x=not0':
		# need (xLength+1)*2 room to do the reflection, so farthest i can always move it left (to -10) is minn - min(x) to  minn + (gridSize - (xLength+1)*2)
		xChange = random.randint(xMinGraph - min(x), xMinGraph + (gridSize - (xLength + 1) * 2) - min(x))
		yChange = random.randint(yMinGraph - min(y), yMaxGraph - max(y))  # y can go anywhere

		xs = []
		ys = []

		for itemX, itemY in zip(x, y):
			xs.append(itemX + xChange)
			ys.append(itemY + yChange)

		x = xs
		y = ys

		if overlap == False:
			if (max(x) + 1 + 1 + xLength) <= xMaxGraph:  # there are lines on the right that work
				# the farthest right line would be maxx - min(x) // 2
				rightChoices = list(range(min(x) + xLength + 1, (xMaxGraph - min(x)) // 2 + min(
					x) + 1))  # first part is the closest line that has to work, then second part is
			else:
				rightChoices = []
			if (min(x) - 1 - 1 - xLength) >= xMinGraph:  # there are line on the left that work
				leftChoices = list(range(max(x) - (max(x) - xMinGraph) // 2, max(x) - xLength - 1 + 1))
			else:
				leftChoices = []
			refValChoices = rightChoices + leftChoices
		elif overlap == True:
			choices = list(range(min(x), max(x) + 1))
			refValChoices = []
			for item in choices:
				if item - xLength >= xMinGraph and item + xLength <= xMaxGraph:
					refValChoices.append(item)

		refVal = random.choice(refValChoices)
		if nameOfReflection == 'x=not0':
			if 0 in refValChoices:
				refValChoices.remove(0)
				refVal = random.choice(refValChoices)

		refX = []
		refY = []
		for itemX, itemY in zip(x, y):
			refX.append(2 * refVal - itemX)
			refY.append(itemY)

	elif nameOfReflection == 'y=' or nameOfReflection == 'y=not0':
		# need (xLength+1)*2 room to do the reflection, so farthest i can always move it left (to -10) is minn - min(x) to  (minn + gridSize - (xLength+1)*2) - min(x)
		yChange = random.randint(yMinGraph - min(y), yMinGraph + (gridSize - (yLength + 1) * 2) - min(y))
		xChange = random.randint(xMinGraph - min(x), xMaxGraph - max(x))  # y can go anywhere

		xs = []
		ys = []

		for itemX, itemY in zip(x, y):
			xs.append(itemX + xChange)
			ys.append(itemY + yChange)

		x = xs
		y = ys

		if overlap == False:
			if (max(y) + 1 + 1 + yLength) <= yMaxGraph:  # there are lines on the up that work
				# the farthest up line would be maxx - min(y) // 2
				upChoices = list(range(min(y) + yLength + 1, (yMaxGraph - min(y)) // 2 + min(
					y) + 1))  # first part is the closest line that has to work, then second part is
			else:
				upChoices = []
			if (min(y) - 1 - 1 - yLength) >= yMinGraph:  # there are line on the left that work
				downChoices = list(range(max(y) - (max(y) - yMinGraph) // 2, max(y) - yLength - 1 + 1))
			else:
				downChoices = []
			refValChoices = upChoices + downChoices
		elif overlap == True:
			choices = list(range(min(y), max(y) + 1))
			refValChoices = []
			for item in choices:
				if item - yLength >= yMinGraph and item + yLength <= yMaxGraph:
					refValChoices.append(item)

		refVal = random.choice(refValChoices)
		if nameOfReflection == 'y=not0':
			if 0 in refValChoices:
				refValChoices.remove(0)
				refVal = random.choice(refValChoices)

		refX = []
		refY = []
		for itemX, itemY in zip(x, y):
			refY.append(2 * refVal - itemY)
			refX.append(itemX)

	elif nameOfReflection == 'yaxis' or nameOfReflection == 'x=0':
		if overlap == False:
			# can't touch yaxis, so the point it can go to leftward is -1 - xLength to 1 + xlength
			# it can go all the way to the minn value, so minn - min(x) but it has to be less than 0 for the max(x), so min(x) + xLength + 1
			# leftXChange = list(range((0 - xLength - 1) - min(x), (0 + xLength + 1) - min(x) + 1))
			leftXChange = list(range(xMinGraph - min(x), (0 - xLength - 1) - min(x) + 1))
			rightXChange = list(range(0 + xLength + 1, xMaxGraph - max(x) + 1))
			xChange = random.choice(leftXChange + rightXChange)
			yChange = random.randint(yMinGraph - min(y), yMaxGraph - max(y))
		else:
			xChange = random.choice(list(range((0 - xLength) - min(x), (0 + xLength) - max(x) + 1)))
			yChange = random.randint(yMinGraph - min(y), yMaxGraph - max(y))

		xs = []
		ys = []

		for itemX, itemY in zip(x, y):
			xs.append(itemX + xChange)
			ys.append(itemY + yChange)

		x = xs
		y = ys

		refVal = 0

		refX = []
		refY = []
		for itemX, itemY in zip(x, y):
			refX.append(2 * refVal - itemX)
			refY.append(itemY)

	elif nameOfReflection == 'xaxis' or nameOfReflection == 'y=0':
		if overlap == False:
			# can't touch Xaxis, so the point it can go to downward is \
			# it can go all the way to the minn value, so minn - min(x) but it has to be less than 0 for the max(x), so min(x) + xLength + 1
			downYChange = list(range(yMinGraph - min(y), (0 - yLength - 1) - min(y) + 1))
			upYChange = list(range(0 + yLength + 1, yMaxGraph - max(y) + 1))
			yChange = random.choice(downYChange + upYChange)
			xChange = random.randint(xMinGraph - min(x), xMaxGraph - max(x))
		else:
			yChange = random.choice(list(range((0 - yLength) - min(y), (0 + yLength) - max(y) + 1)))
			xChange = random.randint(xMinGraph - min(x), xMaxGraph - max(x))

		xs = []
		ys = []

		for itemX, itemY in zip(x, y):
			xs.append(itemX + xChange)
			ys.append(itemY + yChange)

		x = xs
		y = ys

		refVal = 0

		refX = []
		refY = []
		print(x, y)
		for itemX, itemY in zip(x, y):
			refY.append(2 * refVal - itemY)
			refX.append(itemX)

	if nameOfReflection == 'xaxis' or nameOfReflection == 'yaxis':
		refValString = '$' + nameOfReflection[0] + '-' + nameOfReflection[1:] + '$'
	elif nameOfReflection == 'y=' or nameOfReflection == 'x=':
		refValString = 'line $' + nameOfReflection[0] + ' = {%d}' % refVal + '$'
	elif nameOfReflection == 'y=0' or nameOfReflection == 'x=0':
		refValString = 'line $' + nameOfReflection[0] + ' = 0 $'
	elif nameOfReflection == 'x=not0' or nameOfReflection == 'y=not0':
		refValString = 'line $' + nameOfReflection[0] + ' = {%d}' % refVal + '$'

	print('refX is',refX)
	return x, y, refX, refY, refVal, refValString  # need to add part for x= or y= or whatever
def rotation(x = [], y = [], xMinGraph = -10, xMaxGraph = 10, yMinGraph = -10, yMaxGraph = 10, center = ['origin'] , degrees = [90, 180, 270], direction = ['counterclockwise','clockwise'], overlap = False):
	# change for random center, random degrees, random direction, etc
	print(degrees, direction, center)
	degrees = random.choice(degrees)
	direction = random.choice(direction)
	center = random.choice(center)

	'''
	imagine a square with min(x) and min(y) being at (0,0)
	center of rotation (if no overlap) can only be 
	xLength, yLength
	max(x) - lowerpoint <= -10
	centerX = random.choice([x for x in range(max(x)-xMaxGraph, min(x)+xMaxGraph)] if x not in [range(0,xLength+1)])
	#and this is different if overlap == True
	centerY = random.choice([x for x in range(max(x)-xMaxGraph, min(x)+xMaxGraph)] if x not in [range(0,xLength+1)])
	
	now the point will allow the whole picture to be only -10 to 10 long etc

	translate to 0,0
	rotate
	translate back

	then

	translate the many different locations possible, which would be

	'''
	print(x,y)
	# lets do vertically then horizontally, then we can do other shit
	xLength = max(x) - min(x)
	yLength = max(y) - min(y)


	#find a center that will work with overlap, this will move the triangle if it's touching the middle etc, later we will return new coordinates if center is not origin, else we'll keep these coordinates for origin
	if overlap == False:
		centerX = random.choice([item for item in range(max(x)-xMaxGraph, min(x)+xMaxGraph+1) if x not in range(min(x),min(x)+xLength+1)])
		centerY = random.choice([item for item in range(max(y)-yMaxGraph, min(y)+yMaxGraph+1) if x not in range(min(y),min(y)+yLength+1)])
	else: #want center to be on min to max etc
		centerX = random.randint(min(x), max(x))
		centerY = random.randint(min(y), max(y))

	#now translate centers and x and y coordinates, then do the actual rotation
	#translateX = random.randint(minn, maxx - (centerX*2))
	#translateY = random.randint(minn, maxx - (centerY*2))
	translateX = centerX * -1
	translateY = centerY * -1

	#translate x and y so that they are not touching the origin

	if direction == 'counterclockwise':
		angleRot = math.radians(degrees)
	if direction == 'clockwise':
		angleRot = math.radians(360 - degrees)

	# this angle is always counterclockwise
	tX = [itemX - centerX for itemX in x]  # translate to origin
	tY = [itemY - centerY for itemY in y]

	rotX = [itemX * int(math.cos(angleRot)) - itemY * int(math.sin(angleRot)) for itemX, itemY in zip(tX, tY)]  # rotate, add ints so that coordinates wouldn't be floats
	rotY = [itemX * int(math.sin(angleRot)) + itemY * int(math.cos(angleRot)) for itemX, itemY in zip(tX, tY)]

	# translate Back if center is not origin
	if center != 'origin':
		#between tX and rotX, determine how much the whole shit can move
		xChange = random.randint(xMinGraph-min([0]+tX+rotX), xMaxGraph-max([0]+tX+rotX))
		yChange = random.randint(yMinGraph-min([0]+tY+rotY), yMaxGraph-max([0]+tY+rotY))
		newX = [itemX + xChange for itemX in tX]
		newY = [itemY + yChange for itemY in tY]

		newRotX = [itemX + xChange for itemX in rotX]
		newRotY = [itemY + yChange for itemY in rotY]
		centerX = xChange
		centerY = yChange
	else: #origin
		newX = tX
		newY = tY
		newRotX = rotX
		newRotY = rotY
		centerX = 0
		centerY = 0

	center = [centerX, centerY]
	
	print(x,y,rotX,rotY)
	
	print('center is ', center)
	return newX, newY, newRotX, newRotY, center, degrees, direction

def dilation(minn, maxx, x, y, center, sf, overlap):
	# for scalefactor the most i really need is 2,3 or 1/2 1/3, maybe 3/2, 5/2, 2/3, 4/3
	# in any case if the original triangle is small enough to always get 3 times bigger somewhere on the grid, we should be able to do all of the above
	# center options: no overlap == inside, outside
	# overlap = on, vertex

	xLength = max(x) - min(x)
	yLength = max(y) - min(y)
	gridSize = maxx - minn

	maxInt = math.floor(gridSize / (max([xLength, yLength])))

	# regardless if sf is interger or fraction, it will start as integer and then we'll just switch afterwards
	sfVal = random.randint(2, maxInt)
	# http: // blackpawn.com / texts / pointinpoly / default.html FOR EXAMPLANATION
	import numpy

	centerPoints = []

	for xP in range(min(x), max(x) + 1):
		for yP in range(min(y), max(y) + 1):
			p = [xP, yP]
			a = [x[0], y[0]]
			b = [x[1], y[1]]
			c = [x[2], y[2]]
			if pointTriangle(center, p, a, b, c) == True:
				centerPoints.append(p)

	if center == 'vertex':
		centerPoints = [[x[0], y[0]], [x[1], y[1]], [x[2], y[2]]]

	centerChosen = random.choice(centerPoints)

	centerX = centerChosen[0]
	centerY = centerChosen[1]

	# if i dilate the triangle in the spot it currently is, then i can move it so that the confines are on the graph, thus determining a new center
	tempDX = [sfVal * (item + -1 * centerX) + centerX for item in x]
	tempDY = [sfVal * (item + -1 * centerY) + centerY for item in y]

	# check to make sure it can be moved onto the grid
	if max(tempDY) - min(tempDY) > gridSize:
		print('oh no y')
	if max(tempDX) - min(tempDX) > gridSize:
		print('oh no x')

	# so now i have the triangle dilated, so i need to make it so max(x) < maxx and min(x) > minn, which i hope is possible
	xChange = random.randint(minn - min(tempDX), maxx - max(tempDX))
	yChange = random.randint(minn - min(tempDY), maxx - max(tempDY))

	# translate the center as well
	centerX = centerX + xChange
	centerY = centerY + yChange

	centerCoord = [centerX, centerY]

	xs = []
	ys = []

	for itemX, itemY in zip(x, y):
		xs.append(itemX + xChange)
		ys.append(itemY + yChange)

	x = xs
	y = ys

	dX = []
	dY = []

	for ddx, ddy in zip(tempDX, tempDY):
		dX.append(ddx + xChange)
		dY.append(ddy + yChange)

	# for now sf is 2,3, 1/2, 3/2 or 1/3 or 2/3 because orignal image is 2 times or 3 times and fration are still smaller than original
	# could eventually do sf of 2, 4, 6, so that I could then reverse it and do 5/2 (2.5), 4/3 etc

	if sf == 'integer':
		sfVal = sfVal
		return centerCoord, sfVal, x, y, dX, dY
	elif sf == 'fraction':
		if sfVal == 2:
			oo = random.randint(1, 2)
			if oo == 1:
				sfVal = 1 / sfVal
			elif oo == 2:
				sfVal = 3 / sfVal
		elif sfVal == 3:
			oo = random.randint(1, 2)
			if oo == 1:
				sfVal = 1 / sfVal
			elif oo == 2:
				sfVal = 2 / sfVal
		return centerCoord, sfVal, x, y, dX, dY

def rotateCoordinatesAsList(xAsList, yAsList, direction, degrees, centerX = 0, centerY = 0):
	if direction == 'counterclockwise':
		angleRot = math.radians(degrees)
	if direction == 'clockwise':
		angleRot = math.radians(360 - degrees)
	print(max(xAsList)-min(xAsList))
	print(max(yAsList)-min(yAsList))
	# this angle is always counterclockwise
	tX = [itemX - centerX for itemX in xAsList]  # translate to origin
	tY = [itemY - centerY for itemY in yAsList]
	print(max(tX)-min(tX))
	print(max(tY)-min(tY))
	rotX = [itemX * int(math.cos(angleRot)) - itemY * int(math.sin(angleRot)) for itemX, itemY in zip(tX, tY)]  # rotate, add ints so that coordinates wouldn't be floats
	rotY = [itemX * int(math.sin(angleRot)) + itemY * int(math.cos(angleRot)) for itemX, itemY in zip(tX, tY)]
	print(max(rotX)-min(rotX))
	print(max(rotY)-min(rotY))
	# translate Back
	rottX = [int(itemX + centerX) for itemX in rotX]  # translate to origin
	rottY = [int(itemY + centerY) for itemY in rotY]
	print(max(rottX)-min(rottX))
	print(max(rottY)-min(rottY))
	print('-----------------')
	return rottX, rottY
def reflectCoordinates(x, y, xy, refVal):
	refX = []
	refY = []
	if xy == 'y':
		for itemX, itemY in zip(x, y):
			refX.append(itemX)
			refY.append(2 * refVal - itemY)
	elif xy == 'x':
		for itemX, itemY in zip(x, y):
			refX.append(2 * refVal - itemX)
			refY.append(itemY)
	return refX, refY
def translateCoordinates(x, y, changeX, changeY):
	newx = []
	newy = []
	for itemX, itemY in zip(x, y):
		newx.append(itemX + changeX)
		newy.append(itemY + changeY)
	return newx, newy

def sequence(xMinGraph = -10, xMaxGraph = 10, yMinGraph = -10, yMaxGraph = 10, transformation1 = ['translation','reflection','rotation','dilation'], transformation2 = ['translation','reflection','rotation','dilation'], x = [], y = [], secondShape = False):
	dick = 3
	#let's try doing translation reflection first
	trans1 = random.choice(transformation1)
	trans2 = random.choice(transformation2)
	x1 = x
	y1 = y 
	print(trans1, trans2)
	if trans1 == 'translation':
		xChange = random.choice([item for item in range(xMinGraph - min(x1), xMaxGraph - max(x1) + 1) if item not in range(0,max(x1)-min(x1)+1)])
		yChange = random.choice([item for item in range(yMinGraph - min(y1), yMaxGraph - max(y1) + 1) if item not in range(0,max(y1)-min(y1)+1)])
		x2, y2 = translateCoordinates(x = x1, y = y1, changeX = xChange, changeY = yChange)
	elif trans1 == 'reflection':
		direction = random.choice(['x','y']) #to choose horizontal or vertical
		xLength = max(x1)-min(x1)
		yLength = max(y1)-min(y1)
		if direction == 'x':
			refVal = random.choice([item for item in range(max(x1)-abs(xMinGraph-max(x1))//2, min(x1)+(xMaxGraph-min(x1))//2+1) if item not in range(min(x1),max(x1)+1)])
		elif direction == 'y':
			refVal = random.choice([item for item in range(max(y1)-abs(yMinGraph-max(y1))//2, min(y1)+(yMaxGraph-min(y1))//2+1) if item not in range(min(y1),max(y1)+1)])
		x2, y2 = reflectCoordinates(x = x1, y = y1, xy = direction, refVal = refVal)
	
	elif trans1 == 'rotation':
		x2, y2 = rotateCoordinatesAsList(xAsList = x1, yAsList = y1, direction = random.choice(['clockwise','counterclockwise']), degrees = random.choice([90,180,270]), centerX = 0, centerY = 0)
	
	if trans2 == 'translation':
		print(x2,y2)
		xChange = random.choice([item for item in range(xMinGraph - min(x2), xMaxGraph - max(x2) + 1) if item not in range(0,max(x2)-min(x2)+1)])
		yChange = random.choice([item for item in range(yMinGraph - min(y2), yMaxGraph - max(y2) + 1) if item not in range(0,max(y2)-min(y2)+1)])

		x3, y3 = translateCoordinates(x = x2, y = y2, changeX = xChange, changeY = yChange)
	elif trans2 == 'reflection':
		direction = random.choice(['x','y']) #to choose horizontal or vertical
		xLength = max(x2)-min(x2)
		yLength = max(y2)-min(y2)
		if direction == 'x':
			refVal = random.choice([item for item in range(max(x2)-abs(xMinGraph-max(x2))//2, min(x2)+(xMaxGraph-min(x2))//2+1) if item not in range(min(x2),max(x2)+1)])
		elif direction == 'y':
			refVal = random.choice([item for item in range(max(y2)-abs(yMinGraph-max(y2))//2, min(y2)+(yMaxGraph-min(y2))//2+1) if item not in range(min(y2),max(y2)+1)])

		x3, y3 = reflectCoordinates(x = x2, y = y2, xy = direction, refVal = refVal)
	elif trans2 == 'rotation':
		x3, y3 = rotateCoordinatesAsList(xAsList = x2, yAsList = y2, direction = random.choice(['clockwise','counterclockwise']), degrees = random.choice([90,180,270]))

	return trans1, trans2, x1, y1, x2, y2, x3, y3

def reflectionReflection(options, minn, maxx, typeOfTriangle, size, ref1List, ref2List, overlap1, overlap2):
	# (vert) (vert) right right
	# (vert) (vert) right left
	# flip over y-axis for left left, left right
	#can rotate 90 cc or ccw for ho ho up up, ho ho up down, ho ho down up

	# (vert) (ho) right up
	# flip y axis for (vert) (ho) left up
	# flip x axis for (vert) (ho) right down
	# flip y and x axis for (vert) (ho) left down

	# (vert) can be x= or x=0/yaxis or x=not0
	# (ho) can be y= or y=0/xaixs or y=not0

	ref1Type = random.choice(ref1List)
	ref2Type = random.choice(ref2List)

	choices = ['xaxis','yaxis','x=','y=','y=0','x=0','y=not0','x=not0']

	vertLines = ['yaxis', 'x=', 'x=not0', 'x=0']
	hoLines = ['x-axis', 'y=', 'y=not0', 'y=0']

	if ref1List == 'random':
		ref1Type = random.choice(choices)
	if ref2List == 'random':
		ref2Type = random.choice(choices)

	# would like to specify ref type for xaxis or yaxis etc for off grid
	x, y = polygon(minn, maxx, typeOfTriangle, size)
	# lets do vertically then horizontally, then we can do other shit
	xLength = max(x) - min(x)
	yLength = max(y) - min(y)

	# moving polygon so that it alligns with where min(x) = 0 and min(y) = 0
	alignedX = []
	alignedY = []
	for itemX, itemY in zip(    x, y):
		alignedX.append(itemX - min(x))
		alignedY.append(itemY - min(y))

	if ( (ref1Type in vertLines) and (ref2Type in vertLines) ) or ( (ref1Type in hoLines) and (ref2Type in hoLines) ) == True: #two vert lines first
		#Note: we don't care about refList because it doesn't matter if one of these is the y-axis
		if overlap1 == 'no':  # same direction, polygon needs to be between 2 and 3 long
			refVal1 = random.randint(xLength + 1, math.floor(
				((maxx - minn) - (xLength + 2)) / 2))  # then polygon will have enough room to go right
		else:
			refVal1 = random.randint(math.ceil(xLength / 2), xLength)

		if overlap2 == 'no':
			refVal2 = random.randint(refVal1 * 2 + 1, math.floor(((maxx - minn) - (refVal1 * 2 - xLength)) / 2) + (
			refVal1 * 2 - xLength))
		else:
			refVal2 = random.randint(refVal1 * 2 - xLength + 1, refVal1 * 2)



	else: #this is where we'll care about x-axis and y-axis
		if overlap1 == 'no':  # eventually i need to left and right reflection
			refVal1 = random.randint(xLength + 1, (maxx - minn) / 2)
		else:
			refVal1 = random.randint(math.ceil(xLength / 2), xLength)

		if overlap2 == 'no':  # eventually i need to left and right reflection
			refVal2 = random.randint(yLength + 1, (maxx - minn) / 2)  # square grid
		else:
			refVal2 = random.randint(math.ceil(yLength / 2), yLength)











	# now transate everything to the 10 by 10 grid
	if case == 'normal':
		translateValueX = random.randint(minn, maxx - (refVal1 - min(x)) * 2)  # t1, so use x and y
		translateValueY = random.randint(minn, maxx - (refVal2 - min(y)) * 2)  # t2 so use self.refX, self.refY
	else:
		tye = min(x)
		refTye = refVal1 - min(x)
		refTye = refTye * 2
		refTye = refTye - xLength #minx on second triangle
		dist = refVal2 - refTye
		dist = dist * 2
		refTye = refTye + dist

		translateValueX = random.randint(minn, maxx - (refTye))
		translateValueY = random.randint(minn, maxx - max(y))# t1, so use x and y

	if case == 'normal':
		refVal1 = refVal1 + translateValueX
		refVal2 = refVal2 + translateValueY
	else:
		refVal1 = refVal1 + translateValueX
		refVal2 = refVal2 + translateValueX

	x1 = []
	y1 = []

	x2 = []
	y2 = []

	x3 = []
	y3 = []

	for itemX, itemY in zip(x, y):
		x1.append(itemX + translateValueX)
		y1.append(itemY + translateValueY)

	# determing reflected coordinates
	if case == 'normal':
		for itemX, itemY in zip(x1, y1): #x=
			x2.append(2 * refVal1 - itemX)
			y2.append(itemY)

		for itemX, itemY in zip(x2, y2): #y =
			x3.append(itemX)
			y3.append(2 * refVal2 - itemY)
	else:
		for itemX, itemY in zip(x1, y1):  # x=
			x2.append(2 * refVal1 - itemX)
			y2.append(itemY)

		for itemX, itemY in zip(x2, y2):  # x=
			x3.append(2 * refVal2 - itemX)
			y3.append(itemY)

	if options == 'random':
		randomized = random.choice(['stay', 'y=x=', 'switchx=', 'switchy='])
	else:
		randomized = random.choice(options) #x=y=, y=x=,

	if case == 'normal':
		refVal1Type = 'x'
		refVal2Type = 'y'
	else:
		refVal1Type = 'x'
		refVal2Type = 'x'

	#if randomized = x= y= then it stays the same

	if randomized == 'y=x=' and case == 'normal':  # switches order
		# will need to rotate everything aroudn the origin 90 cw or ccw, refvalues will change and have their own loop
		direction = random.choice(['ccw', 'cc'])
		x1, y1 = rotateCoordinates(x1, y1, 0, 0, direction, 90)
		x2, y2 = rotateCoordinates(x2, y2, 0, 0, direction, 90)
		x3, y3 = rotateCoordinates(x3, y3, 0, 0, direction, 90)

		#for x=refVal1, [refVal1, 0]
		first = [refVal1, 0]

		#for y=refVal2, [0, refVal2]
		second = [0, refVal2]

		xs = [refVal1, 0]
		ys = [0, refVal2]

		newX, newY = rotateCoordinates(xs, ys, 0, 0, direction, 90)

		newX.remove(0)
		refVal2 = newX[0]

		newY.remove(0)
		refVal1 = newY[0]

		refVal1Type = 'y'
		refVal2Type = 'x'
	else:
		chick = 1

	randomized = random.choice(['switchx=', 'switchy=','nothing','nothing']) #gives a fair opportunity to switch up graph
	if randomized == 'switchx=' and refVal1 == 'x':
		# will reflect over y-axis
		x1, y1 = reflectCoordinates(x1, y1, 'x', 0)
		x2, y2 = reflectCoordinates(x2, y2, 'x', 0)
		x3, y3 = reflectCoordinates(x3, y3, 'x', 0)
		refVal1 = refVal1 * -1
	elif randomized == 'switchy=' and refVal2 == 'y':
		# will reflect over x-axis
		x1, y1 = reflectCoordinates(x1, y1, 'y', 0)
		x2, y2 = reflectCoordinates(x2, y2, 'y', 0)
		x3, y3 = reflectCoordinates(x3, y3, 'y', 0)
		refVal2 = refVal2 * -1

	if refVal1Type == 'x':
		if refVal1 != 0:
			refVal1String = 'line $x = %s$' % constantOperation(refVal1, True)
		else:
			refVal1String = '$y-axis$'
	elif refVal1Type == 'y':
		if refVal1 != 0:
			refVal1String = 'line $y = %s$' % constantOperation(refVal1, True)
		else:
			refVal1String = '$x-axis$'

	if refVal2Type == 'x':
		if refVal2 != 0:
			refVal2String = 'line $x = %s$' % constantOperation(refVal2, True)
		else:
			refVal2String = '$y-axis$'
	elif refVal2Type == 'y':
		if refVal2 != 0:
			refVal2String = 'line $y = %s$' % constantOperation(refVal2, True)
		else:
			refVal2String = '$x-axis$' #will handle x-axis vs y= shit when we're writing the problem

	return refVal1String, refVal2String, x1, y1, x2, y2, x3, y3
def reflectionTranslation(minn, maxx, refList, refOverlap, transOverlap):
	#would like to specify ref type for xaxis or yaxis etc for off grid
	x, y = polygon(minn, maxx, 'right triangle', 'smaller')
	# lets do vertically then horizontally, then we can do other shit
	xLength = max(x) - min(x)
	yLength = max(y) - min(y)

	# moving polygon so that it alligns with where min(x) = 0 and min(y) = 0
	alignedX = []
	alignedY = []
	for itemX, itemY in zip(x, y):
		alignedX.append(itemX - min(x))
		alignedY.append(itemY - min(y))

	if refOverlap == 'no':  # eventually i need to left and right reflection
		refVal1 = random.randint(xLength + 1, (maxx - minn) / 2)
	else:
		refVal1 = random.randint(math.ceil(xLength / 2), xLength)


	x = alignedX
	y = alignedY

	#now we need to determine translate amounts

	farRightX = (refVal1 - min(x)) * 2
	leftX = farRightX - xLength

	botY = min(y)
	topY = max(y)

	#easy, just donn't move it in the plane you just flipped it in
	if transOverlap == 'no':
		transValX = random.randint(-1 * leftX, (maxx - minn) - farRightX)
		transValY = random.randint(yLength + 1, (maxx - minn) - max(y))
	else:
		transValX = random.randint(-1 * leftX, (maxx - minn) - farRightX)
		transValY = random.randint(0, (maxx - minn) - max(y))

	#build all the shit in the top right, then translate everything
	x1 = x
	y1 = y
	x2 = []
	y2 = []
	x3 = []
	y3 = []

	x2, y2 = reflectCoordinates(x1, y1, 'x', refVal1)

	x3, y3 = translateCoordinates(x2, y2, transValX, transValY)

	if 'xaxis' in refList or 'yaxis' in refList or 'x=0' in refList or 'y=0' in refList:
		wholeTransX = refVal1 * -1
	else:
		wholeTransX = random.randint(minn, maxx - max(x1 + x2 + x3))
		if 'x=not0' in refList or 'y=not0' in refList:
			while wholeTransX + refVal1 == 0:
				print('ohhhh no')
				wholeTransX = random.randint(minn, maxx - max(x1 + x2 + x3))


	wholeTransY = random.randint(minn, maxx - max(y1 + y2 + y3))

	newX1 = []
	newX2 = []
	newX3 = []
	newY1 = []
	newY2 = []
	newY3 = []

	for ex1, ex2, ex3, why1, why2, why3 in zip(x1, x2, x3, y1, y2, y3):
		newX1.append(ex1 + wholeTransX)
		newX2.append(ex2 + wholeTransX)
		newX3.append(ex3 + wholeTransX)
		newY1.append(why1 + wholeTransY)
		newY2.append(why2 + wholeTransY)
		newY3.append(why3 + wholeTransY)

	refVal1 = refVal1 + wholeTransX

	x1 = newX1
	x2 = newX2
	x3 = newX3
	y1 = newY1
	y2 = newY2
	y3 = newY3

	#NOTE: can later switch it to have y = etc
	refVal1Type = 'x'

	randomized = random.choice(['rightX','leftX','downY','upY'])

	if randomized == 'rightX':
		china = 1 #do nothing
	elif randomized == 'leftX':
		# will reflect over y-axis
		x1, y1 = reflectCoordinates(x1, y1, 'x', 0)
		x2, y2 = reflectCoordinates(x2, y2, 'x', 0)
		x3, y3 = reflectCoordinates(x3, y3, 'x', 0)
		refVal1 = refVal1 * -1
	elif randomized == 'downY' or randomized == 'upY':
		if randomized == 'downY':
			direction = 'cc'
		elif randomized == 'upY':
			direction = 'ccw'
		# will need to rotate everything aroudn the origin 90 cw or ccw, refvalues will change and have their own loop
		x1, y1 = rotateCoordinates(x1, y1, 0, 0, direction, 90)
		x2, y2 = rotateCoordinates(x2, y2, 0, 0, direction, 90)
		x3, y3 = rotateCoordinates(x3, y3, 0, 0, direction, 90)

		# for x=refVal1, [refVal1, 0]
		first = [refVal1, 0]

		xs = [refVal1]
		ys = [0]

		newX, newY = rotateCoordinates(xs, ys, 0, 0, direction, 90)

		refVal1 = newY[0]

		refVal1Type = 'y'

	if refVal1Type == 'x':
		if refVal1 != 0:
			refVal1String = 'line $x = %s$' % constantOperation(refVal1, True)
		else:
			refVal1String = '$y-axis$'
	elif refVal1Type == 'y':
		if refVal1 != 0:
			refVal1String = 'line $y = %s$' % constantOperation(refVal1, True)
		else:
			refVal1String = '$x-axis$'

	return refVal1String, transValX, transValY, x1, y1, x2, y2, x3, y3
	#so for it's x= going to the right, then some random translation
	#i would like x= going left, then transation, so that would be flip whole shit over yaxis

	#if i want to do translation first all i ahve to do is reverse coordiantes and such

	#if i want to do y= reflection (or xaxis) rotate 90 clockwise for down,
	#90 counterclockwise for up
class transformations1():
	def __init__(self, type):
		self.type = type

		if self.type == 'SA':
			doc.append(NoEscape('How much woods could a woodchuck chuck if a woodchuck could chuck wood?'))
			doc.append(NewLine())
			length = sizingXY(-10, 10, 'medium')
			hoSpace = (7.5 - length) / 2
			doc.append(HorizontalSpace('%gin' % hoSpace))  # 7.5 width - length / 2
			with doc.create(TikZ(options='x=%gcm, y=%gcm, auto' % (
			length, length))):  # can easily switch it for rectangles in the future
				grid(-10, 10)

			doc.append(NewLine())
			doc.append(NoEscape('You sack of shit'))
			doc.append(VerticalSpace('1in'))
			doc.append(NewLine())
		elif self.type == 'MC':
			with doc.create(Figure(position='th!')):
				doc.append(NoEscape('How much woods could a woodchuck chuck if a woodchuck could chuck wood?'))
				doc.append(NewLine())
				length = sizingXY(-10, 10, 'medium')

				with doc.create(Center()):
					with doc.create(TikZ(options='x=%gcm, y=%gcm' % (
					length, length))):  # can easily switch it for rectangles in the future
						grid(-10, 10)
						x, y = polygon(-10, 10, 'right triangle', 'smaller')
						x, y, rX, rY = dilation(-10, 10, x, y, 'inside', 'integer', 'yes')
						for thing1, thing2, thing3, thing4 in zip(x, y, rX, rY):
							if abs(thing1) > 10 or abs(thing2) > 10 or abs(thing3) > 10 or abs(thing4) > 10:
								print('shhhhheiiitt')

						graphPolygon(x, y, ['A', 'B', 'C'])
						graphPolygon(rX, rY, ['D', 'E', 'F'])

				string1 = '20 woods'
				string2 = '30 woods'
				string4 = r'$\infty$'
				string3 = '20,000 woods'
				stringsDict = {0: string1, 1: string2, 2: string3, 3: string4}

				# for multiple choice
				for i in range(4):
					with doc.create(MiniPage(width=r"0.5\textwidth")):
						doc.append(NoEscape('(%d)' % (i + 1)))
						length = sizingXY(-10, 10, 'small')  # length*20 because size was for xstep etc
						with doc.create(TikZ(options='x=%gcm, y=%gcm' % (
						length, length))):  # can easily switch it for rectangles in the future
							grid(-10, 10)
							x, y = polygon(-10, 10, 'scalene triangle', 'smaller')
							x, y, tX, tY, xV, yV = translation(-10, 10, x, y, '+', '+', 'no')
							graphPolygon(x, y, ['A', 'B', 'C'])
							graphPolygon(tX, tY, ['D', 'E', 'F'])

					if (i % 2) == 1:
						doc.append(VerticalSpace("10pt"))
						doc.append(LineBreak())

class sample2():
	def __init__(self, type):
		self.vSpace = 0
		self.type = type
	def addQuestion(self):
		if self.type == 'SA':
			doc.append(NoEscape('How much woods could a woodchuck chuck if a woodchuck could chuck wood?'))
			doc.append(NewLine())
			length = sizingXY(-10, 10, 'medium')
			hoSpace = (7.5 - length)/2
			doc.append(HorizontalSpace('%gin' % hoSpace)) #7.5 width - length / 2
			with doc.create(TikZ(options='x=%gcm, y=%gcm, auto' % (length, length))):  # can easily switch it for rectangles in the future
				grid(-10, 10)

			doc.append(NewLine())
			doc.append(NoEscape('You sack of shit'))
			doc.append(VerticalSpace('1in'))
			doc.append(NewLine())
		elif self.type == 'MC':
			with doc.create(Figure(position='th!')):
				doc.append(NoEscape('How much woods could a woodchuck chuck if a woodchuck could chuck wood?'))
				doc.append(NewLine())
				length = sizingXY(-10, 10, 'medium')

				with doc.create(Center()):
					with doc.create(TikZ(options='x=%gcm, y=%gcm' % (length, length))):  # can easily switch it for rectangles in the future
							grid(-10, 10)
							x, y = polygon(-10,10,'right triangle','smaller')
							blah, blah, x, y, rX, rY = dilation(-10,10,x,y,'inside','integer','yes')
							for thing1, thing2, thing3, thing4 in zip(x, y, rX, rY):
								if abs(thing1) > 10 or abs(thing2) > 10 or abs(thing3) > 10 or abs(thing4) > 10:
									print('shhhhheiiitt')

							graphPolygon(x, y, ['A', 'B', 'C'])
							graphPolygon(rX, rY, ['D', 'E', 'F'])

				string1 = '20 woods'
				string2 = '30 woods'
				string4 = r'$\infty$'
				string3 = '20,000 woods'
				stringsDict = {0:string1, 1:string2, 2:string3, 3:string4}

				#for multiple choice
				for i in range(4):
					with doc.create(MiniPage(width=r"0.5\textwidth")):
						doc.append(NoEscape('(%d)' % (i+1)))
						length = sizingXY(-10, 10, 'small')# length*20 because size was for xstep etc
						with doc.create(TikZ(options='x=%gcm, y=%gcm' % (length, length))):  # can easily switch it for rectangles in the future
							grid(-10, 10)
							x, y = polygon(-10,10,'scalene triangle','smaller')
							x, y, tX, tY, xV, yV = translation(-10, 10, x, y, '+', '+', 'no')
							graphPolygon(x, y, ['A', 'B', 'C'])
							graphPolygon(tX, tY, ['D', 'E', 'F'])

					if (i % 2) == 1:
						doc.append(VerticalSpace("10pt"))
						doc.append(LineBreak())

#Examples of questions I've created
#Merge info.py  into this file, test make sure shit works, then
#File: updating SQL database with questions
#File: creates document
#File: contains useful fucntions//separated into multiple files etc

class performTranslation(): #need to fix answer key!!!!!!!!! self.l... and docs etc
	def __init__(self, doc, notation, prime, minn, maxx, xChangeAmount, yChangeAmount, overlap):
		self.prime = prime
		self.minn = minn
		self.maxx = maxx
		self.xChangeAmount = xChangeAmount
		self.yChangeAmount = yChangeAmount
		self.overlap = overlap
		self.type = 'SA'
		self.notation = notation
	def addQuestion(self):
		one, two, three = annotatePolygon(self.prime, 3)

		x, y, tX, tY, xVal, yVal = translation(self.minn, self.maxx, self.xChangeAmount, self.yChangeAmount, self.overlap)

		if self.notation == False:
			if xVal < 0:
				xString = '%d units to the left ' % abs(xVal)
			elif xVal > 0:
				xString = '%d units to the right ' % abs(xVal)
			else:
				xString = ''

			if yVal < 0:
				yString = '%d units down' % abs(yVal)
			elif yVal > 0:
				yString = '%d units up' % abs(yVal)
			else:
				yString = ''

			if len(xString) > 0 and len(yString) > 0:
				doc.append(NoEscape(r'Given $\bigtriangleup %s$ on the set of axes below, graph $\bigtriangleup %s$ after a translation of ' % (one[0]+one[1]+one[2], two[0]+two[1]+two[2]) + xString + 'and '+ yString + '.'))
			elif len(xString) == 0 and len(yString) != 0:
				doc.append(NoEscape(
					r'Given $\bigtriangleup %s$ on the set of axes below, graph $\bigtriangleup %s$ after a translation of ' % (
					one[0] + one[1] + one[2], two[0] + two[1] + two[2]) + xString + yString + '.'))
			elif len(xString) != 0 and len(yString) == 0:
				doc.append(NoEscape(
					r'Given $\bigtriangleup %s$ on the set of axes below, graph $\bigtriangleup %s$ after a translation of ' % (
						one[0] + one[1] + one[2], two[0] + two[1] + two[2]) + xString + yString + '.'))
		else:
			if xVal < 0:
				xString = '$(x, y)\Rightarrow(x - %d, ' % abs(xVal)
			elif xVal > 0:
				xString = '$(x, y)\Rightarrow(x + %d, '  % abs(xVal)
			else:
				xString = '$(x, y)\Rightarrow(x, '

			if yVal < 0:
				yString = 'y - %d)$' % abs(yVal)
			elif yVal > 0:
				yString = 'y + %d)$' % abs(yVal)
			else:
				yString = 'y)$'

			doc.append(NoEscape(r'Given $\bigtriangleup %s$ on the set of axes below, graph $\bigtriangleup %s$ after a translation of ' % (one[0]+one[1]+one[2], two[0]+two[1]+two[2]) + xString + yString + '.'))

		doc.append(NewLine())

		length = sizingXY(-10, 10, 'medium')

		with doc.create(Center()):
			with doc.create(TikZ(options='x=%gcm, y=%gcm' % (length, length))):  # can easily switch it for rectangles in the future
				grid(doc, -10, 10)

				graphPolygon(doc, x, y, [one[0], one[1], one[2]], 'black')

	def addAnswer(self):
		one, two, three = annotatePolygon(self.prime, 3)

		x, y = polygon(self.minn, self.maxx, 'right triangle', 'regular')

		x, y, tX, tY, xVal, yVal = translation(self.minn, self.maxx, self.xChangeAmount, self.yChangeAmount, self.overlap)

		if xVal < 0:
			xString = '%d units to the left ' % abs(xVal)
		elif xVal > 0:
			xString = '%d units to the right ' % abs(xVal)
		else:
			xString = ''

		if yVal < 0:
			yString = '%d units down' % abs(yVal)
		elif yVal > 0:
			yString = '%d units up' % abs(yVal)
		else:
			yString = ''

		if len(xString) > 0 and len(yString) > 0:
			docAnswer.append(NoEscape(r'Given $\bigtriangleup %s$ on the set of axes below, graph $\bigtriangleup %s$ after a translation of ' % (one[0]+one[1]+one[2], two[0]+two[1]+two[2]) + xString + 'and '+ yString + '.'))
		elif len(xString) == 0 and len(yString) != 0:
			docAnswer.append(NoEscape(
				r'Given $\bigtriangleup %s$ on the set of axes below, graph $\bigtriangleup %s$ after a translation of ' % (
				one[0] + one[1] + one[2], two[0] + two[1] + two[2]) + xString + yString + '.'))
		elif len(xString) != 0 and len(yString) == 0:
			docAnswer.append(NoEscape(
				r'Given $\bigtriangleup %s$ on the set of axes below, graph $\bigtriangleup %s$ after a translation of ' % (
					one[0] + one[1] + one[2], two[0] + two[1] + two[2]) + xString + yString + '.'))

		docAnswer.append(NewLine())

		length = sizingXY(-10, 10, 'medium')

		with docAnswer.create(Center()):
			with docAnswer.create(TikZ(options='x=%gcm, y=%gcm' % (length, length))):  # can easily switch it for rectangles in the future
				grid(docAnswer, -10, 10)

				graphPolygon(docAnswer, x, y, [one[0], one[1], one[2]], 'black')
				graphPolygon(docAnswer, tX, tY, [two[0], two[1], two[2]], 'red')
class performReflection():
	def __init__(self, doc, prime, minn, maxx, nameOfReflectionList, overlap):
		self.prime = prime
		self.minn = minn
		self.maxx = maxx
		self.nameOfReflectionList = nameOfReflectionList
		self.overlap = overlap
		self.type = 'SA'
	def addQuestion(self):
		self.one, self.two, self.three = annotatePolygon(self.prime, 3)

		self.x, self.y, self.rX, self.rY, self.refVal, self.refValString = reflection(self.minn, self.maxx, self.nameOfReflectionList, self.overlap)

		doc.append(NoEscape(r'Given $\bigtriangleup %s$ on the set of axes below, graph $\bigtriangleup %s$ after a reflection over the ' % (self.one[0]+self.one[1]+self.one[2], self.two[0]+self.two[1]+self.two[2]) + self.refValString + '.'))

		doc.append(NewLine())

		length = sizingXY(-10, 10, 'medium')

		with doc.create(Center()):
			with doc.create(TikZ(options='x=%gcm, y=%gcm' % (length, length))):  # can easily switch it for rectangles in the future
				grid(doc, -10, 10)

				graphPolygon(doc, self.x, self.y, [self.one[0], self.one[1], self.one[2]], 'black')

	def addAnswer(self):
		self.one, self.two, self.three = annotatePolygon(self.prime, 3)

		self.x, self.y = polygon(self.minn, self.maxx, 'right triangle', 'regular')

		self.x, self.y, self.rX, self.rY, self.refVal, self.refValString = reflection(self.minn, self.maxx, self.nameOfReflectionList, self.overlap)

		docAnswer.append(NoEscape(
			r'Given $\bigtriangleup %s$ on the set of axes below, graph $\bigtriangleup %s$ after a reflection over the ' % (
			self.one[0] + self.one[1] + self.one[2],
			self.two[0] + self.two[1] + self.two[2]) + self.refValString + '.'))

		docAnswer.append(NewLine())

		length = sizingXY(-10, 10, 'medium')

		with docAnswer.create(Center()):
			with docAnswer.create(TikZ(options='x=%gcm, y=%gcm' % (length, length))):  # can easily switch it for rectangles in the future
				grid(docAnswer, -10, 10)

				graphPolygon(docAnswer, self.x, self.y, [self.one[0], self.one[1], self.one[2]], 'black')
				graphPolygon(docAnswer, self.rX, self.rY, [self.two[0], self.two[1], self.two[2]], 'red')
class performReflectionReflection():
	def __init__(self, doc, prime, axisOrEquation, options, minn, maxx, case, overlap1, overlap2):
		self.prime = prime
		self.minn = minn
		self.maxx = maxx
		self.case = case
		self.overlap1 = overlap1
		self.overlap2 = overlap2
		self.type = 'SA'
		self.axisOrEquation = axisOrEquation
		self.one, self.two, self.three = annotatePolygon(self.prime, 3)
		self.ref1String, self.ref2String, self.x1, self.y1, self.x2, self.y2, self.x3, self.y3 = reflectionReflection(options, self.minn, self.maxx, self.case,
																			  self.overlap1, self.overlap2)
	def addQuestion(self):
		if self.axisOrEquation == 'equation' and 'axis' in self.ref1String:
			if self.ref1String[1] == 'x':
				self.ref1String = 'line $y = 0$'
			else:
				self.ref1String = 'line $x = 0$'

		if self.axisOrEquation == 'equation' and 'axis' in self.ref2String:
			if self.ref2String[1] == 'x':
				self.ref2String = 'line $y = 0$'
			else:
				self.ref2String = 'line $x = 0$'

		doc.append(NoEscape(r'Given $\bigtriangleup %s$ on the set of axes below, graph $\bigtriangleup %s$ after a reflection over the ' % (self.one[0]+self.one[1]+self.one[2], self.three[0]+self.three[1]+self.three[2]) + self.ref1String + ' followed by a reflection over the ' + self.ref2String + '.'))

		doc.append(NewLine())

		length = sizingXY(-10, 10, 'medium')

		with doc.create(Center()):
			with doc.create(TikZ(options='x=%gcm, y=%gcm' % (length, length))):  # can easily switch it for rectangles in the future
				grid(doc, -10, 10)

				graphPolygon(doc, self.x1, self.y1, [self.one[0], self.one[1], self.one[2]], 'black')

	def addAnswer(self):
		if self.axisOrEquation == 'equation' and 'axis' in self.ref1String:
			if self.ref1String[1] == 'x':
				self.ref1String = 'line $y = 0$'
			else:
				self.ref1String = 'line $x = 0$'

		if self.axisOrEquation == 'equation' and 'axis' in self.ref2String:
			if self.ref2String[1] == 'x':
				self.ref2String = 'line $y = 0$'
			else:
				self.ref2String = 'line $x = 0$'

		docAnswer.append(NoEscape(r'Given $\bigtriangleup %s$ on the set of axes below, graph $\bigtriangleup %s$ after a reflection over the ' % (self.one[0]+self.one[1]+self.one[2], self.three[0]+self.three[1]+self.three[2]) + self.ref1String + ' followed by a reflection over the ' + self.ref2String + '.'))

		docAnswer.append(NewLine())

		length = sizingXY(-10, 10, 'medium')

		with docAnswer.create(Center()):
			with docAnswer.create(TikZ(
					options='x=%gcm, y=%gcm' % (length, length))):  # can easily switch it for rectangles in the future
				grid(docAnswer, -10, 10)

				graphPolygon(docAnswer, self.x1, self.y1, [self.one[0], self.one[1], self.one[2]], 'black')
				graphPolygon(docAnswer, self.x2, self.y2, [self.two[0], self.two[1], self.two[2]], 'gray')
				graphPolygon(docAnswer, self.x3, self.y3, [self.three[0], self.three[1], self.three[2]], 'red')
class performReflectionTranslation(): #need to add in y= etc etc etc
	def __init__(self, prime, axisOrEquation, notation, refList, minn, maxx, overlap1, overlap2, doc = None, docAnswer = None):
		#let's me put None in keyword argument?
		if doc == None:
			doc = createDocument()
		if docAnswer == None:
			docAnswer = createDocument()

		self.prime = prime
		self.minn = minn
		self.maxx = maxx
		self.overlap1 = overlap1
		self.overlap2 = overlap2
		self.type = 'SA'
		self.axisOrEquation = axisOrEquation
		self.refList = refList
		self.notation = notation

	def addQuestion(self, doc = None):
		self.one, self.two, self.three = annotatePolygon(self.prime, 3)
		self.ref1String, self.xVal, self.yVal, self.x1, self.y1, self.x2, self.y2, self.x3, self.y3 = reflectionTranslation(self.minn, self.maxx, self.refList, self.overlap1, self.overlap2)

		if self.notation == False:
			if self.xVal < 0:
				self.xString = '%d units to the left ' % abs(self.xVal)
			elif self.xVal > 0:
				self.xString = '%d units to the right ' % abs(self.xVal)
			else:
				self.xString = ''

			if self.yVal < 0:
				self.yString = '%d units down' % abs(self.yVal)
			elif self.yVal > 0:
				self.yString = '%d units up' % abs(self.yVal)
			else:
				self.yString = ''
		else:
			if self.xVal < 0:
				self.xString = '$(x, y)\Rightarrow(x - %d, ' % abs(self.xVal)
			elif self.xVal > 0:
				self.xString = '$(x, y)\Rightarrow(x + %d, '  % abs(self.xVal)
			else:
				self.xString = '$(x, y)\Rightarrow(x, '

			if self.yVal < 0:
				self.yString = 'y - %d)$' % abs(self.yVal)
			elif self.yVal > 0:
				self.yString = 'y + %d)$' % abs(self.yVal)
			else:
				self.yString = 'y)$'

		if self.axisOrEquation == 'equation' and 'axis' in self.ref1String:
			if self.ref1String[1] == 'x':
				self.ref1String = 'line $y = 0$'
			else:
				self.ref1String = 'line $x = 0$'


		doc.append(NoEscape(r'Given $\bigtriangleup %s$ on the set of axes below, graph $\bigtriangleup %s$ after a reflection over the ' % (self.one[0]+self.one[1]+self.one[2], self.three[0]+self.three[1]+self.three[2]) + self.ref1String + ' followed by a translation of ' + self.xString + self.yString + '.'))

		doc.append(NewLine())

		length = sizingXY(-10, 10, 'medium')

		with doc.create(Center()):
			with doc.create(TikZ(options='x=%gcm, y=%gcm' % (length, length))):  # can easily switch it for rectangles in the future
				grid(doc, -10, 10)

				graphPolygon(doc, self.x1, self.y1, [self.one[0], self.one[1], self.one[2]], 'black')

	def addAnswer(self, docAnswer = None):
		if self.axisOrEquation == 'equation' and 'axis' in self.ref1String:
			if self.ref1String[1] == 'x':
				self.ref1String = 'line $y = 0$'
			else:
				self.ref1String = 'line $x = 0$'

		if self.axisOrEquation == 'equation' and 'axis' in self.ref2String:
			if self.ref2String[1] == 'x':
				self.ref2String = 'line $y = 0$'
			else:
				self.ref2String = 'line $x = 0$'

		docAnswer.append(NoEscape(r'Given $\bigtriangleup %s$ on the set of axes below, graph $\bigtriangleup %s$ after a reflection over the ' % (self.one[0]+self.one[1]+self.one[2], self.three[0]+self.three[1]+self.three[2]) + self.ref1String + ' followed by a translation of ' + self.xString + self.yString + '.'))

		docAnswer.append(NewLine())

		length = sizingXY(-10, 10, 'medium')

		with docAnswer.create(Center()):
			with docAnswer.create(TikZ(
					options='x=%gcm, y=%gcm' % (length, length))):  # can easily switch it for rectangles in the future
				grid(docAnswer, -10, 10)

				graphPolygon(docAnswer, self.x1, self.y1, [self.one[0], self.one[1], self.one[2]], 'black')
				graphPolygon(docAnswer, self.x2, self.y2, [self.two[0], self.two[1], self.two[2]], 'gray')
				graphPolygon(docAnswer, self.x3, self.y3, [self.three[0], self.three[1], self.three[2]], 'red') #f#FIX FOR ANSWER KEYEEEEEE
class performRotation():#answerkey!!!
	def __init__(self, doc, prime, minn, maxx, center, degrees, direction, overlap, rigidMotionOption):
		self.prime = prime
		self.minn = minn
		self.maxx = maxx
		self.overlap = overlap
		self.type = 'SA'
		self.center = center
		self.degrees = degrees
		self.direction = direction
		self.rigidMotionOption = rigidMotionOption
	def addQuestion(self):
		self.one, self.two, self.three = annotatePolygon(self.prime, 3)

		self.x, self.y, self.rotX, self.rotY, self.center, self.degrees, self.direction = rotation(-10, 10, self.center, self.degrees, self.direction, self.overlap)

		if self.direction == 'cc':
			self.dirStr = 'clockwise'
		elif self.direction == 'ccw':
			self.dirStr = 'counterclockwise'

		doc.append(NoEscape(r'Given $\bigtriangleup %s$ on the set of axes below, graph $\bigtriangleup %s$ after a rotation of ' % (self.one[0]+self.one[1]+self.one[2], self.two[0]+self.two[1]+self.two[2]) + '$%d^\circ$' % self.degrees + ' ' + self.dirStr + ' around the origin.'))

		doc.append(NewLine())

		if self.rigidMotionOption == True:
			doc.append(NewLine())
			doc.append(NoEscape(r'Explain why $\bigtriangleup %s$ $\cong$ $\bigtriangleup %s$' % (self.one[0]+self.one[1]+self.one[2], self.two[0]+self.two[1]+self.two[2])))

		doc.append(NewLine())

		length = sizingXY(-10, 10, 'medium')

		with doc.create(Center()):
			with doc.create(TikZ(options='x=%gcm, y=%gcm' % (length, length))):  # can easily switch it for rectangles in the future
				grid(doc, -10, 10)

				graphPolygon(doc, self.x, self.y, [self.one[0], self.one[1], self.one[2]], 'black')



	def addAnswer(self):
		self.one, self.two, self.three = annotatePolygon(self.prime, 3)

		self.x, self.y = polygon(self.minn, self.maxx, 'right triangle', 'regular')

		self.x, self.y, self.rX, self.rY, self.refVal, self.refValString = reflection(self.minn, self.maxx, self.x, self.y, self.nameOfReflectionList, self.overlap)

		docAnswer.append(NoEscape(
			r'Given $\bigtriangleup %s$ on the set of axes below, graph $\bigtriangleup %s$ after a reflection over the ' % (
			self.one[0] + self.one[1] + self.one[2],
			self.two[0] + self.two[1] + self.two[2]) + self.refValString + '.'))

		docAnswer.append(NewLine())

		length = sizingXY(-10, 10, 'medium')

		with docAnswer.create(Center()):
			with docAnswer.create(TikZ(options='x=%gcm, y=%gcm' % (length, length))):  # can easily switch it for rectangles in the future
				grid(docAnswer, -10, 10)

				graphPolygon(docAnswer, self.x, self.y, [self.one[0], self.one[1], self.one[2]], 'black')
				graphPolygon(docAnswer, self.rX, self.rY, [self.two[0], self.two[1], self.two[2]], 'red')
class identifyRotation():
	def __init__(self, doc, minn, maxx, prime, center, degrees, direction, overlap):
		self.center = center
		self.degrees = degrees
		self.direction = direction
		self.minn = minn
		self.maxx = maxx
		self.overlap = overlap
		self.prime = prime
	def addQuestion(self):
		self.x, self.y, self.rotX, self.rotY, self.center, self.degrees, self.direction = rotation(self.minn, self.maxx, self.center, self.degrees, self.direction, self.overlap)
		self.one, self.two, self.three = annotatePolygon(self.prime, 3)

		if self.center == [0,0]:
			self.centerStr = 'the origin'
		else:
			self.centerX = self.center[0]
			self.centerY = self.center[1]
			self.centerStr = '(%d, %d)' % (self.centerX, self.centerY)

		if self.direction == 'cc':
			self.dirStr = 'clockwise'
		elif self.direction == 'ccw':
			self.dirStr = 'counterclockwise'

		doc.append(NoEscape(r'On the set of axes below, identify the transformation that maps $\bigtriangleup %s$ onto $\bigtriangleup %s$.' % (self.one[0]+self.one[1]+self.one[2], self.two[0]+self.two[1]+self.two[2])))

		doc.append(NewLine())

		length = sizingXY(-10, 10, 'medium')

		with doc.create(Center()):
			with doc.create(TikZ(options='x=%gcm, y=%gcm' % (length, length))):  # can easily switch it for rectangles in the future
				grid(doc, self.minn, self.maxx)

				graphPolygon(doc, self.x, self.y, [self.one[0], self.one[1], self.one[2]], 'black')
				graphPolygon(doc, self.rotX, self.rotY, [self.two[0], self.two[1], self.two[2]], 'black')

	def addAnswer(self):
		doc.append(NoEscape('rotation $%d^\circ$' % self.degrees + ' ' + self.dirStr + ' around %s' % self.centerStr))

		doc.append(NewLine())

		length = sizingXY(-10, 10, 'medium')

		with doc.create(Center()):
			with doc.create(TikZ(options='x=%gcm, y=%gcm' % (length, length))):  # can easily switch it for rectangles in the future
				grid(doc, self.minn, self.maxx)

				graphPolygon(doc, self.x, self.y, [self.one[0], self.one[1], self.one[2]], 'black')
				graphPolygon(doc, self.rotX, self.rotY, [self.two[0], self.two[1], self.two[2]], 'black')
class identifyReflection():
	def __init__(self, doc, minn, maxx, prime, nameOfReflectionList, overlap):
		self.nameOfReflectionList = nameOfReflectionList

		self.minn = minn
		self.maxx = maxx

		self.overlap = overlap

		self.prime = prime

	def addQuestion(self):
		self.x, self.y, self.self.refX, self.self.refY, self.refVal, self.refValString = reflection(self.minn, self.maxx, self.nameOfReflectionList, self.overlap)

		self.one, self.two, self.three = annotatePolygon(self.prime, 3)

		doc.append(NoEscape(
			r'On the set of axes below, identify the transformation that maps $\bigtriangleup %s$ onto $\bigtriangleup %s$.' % (
			self.one[0] + self.one[1] + self.one[2], self.two[0] + self.two[1] + self.two[2])))

		doc.append(NewLine())

		length = sizingXY(-10, 10, 'medium')

		with doc.create(Center()):
			with doc.create(TikZ(
					options='x=%gcm, y=%gcm' % (length, length))):  # can easily switch it for rectangles in the future
				grid(doc, self.minn, self.maxx)

				graphPolygon(doc, self.x, self.y, [self.one[0], self.one[1], self.one[2]], 'black')
				graphPolygon(doc, self.self.refX, self.self.refY, [self.two[0], self.two[1], self.two[2]], 'black')

	def addAnswer(self):
		doc.append(NoEscape('Reflection over %s' % self.refValString))

		doc.append(NewLine())

		length = sizingXY(-10, 10, 'medium')

		with doc.create(Center()):
			with doc.create(TikZ(
					options='x=%gcm, y=%gcm' % (length, length))):  # can easily switch it for rectangles in the future
				grid(doc, self.minn, self.maxx)

				graphPolygon(doc, self.x, self.y, [self.one[0], self.one[1], self.one[2]], 'black')
				graphPolygon(doc, self.self.refX, self.self.refY, [self.two[0], self.two[1], self.two[2]], 'black')
class identifyTranslation():
	def __init__(self, doc, minn, maxx, prime, xChangeAmount, yChangeAmount, overlap):
		self.xChangeAmount = xChangeAmount
		self.yChangeAmount = yChangeAmount

		self.minn = minn
		self.maxx = maxx

		self.overlap = overlap
		self.prime = prime
	def addQuestion(self):
		self.x, self.y, self.tX, self.tY, self.xVal, self.yVal  = translation(self.minn, self.maxx, self.xChangeAmount, self.yChangeAmount, self.overlap)
		self.one, self.two, self.three = annotatePolygon(self.prime, 3)

		doc.append(NoEscape(
			r'On the set of axes below, identify the transformation that maps $\bigtriangleup %s$ onto $\bigtriangleup %s$.' % (
				self.one[0] + self.one[1] + self.one[2], self.two[0] + self.two[1] + self.two[2])))

		doc.append(NewLine())

		length = sizingXY(-10, 10, 'medium')

		with doc.create(Center()):
			with doc.create(TikZ(
					options='x=%gcm, y=%gcm' % (length, length))):  # can easily switch it for rectangles in the future
				grid(doc, self.minn, self.maxx)

				graphPolygon(doc, self.x, self.y, [self.one[0], self.one[1], self.one[2]], 'black')
				graphPolygon(doc, self.tX, self.tY, [self.two[0], self.two[1], self.two[2]], 'black')

	def addAnswer(self):
		if self.xVal < 0:
			xString = '%d units to the left ' % abs(self.xVal)
		elif self.xVal > 0:
			xString = '%d units to the right ' % abs(self.xVal)
		else:
			xString = ''

		if self.yVal < 0:
			yString = '%d units down' % abs(self.yVal)
		elif self.yVal > 0:
			yString = '%d units up' % abs(self.yVal)
		else:
			yString = ''

		if len(xString) > 0 and len(yString) > 0:
			doc.append(NoEscape(
				r'Translation of ' + xString + 'and ' + yString + '.'))
		elif len(xString) == 0 and len(yString) != 0:
			doc.append(NoEscape(
				r'Translation of ' + xString + yString + '.'))
		elif len(xString) != 0 and len(yString) == 0:
			doc.append(NoEscape(
				r'Translation of ' + xString + yString + '.'))

		doc.append(NewLine())

		length = sizingXY(-10, 10, 'medium')

		with doc.create(Center()):
			with doc.create(TikZ(
					options='x=%gcm, y=%gcm' % (length, length))):  # can easily switch it for rectangles in the future
				grid(doc, self.minn, self.maxx)

				graphPolygon(doc, self.x, self.y, [self.one[0], self.one[1], self.one[2]], 'black')
				graphPolygon(doc, self.tX, self.tY, [self.two[0], self.two[1], self.two[2]], 'black')

class identifyTranslationReflection():
	def __init__(self, doc, prime, middleShape, notation, minn, maxx, refList, overlap1, overlap2):
		self.prime = prime
		self.minn = minn
		self.maxx = maxx
		self.overlap1 = overlap1
		self.overlap2 = overlap2
		self.type = 'SA'
		self.middleShape = middleShape
		self.refList = refList
		self.notation = notation
	def addQuestion(self):
		self.one, self.two, self.three = annotatePolygon(self.prime, 3)
		self.ref1String, self.xVal, self.yVal, self.x1, self.y1, self.x2, self.y2, self.x3, self.y3 = reflectionTranslation(self.minn, self.maxx, self.refList, self.overlap1, self.overlap2)

		doc.append(NoEscape(r'Given the graph below, identify the sequence of transformations that maps $\bigtriangleup %s$ onto $\bigtriangleup %s$.' % (self.one[0]+self.one[1]+self.one[2], self.three[0]+self.three[1]+self.three[2])))

		doc.append(NewLine())

		length = sizingXY(-10, 10, 'medium')

		with doc.create(Center()):
			with doc.create(TikZ(options='x=%gcm, y=%gcm' % (length, length))):  # can easily switch it for rectangles in the future
				grid(doc, -10, 10)

				graphPolygon(doc, self.x1, self.y1, [self.one[0], self.one[1], self.one[2]], 'black')
				if self.middleShape == True:
					graphPolygon(doc, self.x2, self.y2, [self.two[0], self.two[1], self.two[2]], 'black')
				graphPolygon(doc, self.x3, self.y3, [self.three[0], self.three[1], self.three[2]], 'black')

	def addAnswer(self):
		if self.notation == False:
			if self.xVal < 0:
				xString = '%d units to the left ' % abs(self.xVal)
			elif self.xVal > 0:
				xString = '%d units to the right ' % abs(self.xVal)
			else:
				xString = ''

			if self.yVal < 0:
				yString = '%d units down' % abs(self.yVal)
			elif self.yVal > 0:
				yString = '%d units up' % abs(self.yVal)
			else:
				yString = ''
		else:
			if self.xVal < 0:
				xString = '$(x, y)\Rightarrow(x - %d, ' % abs(self.xVal)
			elif self.xVal > 0:
				xString = '$(x, y)\Rightarrow(x + %d, '  % abs(self.xVal)
			else:
				xString = '$(x, y)\Rightarrow(x, '

			if self.yVal < 0:
				yString = 'y - %d)$' % abs(self.yVal)
			elif self.yVal > 0:
				yString = 'y + %d)$' % abs(self.yVal)
			else:
				yString = 'y)$'

		if self.axisOrEquation == 'equation' and 'axis' in self.ref1String:
			if self.ref1String[1] == 'x':
				self.ref1String = 'line $y = 0$'
			else:
				self.ref1String = 'line $x = 0$'

		docAnswer.append(NoEscape(r'Given $\bigtriangleup %s$ on the set of axes below, graph $\bigtriangleup %s$ after a reflection over the ' % (self.one[0]+self.one[1]+self.one[2], self.three[0]+self.three[1]+self.three[2]) + self.ref1String + ' followed by a reflection over the ' + self.ref2String + '.'))

		docAnswer.append(NewLine())

		length = sizingXY(-10, 10, 'medium')

		with docAnswer.create(Center()):
			with docAnswer.create(TikZ(
					options='x=%gcm, y=%gcm' % (length, length))):  # can easily switch it for rectangles in the future
				grid(docAnswer, -10, 10)

				graphPolygon(docAnswer, self.x1, self.y1, [self.one[0], self.one[1], self.one[2]], 'black')
				graphPolygon(docAnswer, self.x2, self.y2, [self.two[0], self.two[1], self.two[2]], 'gray')
				graphPolygon(docAnswer, self.x3, self.y3, [self.three[0], self.three[1], self.three[2]], 'red') #f#FIX FOR ANSWER KEYEEEEEE


def translateAnywhere(xs = [], ys = [], minn = -10, maxx = 10):
	print('xs',xs)
	print('ys',ys)
	xChange = random.choice([x for x in range(minn-min(xs), maxx-max(xs)+1)])
	yChange = random.choice([x for x in range(minn-min(ys), maxx-max(ys)+1)])

	#moving shit now
	newXs, newYs = translateCoordinates(xs, ys, xChange, yChange)
	print('newXs',newXs)
	print('newYs',newYs)
	return newXs, newYs, xChange, yChange