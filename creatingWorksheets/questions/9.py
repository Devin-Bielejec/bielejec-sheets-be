import random
import sys
sys.path.append("../creatingWorksheets")
from utils.equations import formatMathString
import math

class _9():
    def __init__(self, diagramLabeled = True, rounding = "whole number", pictureDrawn = True, partsGivenInWords = True, option = "Given radius"):
        self.kwargs = {"diagramLabeled": True, "rounding": ["whole number", "tenth", "hundredth", "thousandth", "in terms of pi"], "pictureDrawn": True, "partsGivenInWords": True, "option": ["Given radius", "Given diameter"]}
        self.toolTips = {
        "diagramLabeled": "Length of prism is labeled",            
        "rounding": {"whole number": "Whole Number", "tenth": "Tenth", "hundredth": "Hundredth", "thousandth": "Thousandth", "in terms of pi": "pi in answer"}, 
        "pictureDrawn": "Picture is drawn", 
        "partsGivenInWords": "Parts described in question",
        "option": "Given Information"}

        roundingChosen = random.choice(self.kwargs["rounding"])

        height = random.choice([6,9,12,15,18])
        diameter = random.randint(height-4, height+2) #keeps cone right size
        radius = diameter/2 #radius shoudl be smaller than height??
        #keep int etc
        if diameter % radius == 0:
            radius = int(radius)
        
        volume = math.pi * radius ** 2 * height * 1/3
        shape = 'cone'

        roundingStrings = ['whole number', 'tenth', 'hundredth', 'thousandth']
        if roundingChosen != "in terms of pi":
            self.answer = round(volume, roundingStrings.index(roundingChosen))   
        else:
            self.answer = formatMathString(f"{radius **2 * height * 1/3}\pi")

        #If picture is not drawn, words need to be in question and vice versa
        if pictureDrawn == False:
            partsGivenInWords = True
        if partsGivenInWords == False:
            pictureDrawn = True
            diagramLabeled = True

        self.question = ""

        if pictureDrawn == True:
            self.question = 'Given the %s below, ' % shape
        else:
            self.question = 'Given a %s, ' % shape

        #Starting Info
        if option == "Given radius":
            startingInfo = "the radius is %g" % radius
        else:
            startingInfo = "the diameter is %g" % diameter

        if partsGivenInWords == True:
            self.question += f'the {startingInfo} and the height is {height}, '

        if roundingChosen != "in terms of pi":
            self.question += 'find the volume rounded to the nearest %s.' % (roundingChosen)
        else:
            self.question += "find the volume in terms of "
            self.question += formatMathString("\pi.")

        if pictureDrawn == True:
            self.question = [{"text": self.question}, {"picture": {"cone": {"wholeFigureRotation": 0, "diagramLabeled": diagramLabeled, "height": height, "radius": radius, "diameter": diameter, "baseRotation": 0, "radiusDrawn": option == "Given radius", "diameterDrawn": option != "Given radius"}}}]
       
