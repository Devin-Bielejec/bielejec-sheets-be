import random

class _7():
    def __init__(self, wholeFigureRotation = 0):
        self.kwargs = {"wholeFigureRotation": [None,0,45,90,135,180]}
        self.toolTips = {
        "pictureDrawn": "Picture is drawn", "wholeFigureRotation": "Degrees Rotated"}

        if wholeFigureRotation is not None:
            pictureDrawn = True
        else:
            pictureDrawn = False

        dimensions = [x for x in range(1,30)]
        length = random.choice([x for x in dimensions if x > 5])
        width = length

        #Will make a nice looking pyramid
        height = int(random.choice([x/10 for x in range(11,19)])*length)
        shape = 'regular square pyramid'

        volume = length * width * height * 1/3
        roundingStrings = ['whole number', 'tenth', 'hundredth', 'thousandth']
        roundingChosen = random.choice(roundingStrings)

        self.answer = round(volume, roundingStrings.index(roundingChosen))

        self.question = ""

        if not pictureDrawn:
            self.question = 'Given a %s, ' % shape
            self.question += 'the side of the base is %g and the height is %g, ' % (width, height)
            self.question += rf'find the volume rounded to the nearest  \textit{{{roundingChosen}}}.'
        else:
            self.question = rf"round to the nearest \textit{{{roundingChosen}}}"

        self.directions = "Find the volume:"
        self.duplicateCheck = f"pyramidwidth{width}height{height}length{length}"
        if pictureDrawn == True:
            self.question = [{"text": self.question}, {"picture": {"regular square pyramid": {"wholeFigureRotation": wholeFigureRotation, "diagramLabeled": True, "height": height, "sideValue": length, "baseRotation": 0}}}]
       
