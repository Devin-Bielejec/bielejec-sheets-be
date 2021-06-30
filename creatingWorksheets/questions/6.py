import random

class _6():
    def __init__(self, diagramLabeled = True, rounding = "whole number", pictureDrawn = True, partsGivenInWords = True):
        self.kwargs = {"diagramLabeled": True, "rounding": ["whole number", "tenth", "hundredth", "thousandth"], "pictureDrawn": True, "partsGivenInWords": True}
        self.toolTips = {
        "diagramLabeled": "Length of prism is labeled",            
        "rounding": {"whole number": "Whole Number", "tenth": "Tenth", "hundredth": "Hundredth", "thousandth": "Thousandth"}, 
        "pictureDrawn": "Picture is drawn", 
        "partsGivenInWords": "Parts described in question"}

        roundingChosen = random.choice(self.kwargs["rounding"])

        dimensions = [x for x in range(1,30)]
        length = random.choice([x for x in dimensions if x > 5])
        width = random.choice([x for x in dimensions if x < length - 5 or x > length + 5])
        height = random.choice([x for x in dimensions if x != length and x != width])
        shape = 'rectangular prism'

        volume = length * width * height
        roundingStrings = ['whole number', 'tenth', 'hundredth', 'thousandth']
        self.answer = round(volume, roundingStrings.index(rounding))

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


        if partsGivenInWords == True:
            self.question += 'the length is %g, the width is %g, and the height is %g, ' % (length, width, height)

        self.question += 'find the volume rounded to the nearest %s.' % (roundingChosen)



        if pictureDrawn == True:
            self.question = [{"text": self.question}, {"picture": {"rectangular prism": {"wholeFigureRotation": 0, "diagramLabeled": diagramLabeled, "height": height, "length": length, "width": width, "baseRotation": 0}}}]
       
