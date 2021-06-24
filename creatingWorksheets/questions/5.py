class findCubeVolume(): #need to fix answer key!!!!!!!!! self.l... and docs etc
	def __init__(self, default = False, wholeFigureRotation = 0, sideLabeledOnDiagram = True, rounding = ['whole number', 'tenth', 'hundredth', 'thousandth'], pictureDrawn = True, option = ['Cube'], partsGivenInWords = True):
		#Oblique

		if default == True:
			self.wholeFigureRotation = 0
			
			self.sideLabeledOnDiagram = True

			self.rounding = ['whole number']
			self.pictureDrawn = True
			self.option = ['Cube']
			self.partsGivenInWords = True
		else:
			self.defaultKwargs = {'default':False, 
			'wholeFigureRotation':0, 

			'sideLabeledOnDiagram':True, 
			'rounding':['whole number', 'tenth', 'hundredth', 'thousandth'],
			'pictureDrawn':True,
			'option':['Cube'],
			'partsGivenInWords':True}

			self.wholeFigureRotation = wholeFigureRotation
			self.rounding = rounding
			self.pictureDrawn = pictureDrawn
			self.option = option
			self.partsGivenInWords = partsGivenInWords

			self.sideLabeledOnDiagram = sideLabeledOnDiagram

		self.topics = ['3D']
		self.skills = ['Determine the volume of a cube']
		self.ID = self.topics[0] + 'determineVolumeCube'

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