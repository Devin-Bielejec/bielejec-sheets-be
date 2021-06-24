class _5():
	def __init__(self, wholeFigureRotation = 0, sideLabeledOnDiagram = True, rounding = "whole number", pictureDrawn = True,  partsGivenInWords = True):
		#Oblique
        self.kwargs = {"wholeFigureRotation": [0, 90], "edgeLabeled": True, "rounding": ["whole number", "tenth", "hundredth", "thousandth"], "pictureDrawn": True, "edgeGivenInWords": True}
        self.toolTips = {
                    "wholeFigureRotation": {0: "normal orientation", 90: "turned on side"}, 
                    "edgeLabeled": "Edge of Cube is labeled", 
                    "rounding": {"whole number": "Whole Number", "tenth": "Tenth", "hundredth": "Hundredth", "thousandth": "Thousandth"}, 
                    "pictureDrawn": "Picture is drawn", 
                    "edgeGivenInWords": "Edge length described in question"}

		

	def addQuestion(self, doc = None):
		roundingChosen = random.choice(self.rounding)
		optionChosen = random.choice(self.option)

		#If picture: Given the right circular cone below, if the radius is 4 and the height is 10, what is the volume rounded to the nearest whole number?
		length = random.randint(10,20)
		width = length
		height = length
		shape = 'cube'

		volume = length * width * height
		roundedVolume = roundGivenString(string = roundingChosen, value = volume)

		if self.pictureDrawn == True:
			introString = 'Given the %s below, ' % shape
		else:
			introString = 'Given a %s, ' % shape

		if self.partsGivenInWords == True:
			givenString = 'the side length is %g, ' % (length)
		else:
			givenString = ""

		roundingString = 'find the volume rounded to the nearest %s.' % (roundingChosen)
		self.answer = roundedVolume

		doc.append(NoEscape(r'' + introString + givenString + roundingString))

		doc.append(NewLine())

		if self.pictureDrawn == True:
			with doc.create(Center()):
				cube(options = 'rotate=%d, x=2.5cm, y=2.5cm' % (self.wholeFigureRotation), 
					doc = doc, 
					sideLabeledOnDiagram = self.sideLabeledOnDiagram, 
					sideValue = length)
		else:
			doc.append(VerticalSpace('2in'))


	def addAnswer(self, docAnswer = None):
		docAnswer.append(NoEscape(r'' + str(self.answer)))