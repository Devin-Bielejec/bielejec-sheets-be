import sys
from fractions import Fraction
sys.path.insert(0, "./creatingWorksheets/utils")
from utils.equations import formatMathString, toLatexFraction, randomBetweenNot
from utils.shapes import triangleCoordinates
from utils.pdfFunctions import annotatePolygon
from utils.transformations import rotation
import math
import string
import random

#multiplying terms
class _18():
    def __init__(self, simplifyFraction=False,coefficients=True, multiVariables=True,someExponentIsOne=True):
        """
        coeffecients-bool
        multivariables-bool
        someExponentIsOne-bool
        """
        self.kwargs = {
            "coefficients": True,
            "multiVariables": True,
            "someExponentIsOne": True,
            "simplifyFraction": False
        }

        self.toolTips = {
            "coefficients": "There will be coeffecients in front of the terms",
            "multiVariables": "Some terms will have multiple variables",
            "someExponentIsOne": "There will be an exponent of 1",
            "simplifyFraction": "Numerator coefficient will not divide nicely with denominator"
        }

        #coA var1A var2A var3A and each var1AExp etc
        #coB var1B var2B var3B
        if not simplifyFraction:
            coB = randomBetweenNot(-3,3, [0])
            coA = coB * randomBetweenNot(-5,5,[0])
        else:
            factor = random.randint(2,5)
            coA = randomBetweenNot(-12,12,[-1,0,1]) * factor
            coB = randomBetweenNot(-12,12, [x for x in range(-12,13) if math.gcd(coA,x) == 1 or math.gcd(coA,x) == -1])
            
        #Create variables and shuffle
        variables = list(string.ascii_lowercase)
        random.shuffle(variables)

        #Create exponents randomly
        variablesExponents = [random.randint(1,10) for x in range(9)]
        if someExponentIsOne:
            variablesExponents[0] = 1
        else:
            for (index,item) in enumerate(variablesExponents):
                if item == 1:
                    variablesExponents[index] = item + 1
        
        var1A, var2A, var3A = variables[0:3]
        var1B, var2B, var3B = variables[0:3]

        var1AExp, var2AExp, var3AExp, var1BExp, var2BExp, var3BExp = variablesExponents[0:6]

        questionStringA = ""
        questionStringB = ""
        if coefficients:
            questionStringA += f"{coA}"
            questionStringB += f"{coB}"
            answerCo = coA * coB
        else:
            answerCo = 1
        
        if multiVariables:
            numVarsA = random.randint(1,3)
            numVarsB = random.randint(2,3)
        else:
            numVarsA = 1
            numVarsB = 1
        forStringA = [[var1A, var1AExp], [var2A, var2AExp], [var3A, var3AExp]]
        forStringB = [[var1B, var1BExp], [var2B, var2BExp], [var3B, var3BExp]]

        answer = []
        for index in range(numVarsA):
            curVar = forStringA[index][0]
            curVarExp = forStringA[index][1]
            if curVarExp != 1:
                questionStringA += f"{curVar}^{{{curVarExp}}}"
            else:
                questionStringA += f"{curVar}"

            answer.append([curVar, curVarExp])
        for index in range(numVarsB):
            curVar = forStringB[index][0]
            curVarExp = forStringB[index][1]
            if curVarExp != 1:
                questionStringB += f"{curVar}^{{{curVarExp}}}"
            else:
                questionStringB += f"{curVar}"

            #check if answer has same variable
            foundVar = False
            for (indexAnswer,item) in enumerate(answer):
                curAnswerVar = item[0]
                curAnswerVarExp = item[1]
                if curAnswerVar == curVar:
                    answer[indexAnswer][1] = curAnswerVarExp + curVarExp
                    foundVar = True
            if not foundVar:
                #add var to answer
                answer.append([forStringB[index][0], forStringB[index][1]])

        questionString = questionStringA + " \cdot " + questionStringB
        questionString = formatMathString(questionString)
        self.directions = "Multiply the terms:"

        self.question = [{"text": questionString}]

        self.duplicateCheck = f"{var1A}{var1AExp}{var2A}{var2AExp}{var3A}{var3AExp}{var1B}{var1BExp}{var2B}{var2BExp}{var3B}{var3BExp}"

        #sort variables
        sortedAnswerVars = sorted(answer, key=lambda tup: tup[0])

        answerString = f"{answerCo}"
        for item in sortedAnswerVars:
            curVar = item[0]
            curVarExp = item[1]
            if curVarExp != 1:
                answerString += f"{curVar}^{{{curVarExp}}}"
            else:
                answerString += f"{curVar}"
        answerString = formatMathString(answerString)
        self.answer = [{"text": answerString}]
		
        

