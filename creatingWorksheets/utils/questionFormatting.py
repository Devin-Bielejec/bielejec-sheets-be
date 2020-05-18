import random
from pylatex.utils import NoEscape
from pylatex import VerticalSpace, NewLine

"""
Use Alignat to make multiple choice aligned 4 rows, or 2 rows based on number of characters in choices etc
"""


#Always make first choice correct answer
def multipleChoice(choices = ['1','2','3','4','5'], fifthVariation = False, doc = None):
    correctAnswer = choices[0]

    if len(choices) != len(set(choices)):
        return "ERROR"

    #All choices will be shuffled - not numerical
    random.shuffle(choices)

    for i in range(len(choices)):
        doc.append(NoEscape('(%s) ' % str(i+1) + choices[i]))
        if i == 0:
            doc.append(VerticalSpace('.05in'))

        if i != 3:
            doc.append(NewLine())
            doc.append(VerticalSpace('.05in'))

    if fifthVariation == True:
        doc.append(NoEscape(r'(%d) I do not know. (Worth $\frac{1}{3}$ points)' % (len(choices)+1)))

    #Retrun correct answer
    for choice in choices:
        if choice == correctAnswer:
            return choices.index(choice) + 1