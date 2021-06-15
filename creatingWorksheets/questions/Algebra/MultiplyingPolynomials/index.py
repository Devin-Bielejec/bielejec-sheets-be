import sys
from fractions import gcd, Fraction
sys.path.insert(0, "F:/code/bielejec-sheets-be/creatingWorksheets/utils")
from equations import formatMathString, toLatexFraction, randomBetweenNot
import math, random, re



class MultiplyingPolynomials():
  def __init__(self, firstPolynomialDegree=1, secondPolynomialDegree=1, highestExponent=1):
    self.kwargs = {"firstPolynomialDegree":[1,2,3,4,5,6,7,8,9,10], "secondPolynomialDegree": [1,2,3,4,5,6,7,8,9,10], "highestExponent": [1,2,3,4,5,6,7,8,9,10]}

    if firstPolynomialDegree > highestExponent:
      highestExponent = firstPolynomialDegree
    if secondPolynomialDegree > highestExponent:
      highestExponent = secondPolynomialDegree

    #c bx ax^2
    firstDict = {}
    secondDict = {}
    firstExpHash = {}
    secondExpHash = {}
    for f in range(firstPolynomialDegree):
      curExp = random.choice([x for x in range(1,highestExponent+1) if str(x) not in firstExpHash])
      firstExpHash[str(curExp)] = True
      firstDict[str(f)] = {"co": randomBetweenNot(-10,10,[0]), "exp": curExp}
    for s in range(secondPolynomialDegree):
      curExp = random.choice([x for x in range(1,highestExponent+1) if str(x) not in secondExpHash])
      secondExpHash[str(curExp)] = True
      secondDict[str(s)] = {"co": randomBetweenNot(-10,10,[0]), "exp": curExp}

    firstList = [firstDict[str(key)] for key in range(firstPolynomialDegree)]
    secondList = [secondDict[str(key)] for key in range(secondPolynomialDegree)]

    random.shuffle(firstList)
    random.shuffle(secondList)
    #Now loop through first and second list
    #firstList = [{co: 1, exp: etc}]
    self.worksheetQuestion = ""
    
    expression = ""
    for li in [firstList, secondList]: 
      expression += "("
      for item in li:
        expression += str(item["co"])
        if item["exp"] > 0:
          if item["exp"] == 1:
            expression += "x"
          else:
            expression += f"x^{{{item['exp']}}}"
        if li.index(item) != len(li) - 1:
          expression += "+"
    
      expression += ")"
    
    self.worksheetQuestion = expression

    #Get Answer - answer is list pertaining to value of exponent
    #{0: 1, 1: 2, 2: 3} = 1 + 2x + 3x^2
    answer = {}

    for i in firstList:
      for j in secondList:
        #Distributing and putting reults in answer dictionary
        constant = i["co"] * j["co"]
        exp = i["exp"] + j["exp"]

        if f"{exp}" in answer:
          answer[f"{exp}"] += constant
        else:
          answer[f"{exp}"] = constant
    
    keys = list(answer.keys())

    self.answer = ""

    keys.sort(reverse=True)
    
    for e in keys:
      if e == "0":
        self.answer += f"{answer[e]}"
      elif e == "1":
        self.answer += f"{answer[e]}x"
      else:
        self.answer += f"{answer[e]}x^{{{e}}}"
      
      if keys.index(e) != len(keys) - 1:
        self.answer += "+"

    self.worksheetAnswer = formatMathString(self.answer)
    self.answer = formatMathString(self.answer)
    #Take the worksheetQuestions and put them into a list form
    self.worksheetQuestion = formatMathString(self.worksheetQuestion)

    print(self.worksheetAnswer)
    print(self.worksheetQuestion)

multiplyingPolynomialsQuestionsDict = {"MultiplyingPolynomials": MultiplyingPolynomials}
