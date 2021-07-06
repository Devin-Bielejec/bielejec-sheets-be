import random

class _6():
    def __init__(self, pictureDrawn = True):
        self.kwargs = {"pictureDrawn": True}
        self.toolTips = {
        "pictureDrawn": "Picture is drawn", 
        }

        dimensions = [x for x in range(1,30)]
        length = random.choice([x for x in dimensions if x > 5 and x < 24])
        width = random.choice([x for x in dimensions if x > length + 5])
        height = random.choice([x for x in dimensions if x != length and x != width])
        shape = 'rectangular prism'

        volume = length * width * height
        roundingStrings = ['whole number', 'tenth', 'hundredth', 'thousandth']
        roundingChosen = random.choice(roundingStrings)

        self.answer = round(volume, roundingStrings.index(roundingChosen))

        self.question = ""

        if not pictureDrawn:
            self.question = 'Given a %s, ' % shape
            self.question += f'with a length of{length}, width of {width}, and the height of {height}, '
            self.question += rf'find the volume rounded to the nearest \textit{{{roundingChosen}}}.'
        else:
            self.question = fr"round to the nearest \textit{{{roundingChosen}}}"
        
        if pictureDrawn == True:
            self.question = [{"text": self.question}, {"picture": {"rectangular prism": {"wholeFigureRotation": 0, "diagramLabeled": True, "height": height, "length": length, "width": width, "baseRotation": 0}}}]
        self.directions = "Find the volume:"
