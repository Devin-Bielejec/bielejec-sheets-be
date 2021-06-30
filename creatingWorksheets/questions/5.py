import random

class _5():
	def __init__(self, wholeFigureRotation = 0, sideLabeledOnDiagram = True, rounding = "whole number", pictureDrawn = True,  edgeGivenInWords = True):
		#Oblique
		self.kwargs = {"wholeFigureRotation": [0, 90], "edgeLabeled": True, "rounding": ["whole number", "tenth", "hundredth", "thousandth"], "pictureDrawn": True, "edgeGivenInWords": True}
		self.toolTips = {
                    "wholeFigureRotation": {0: "normal orientation", 90: "turned on side"}, 
                    "edgeLabeled": "Edge of Cube is labeled", 
                    "rounding": {"whole number": "Whole Number", "tenth": "Tenth", "hundredth": "Hundredth", "thousandth": "Thousandth"}, 
                    "pictureDrawn": "Picture is drawn", 
                    "edgeGivenInWords": "Edge length described in question"}

		#If picture is not drawn, words need to be in question and vice versa
		if pictureDrawn == False:
			edgeGivenInWords = True
		if edgeGivenInWords == False:
			pictureDrawn = True
			edgeGivenInWords = True

		side = random.randint(10,20)

		volume = side**3

		introString = ""

		if pictureDrawn:
			introString = f'Given the cube below '
		else:
			introString = 'Given a cube '

		if edgeGivenInWords == True:
			introString += f'with a side length of {side}, '

		#Add rounding string
		introString += rf'find the volume rounded to the nearest \textit{{{rounding}}}.'

		roundingStrings = ["whole number", "tenth", "hundredth", "thousandth"]

		self.answer = round(volume, roundingStrings.index(rounding))

		if pictureDrawn:
			self.question = [
			{"text": introString},
			{"picture": {
				"cube": {"wholeFigureRotation": wholeFigureRotation, "sideLabeledOnDiagram": sideLabeledOnDiagram, "sideValue": side}
			}}
		]
		else:
			self.question = introString
			
	

