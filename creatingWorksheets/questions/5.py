import random

class _5():
	def __init__(self, pictureDrawn = True):
		#Oblique
		self.kwargs = {"pictureDrawn": True}
		self.toolTips = {
                    "pictureDrawn": "Picture is drawn", 
					}

		side = random.randint(10,20)

		volume = side**3
		self.question = ""
		if not pictureDrawn:
			self.question = f'Given a cube, with a side length of {side}'
		
		#Add rounding string
		roundingStrings = ["whole number", "tenth", "hundredth", "thousandth"]
		roundingChosen = random.choice(roundingStrings)
		
		if not pictureDrawn:
			self.question += rf'find the volume rounded to the nearest \textit{{{roundingChosen}}}.'
		else:
			self.question += rf'round to the nearest \textit{{{roundingChosen}}}'
		
		self.answer = round(volume, roundingStrings.index(roundingChosen))

		if pictureDrawn:
			self.question = [
			{"text": self.question},
			{"picture": {
				"cube": {"wholeFigureRotation": 0, "sideLabeledOnDiagram": True, "sideValue": side}
			}}
		]


		self.directions = "Find the volume:"
			
	

