import random
import sys
sys.path.append("../creatingWorksheets")
from utils.equations import formatMathString
import math

class _8():
    def __init__(self, option = "Given radius", wholeFigureRotation = 0, roundingInTermsOfPi = False):
        self.kwargs = {"roundingInTermsOfPi": True, "wholeFigureRotation": [None, 0, 45, 90, 135, 180], "option": ["Given radius", "Given diameter"]}
        self.toolTips = {
        "pictureDrawn": "Picture is drawn", 
        "option": "Given Information",
        "roundingInTermsOfPi": "Round final answer in terms of pi", 
        "wholeFigureRotation": "Degrees Rotated"}

        height = random.randint(6, 12)
        diameter = random.randint(height-4, height+2) #keeps cone right size
        radius = diameter/2 #radius shoudl be smaller than height??
        #keep int etc
        if diameter % radius == 0:
            radius = int(radius)
        
        volume = math.pi * radius ** 2 * height
        shape = 'cylinder'

        roundingStrings = ['whole number', 'tenth', 'hundredth', 'thousandth']
        roundingChosen = random.choice(roundingStrings)
        if not roundingInTermsOfPi:
            self.answer = round(volume, roundingStrings.index(roundingChosen))   
        else:
            self.answer = formatMathString(f"{radius ** 2 * height}\pi")

        self.question = ""

        if wholeFigureRotation is None:
            self.question = 'Given a %s, ' % shape

            #Starting Info
            if option == "Given radius":
                startingInfo = "the radius is %g" % radius
            else:
                startingInfo = "the diameter is %g" % diameter

            self.question += f'{startingInfo} and the height is {height}, '

            if not roundingInTermsOfPi:
                self.question += rf'find the volume rounded to the nearest \textit{{{roundingChosen}}}.'
            else:
                self.question += "find the volume in terms of "
                self.question += formatMathString("\pi.")
        else:
            self.question = rf"round to the nearest \textit{{{roundingChosen}}}"
        self.directions = "Find the volume:"
        
        if wholeFigureRotation is not None:
            self.question = [{"text": self.question}, {"picture": {"cylinder": {"wholeFigureRotation": wholeFigureRotation, "diagramLabeled": True, "height": height, "radius": radius, "diameter": diameter, "baseRotation": 0, "radiusDrawn": option == "Given radius", "diameterDrawn": option != "Given radius"}}}]
       
