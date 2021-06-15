import sys, importlib, json, inspect, random

sys.path.append('../')
from questions.Algebra.Quadratics import quadraticsQuestionsDict
from questions.Algebra.SolvingEquations import solvingEquationsQuestionsDict
from questions.Algebra.SystemsOfEquations import systemsOfEquationsQuestionsDict
from questions.Algebra.MultiplyingPolynomials import multiplyingPolynomialsQuestionsDict
from questions.Algebra.EvaluatingFunctions import evaluatingFunctionsQuestionsDict
from questions.Algebra.FactoringTrinomials import factoringTrinomialsQuestionsDict
from questions.Algebra.SquareRootSolving import squareRootSolvingQuestionsDict
from questions.Algebra.QuadraticFormula import quadraticFormulaQuestionsDict
from questions.Algebra.AbsoluteValue import absoluteValueQuestionsDict
from questions.Algebra.RadicalEquations import radicalEquationsQuestionsDict
from questions.Algebra.ReduceAlgebraicFractions import reduceAlgebraicFractionsQuestionsDict
from questions.Algebra.FactorByGrouping import factorByGroupingQuestionsDict

from documentCreation import createVersions

def updateQuestionsDict(questionsDict, newDict):
    questionsDict = {**questionsDict, **newDict}
    return questionsDict


questionsDict = {}
# questionsDict = updateQuestionsDict(questionsDict, quadraticsQuestionsDict)
questionsDict = updateQuestionsDict(questionsDict, factorByGroupingQuestionsDict)

print(questionsDict)
#Stuff above is to access the questions

#get questions for sys argv - for real
# documentOptions = json.loads(sys.argv[1])

#WILL BE REPLACED BY THE IDS AND DOCUMENT OPTIONS COMING FROM JS BACKEND

q = []
k = []

for x in range(15):
    q.append("FactorByGrouping")
    k.append({})

#Testing BELOW
documentOptions = {"ids": q, "kwargs": k, "nameOfDoc": "Week14.Lesson1-FactorByGrouping", "spacingBetween": ".5in", "font":"Huge"}
#WILL BE REPLACED BY THE IDS AND DOCUMENT OPTIONS COMING FROM JS BACKEND


questions = []

createVersions(documentOptions, worksheet = True, collatedAnswerKey = False, columns = 1, numberOfVersions = 1, questionsDict=questionsDict)
