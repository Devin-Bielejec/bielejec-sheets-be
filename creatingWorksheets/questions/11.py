import sys
from fractions import Fraction
sys.path.insert(0, "./creatingWorksheets/utils")
from equations import formatMathString, toLatexFraction, randomBetweenNot
import math
import string
import random

def zeroesCheck(matrix, indices):
  product = 1
  for (r,row) in enumerate(matrix):
    if r in indices:
      for col in row:
        product *= col
  
  return product == 0

def createMatrix(variables=2,typeOfSolution="unique"):
  #Type Of typeOfSolution - unique, infinite, infinite same equations, none
  matrix = []

  if variables == 2 and typeOfSolution == "infinite":
    typeOfSolution = "infinite same equations"
  for ri in range(variables):
    col = [0 for item in range(variables+1)]
    col[ri] = 1
    #last value
    col[variables] = random.randint(-10,10)
    if typeOfSolution == "none" or typeOfSolution == "infinite":
      #Make all values besides last value 0 and make last value not 0
      if ri == variables-1:
        col[ri] = 0
        if typeOfSolution == "none":
          col[variables] = random.choice([x for x in range(-10,11) if x != 0])
        else:
          col[variables] = 0
      elif ri == variables - 2:
        col[ri] = 1
        col[ri+1] = 1
    elif typeOfSolution == "infinite same equations":
      if ri == 0:
        #Make all the equations the same thus first row all 1's
        col = [random.choice([-1,1])*random.randint(1,5) for item in range(variables+1)]
        col[variables] = random.randint(-10,10)
      else:
        col = [0 for item in range(variables+1)]
    
    matrix.append(col)

  answers = [x[variables] for x in matrix]

  while zeroesCheck(matrix,[x for x in range(len(matrix[0]))]):
    #Loop through each row
    for (originalIndex, row) in enumerate(matrix):
      #Loop through each row again
      for (newIndex, row2) in enumerate(matrix):
          scalar = random.choice([-1,1])*random.randint(2,3)
          #mult by int and add to every other row
          #When we're not on duplicate rows and zeroes still present
          if originalIndex is not newIndex and zeroesCheck(matrix,[newIndex]) is True:
            for scalar in [-3,-2,-1,1,2,3]:
              #Find max value
              maxVal = -2000
              for (colIndex, col) in enumerate(row):
                testVal = col * scalar + row2[colIndex]
                if testVal > maxVal:
                  maxVal = testVal
              if maxVal < 10 and maxVal > -2000:
                for (colIndex, col) in enumerate(row):
                  row2[colIndex] = col * scalar + row2[colIndex]
                break

       
      
  return matrix, answers

#System of 2x2 equations with finite solutions
class _11():
  def __init__(self, variables=2, typeOfSolution="unique"):
    self.kwargs = {"variables":[2,3,4], "typeOfSolution": ["unique", "infinite", "infinite same equations", "none"]}
    self.toolTips = {"variables": "Number of Variables", "typeOfSolution": "Type of Solution"}
    
    v1 = "x"
    v2 = "y"
    v3 = "z"
    v4 = "a"
    v5 = "b"
    variableLetters = ["x", "y", "z", "a", "b", "c", "d", "e", "f","g"]
    
    matrix, answers = createMatrix(variables=variables, typeOfSolution=typeOfSolution)

    self.question = ""
    #Loop through each row
    for (ri,row) in enumerate(matrix):
        #Loop through each column
        for (ci, col) in enumerate(row):
            #Add each value of equation before the =
            if ci != len(row) - 1:
              if ci != 0:
                  self.question += f"+{col}{variableLetters[ci]}"
              else:
                  self.question += f"{col}{variableLetters[ci]}"
            else:
              self.question += f"=${col}"
              self.question += "\n"
    self.answer = ""
    for (ai,ans) in enumerate(answers):
        if ai == len(answers)-1:
            self.answer += f"{variableLetters[ai]}={answers[ai]}"
        else:
            self.answer += f"{variableLetters[ai]}={answers[ai]}, "
    self.answer = formatMathString(self.answer)

    self.directions = "Solve the system for each variable: "

    #Take the worksheetQuestions and put them into a list form
    partsOfQuestion = self.question.split("\n")

    self.duplicateCheck = ""
    #Center environment but aligned equations by =
    self.question = [{"text": {"center-aligned": []}}]
    for part in partsOfQuestion:
        self.question[0]["text"]["center-aligned"].append(formatMathString(part))
        self.duplicateCheck += formatMathString(part)