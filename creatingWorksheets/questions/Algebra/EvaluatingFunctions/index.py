from pylatex import (Document, TikZ, TikZNode, Plot,
                     TikZDraw, TikZCoordinate, Axis, Tabular,
                     TikZUserPath, TikZOptions, Center, VerticalSpace, NewLine, Math, Alignat, Section, NewLine)
from pylatex.utils import (NoEscape, bold)
import sys
sys.path.insert(0, "F:/code/bielejec-sheets-be/creatingWorksheets/utils")
from questionFormatting import multipleChoice, multipleChoicePic
from equations import formatMathString, randomBetweenNot
from docRelated import alignedEquations
from graphs import graphLinearFunction, shadeLinearInequality, axisOptions
import math, fractions, numpy, string, uuid, random

class EvaluatingFunctions():
  def __init__(self, typeOfFunction="linear"):
    self.kwargs = {"typeOfFucntion":["linear", "quadratic","cubic"]}

    functionVar = random.choice(["g","h","f"])

    a = randomBetweenNot(-10,10,[0])
    b = randomBetweenNot(-10,10,[0])
    c = randomBetweenNot(-10,10,[0])
    d = randomBetweenNot(-10,10,[0])

    x = random.randint(-10,10)
      
    if typeOfFunction == "linear":
      self.answer = f"{functionVar}({x})={a*x+b}"
      self.worksheetQuestion = f"{functionVar}(x)={a}x+{b}"
    elif typeOfFunction == "quadratic":
      self.answer = f"{functionVar}({x})={a*x**2+b*x+c}"
      self.worksheetQuestion = f"{functionVar}(x)={a}x^2+{b}x+{c}"
    elif typeOfFunction == "cubic":
      self.answer = f"{functionVar}({x})={a*x**3+b*x**2+c*x+d}"
      self.worksheetQuestion = f"{functionVar}(x)={a}x^3+{b}x^2+{c}x+{d}"
    
    self.answer = formatMathString(self.answer)
    self.worksheetAnswer = formatMathString(self.answer)
    self.worksheetQuestion += f"\n{functionVar}({x})=?"
    partsOfQuestion = self.worksheetQuestion.split("\n")
    self.worksheetQuestion = []
    for part in partsOfQuestion:
        self.worksheetQuestion.append({"center": True, "data": formatMathString(part)})

class EvaluatingFunctionsOperations():
  def __init__(self, operation="add", typeOfFunction1="linear", typeOfFunction2="quadratic"):
    self.kwargs = {"typeOfFunction1":["linear", "quadratic","cubic"],"typeOfFunction2":["linear", "quadratic","cubic"], "operation": ["add", "subtract", "multiply"]}

    function1Var = "f"
    function2Var = "g"

    answerValue = 0
    self.worksheetQuestion = ""
    x1 = random.randint(-10,10)
    x2 = random.randint(-10,10)

    for i, function in enumerate([typeOfFunction1, typeOfFunction2]):
        print(i, function)
        if i == 0:
            functionVar = function1Var
            x = x1
        else:
            functionVar = function2Var
            x = x2

        a = randomBetweenNot(-10,10,[0])
        b = randomBetweenNot(-10,10,[0])
        c = randomBetweenNot(-10,10,[0])
        d = randomBetweenNot(-10,10,[0])

        curAnswerVal = 0
        print(function)
        if function == "linear":
            print('insdie linear')
            curAnswerVal = a*x+b
            self.worksheetQuestion += f"{functionVar}(x)={a}x+{b}"
        elif function == "quadratic":
            print('insdie quadratic')
            curAnswerVal = a*x**2+b*x+c
            self.worksheetQuestion += f"{functionVar}(x)={a}x^2+{b}x+{c}"
        elif function == "cubic":
            print("inside cubic")
            curAnswerVal = a*x**3+b*x**2+c*x+d
            self.worksheetQuestion += f"{functionVar}(x)={a}x^3+{b}x^2+{c}x+{d}"

        if operation == "add":
            answerValue += curAnswerVal
        elif operation == "subtract":
            answerValue -= curAnswerVal
        elif operation == "multiply":
            if i == 0:
                answerValue = 1
            answerValue *= curAnswerVal
        self.worksheetQuestion += "\n"
    
    if operation == "add":
        self.worksheetQuestion += f"{function1Var}({x1})+{function2Var}({x2})="
    elif operation == "subtract":
        self.worksheetQuestion += f"{function1Var}({x1})-{function2Var}({x2})="
    elif operation == "multiply":
        self.worksheetQuestion += f"{function1Var}({x1}) \cdot {function2Var}({x2})="

    if operation == "add":
        self.answer = f"{function1Var}({x1})+{function2Var}({x2})= {answerValue}"
    elif operation == "subtract":
        self.answer = f"{function1Var}({x1})-{function2Var}({x2})= {answerValue}"
    elif operation == "multiply":
        self.answer = fr"{function1Var}({x1}) \bullet {function2Var}({x2})= {answerValue}"

    
    self.answer = formatMathString(self.answer)
    self.worksheetAnswer = formatMathString(self.answer)
    partsOfQuestion = self.worksheetQuestion.split("\n")
    self.worksheetQuestion = []
    for part in partsOfQuestion:
        self.worksheetQuestion.append({"center": True, "data": formatMathString(part)})

class CompositionsOfFunctions():
  def __init__(self, typeOfFunction1="linear", typeOfFunction2="quadratic"):
    self.kwargs = {"typeOfFunction1":["linear", "quadratic","cubic"],"typeOfFunction2":["linear", "quadratic","cubic"]}

    function1Var = "f"
    function2Var = "g"

    self.worksheetQuestion = ""
    x = random.randint(-5,5)
    originalX = x
    curAnswerVal = None
    for i, function in enumerate([typeOfFunction1, typeOfFunction2]):
        if i == 0:
            functionVar = function1Var
        else:
            functionVar = function2Var
            
        a = randomBetweenNot(-5,5,[0])
        b = randomBetweenNot(-5,5,[0])
        c = randomBetweenNot(-5,5,[0])
        d = randomBetweenNot(-5,5,[0])

        if function == "linear":
            curAnswerVal = a*x+b
            self.worksheetQuestion += f"{functionVar}(x)={a}x+{b}"
        elif function == "quadratic":
            curAnswerVal = a*x**2+b*x+c
            self.worksheetQuestion += f"{functionVar}(x)={a}x^2+{b}x+{c}"
        elif function == "cubic":
            curAnswerVal = a*x**3+b*x**2+c*x+d
            self.worksheetQuestion += f"{functionVar}(x)={a}x^3+{b}x^2+{c}x+{d}"
        x = curAnswerVal
        self.worksheetQuestion += "\n"
    
    self.worksheetQuestion += f"{function1Var}({function2Var}({originalX}))="
    self.answer = f"{function1Var}({function2Var}({originalX}))={curAnswerVal}"

    self.answer = formatMathString(self.answer)
    self.worksheetAnswer = formatMathString(self.answer)
    partsOfQuestion = self.worksheetQuestion.split("\n")
    self.worksheetQuestion = []
    for part in partsOfQuestion:
        self.worksheetQuestion.append({"center": True, "data": formatMathString(part)})

evaluatingFunctionsQuestionsDict = {"EvaluatingFunctions": EvaluatingFunctions, "EvaluatingFunctionsOperations": EvaluatingFunctionsOperations, "CompositionsOfFunctions": CompositionsOfFunctions}
