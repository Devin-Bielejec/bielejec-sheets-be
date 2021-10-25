import random
import sys
sys.path.append("../creatingWorksheets")
from utils.equations import formatMathString
import math

class _10():
    def __init__(self, pictureDrawn = True, option = "Given radius", roundingInTermsOfPi = False):
        self.kwargs = {"pictureDrawn": True, "roundingInTermsOfPi": True, "option": ["Given radius", "Given diameter"]}
        self.toolTips = {
        "pictureDrawn": "Picture is drawn", 
        "option": "Given Information","roundingInTermsOfPi": "Round final answer in terms of pi"
        }

        radius = random.choice([x for x in range(3,30,3)])
        diameter = radius * 2

        volume = math.pi * 4/3 * radius ** 3
        volumeNoPi = 4/3 * radius ** 3
        shape = 'sphere'

        roundingStrings = ['whole number', 'tenth', 'hundredth', 'thousandth']
        roundingChosen = random.choice(roundingStrings)
        if not roundingInTermsOfPi:
            self.answer = round(volume, roundingStrings.index(roundingChosen))   
        else:
            self.answer = formatMathString(f"{volumeNoPi}\pi")

        self.question = ""

        if not pictureDrawn:
            self.question = 'Given a %s, ' % shape

            #Starting Info
            if option == "Given radius":
                startingInfo = "the radius is %g" % radius
            else:
                startingInfo = "the diameter is %g" % diameter

        
            self.question += f'{startingInfo}, '

            if not roundingInTermsOfPi:
                self.question += rf'find the volume rounded to the nearest \textit{{{roundingChosen}}}.'
            else:
                self.question += "find the volume in terms of "
                self.question += formatMathString("\pi.")
        else:
            if not roundingInTermsOfPi:
                self.question = rf"round to the nearest \textit{{{roundingChosen}}}"
            else:
                self.question += "round in terms of "
                self.question += formatMathString("\pi.")
        self.duplicateCheck = f"sphereradius{radius}"
        self.directions = "Find the volume:"
        if pictureDrawn == True:
            self.question = [{"text": self.question}, {"picture": {"sphere": {"wholeFigureRotation": 0, "diagramLabeled": True,  "radius": radius, "diameter": diameter, "baseRotation": 0, "radiusDrawn": option == "Given radius", "diameterDrawn": option != "Given radius"}}}]
       
