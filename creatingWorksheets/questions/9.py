import random
import sys
sys.path.append("../creatingWorksheets")
from utils.equations import formatMathString
import math

class _9():
    def __init__(self, option = "Given radius", roundingInTermsOfPi = False, wholeFigureRotation = 0):
        self.kwargs = {"option": ["Given radius", "Given diameter"], "roundingInTermsOfPi": False, "wholeFigureRotation": [None,0,45,90, 135, 180]}
        self.toolTips = {
        "pictureDrawn": "Picture is drawn", "wholeFigureRotation": "Degrees Rotated" ,
        "option": "Given Information","roundingInTermsOfPi": "Round final answer in terms of pi"}

        height = random.choice([6,9,12,15,18,21,24,27,30])
        diameter = random.choice([x for x in range(height-4, height+2) if x % 2 == 0])
        radius = diameter/2 #radius shoudl be smaller than height??

        volume = math.pi * radius ** 2 * height * 1/3
        shape = 'cone'

        roundingStrings = ['whole number', 'tenth', 'hundredth', 'thousandth']
        roundingChosen = random.choice(roundingStrings)
        if not roundingInTermsOfPi:
            self.answer = round(volume, roundingStrings.index(roundingChosen))   
        else:
            self.answer = formatMathString(f"{radius **2 * height * 1/3}\pi")

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
            if not roundingInTermsOfPi:
                self.question = rf"round to the nearest \textit{{{roundingChosen}}}"
            else:
                self.question += "round in terms of "
                self.question += formatMathString("\pi.")

        self.directions = "Find the volume:"
        self.duplicateCheck = f"coneheight{height}radius{radius}"
        if wholeFigureRotation is not None:
            self.question = [{"text": self.question}, {"picture": {"cone": {"wholeFigureRotation": wholeFigureRotation, "diagramLabeled": True, "height": height, "radius": radius, "diameter": diameter, "baseRotation": 0, "radiusDrawn": option == "Given radius", "diameterDrawn": option != "Given radius"}}}]
       
