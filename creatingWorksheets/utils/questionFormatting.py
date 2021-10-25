import random
from pylatex.utils import NoEscape
from pylatex.position import Center
from pylatex import VerticalSpace, NewLine, TikZ, TikZOptions, MiniPage, LineBreak

"""
Use Alignat to make multiple choice aligned 4 rows, or 2 rows based on number of characters in choices etc
"""


#Always make first choice correct answer
def multipleChoice(choices = ['1','2','3','4','5'], fifthVariation = False, doc = None, spacing = "normal"):
    correctAnswer = choices[0]

    if len(choices) != len(set(choices)):
        print(choices)
        return "ERROR"

    #All choices will be shuffled - not numerical
    random.shuffle(choices)
    doc.append(NewLine())
    
    #check if any of the choices contain fractions
    additionalSpace = False
    for i in choices:
        if r"\frac" in i:
            additionalSpace = True

    for i in range(len(choices)):
        doc.append(NoEscape(f'({str(i+1)}) {choices[i]}'))

        if additionalSpace and spacing == "normal":
            doc.append(VerticalSpace('.05in'))
        doc.append(NewLine())

    if fifthVariation == True:
        doc.append(NoEscape(r'(%d) I do not know. (Worth $\frac{1}{3}$ points)' % (len(choices)+1)))

    #for space between questions
    doc.append(NewLine())

    #Retrun correct answer
    for choice in choices:
        if choice == correctAnswer:
            return choices.index(choice) + 1

def multipleChoicePic(choices = ['1','2','3','4','5'], fifthVariation = False, math = True, doc = None):
    print(choices)
    #choices will be functions
    correctAnswer = choices[0]

    #All choices will be shuffled - not numerical
    random.shuffle(choices)
    doc.append(NewLine())

    #Assuming that with pictures, we'll want a 2x2 grid
    for i in range(len(choices)):
        with doc.create(MiniPage(width=r"0.5\textwidth", align="c")):
            choices[i](doc = doc)
            doc.append(NewLine())
            with doc.create(Center()) as center:
                center.append(NoEscape(f"({i+1})"))
        
        if (i % 2) == 1:
            doc.append(VerticalSpace("20pt"))
            doc.append(LineBreak())
    if fifthVariation == True:
        doc.append(NoEscape(r'(%d) I do not know. (Worth $\frac{1}{3}$ points)' % (len(choices)+1)))

    #for space between questions
    doc.append(NewLine())

    #Retrun correct answer
    for choice in choices:
        if choice == correctAnswer:
            return choices.index(choice) + 1