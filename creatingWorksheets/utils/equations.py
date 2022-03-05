import re, string, random
from fractions import Fraction


def formatEquation(data):
    #this is also useful to add a list of different parts rather than concatenate them
    string = ""
    for item in data:
        string += item
    
    #find the first && sign, remove one &
    string = string.replace("&&", "&", 1)
    return string

def randomBetweenNot(minNum, maxNum, notList=[]):
  return random.choice([x for x in range(minNum, maxNum+1) if x not in notList])
  
def toLatexFraction(numerator, denominator, simplified = True):
    if simplified:
      newFraction = Fraction(numerator, denominator)
      numerator = newFraction.numerator
      denominator = newFraction.denominator
    

    if denominator == 1:
        return f"{numerator}"
    elif numerator < 0:
        return fr"-1\frac{{{abs(numerator)}}}{{{denominator}}}"
    else:
        return fr"\frac{{{numerator}}}{{{denominator}}}"

def RepresentsInt(s):
  try: 
    int(s)
    return True
  except ValueError:
    return False

def getFactorPairs(val):
  return [(i, int(val / i)) for i in range(1, int(val**0.5)+1) if val % i == 0]

#Runs loop twice to account for --1x situations which resolve to +1x which resolve to x
def formatMathString(givenString):
  """
  +- > -

  endings = [+,-,),}]
  if -1 or +1 then an ending, keep as -1 and +1
  else: we do - and +

  if start of expression or =, then 1 then 

  """
  def format(givenString):
    newString = ""
    i = 0
    while i < len(givenString):
      char = None
      nextChar = None
      nextNextChar = None

      if i <= len(givenString)-1:
        char = givenString[i]
      if i+1 <= len(givenString)-1:
        nextChar = givenString[i+1]
      if i+2 <= len(givenString)-1:
        nextNextChar = givenString[i+2]

      endings = ["=", ")", "+", "}","-"]
      beginningTags = ["(", "\\","{"] + [x for x in string.ascii_letters]

      #+1 and with a proper ending
      #Change + - to just one -
      if char == "+" and nextChar == "-":
        newString += nextChar
        i += 2
      #Change - - to +
      elif char == "-" and nextChar == "-":
        newString += "+"
        i += 2
      #Beginning or after = followed by a 1 with following characters in endings
      elif (i == 0 or givenString[i-1] == "=") and char == "1" and nextChar in endings:
        newString += char + nextChar
        i += 2
      #Beginning or after = followed by (, \, or a letter
      elif (i == 0 or givenString[i-1] == "=") and char == "1" and nextChar in beginningTags:
        #check for \pm
        if givenString[i+1:i+4] == "\\pm":
          newString += char
          i += 1
        else:
          #skip the 1
          newString += nextChar
          i += 2
      #-+ 1 
      elif (char == "-" or char == "+") and nextChar == "1":
        #-+ 1, then ending -> -+ 1
        if nextNextChar in endings or i+1 == len(givenString)-1:
          newString += char + nextChar
          i += 2
        #-+ 1, then beginningTag -> -+  
        elif nextNextChar in beginningTags:
          if givenString[i+2:i+5] == "\\pm":
            newString += char
            i += 1
          else:
            newString += char
            i += 2
        #may be a number
        else:
          newString += char 
          i += 1
      else:
        newString += char
        i += 1 
    print(newString)
    for letter in [x for x in string.ascii_letters]:
      newString = re.sub(rf"$1{letter}",letter, newString)
      
      newString = re.sub(rf"\(1{letter}",f"({letter}", newString)
      
      newString = re.sub(rf"=1{letter}",f"={letter}", newString)

      newString = re.sub(r"{1%s" % letter, f"{letter}", newString)

      newString = re.sub(rf"{letter}\^1", f"{letter}", newString)
      newString = newString.replace("%s^{1}" % letter, "%s" % letter )

    return newString

  givenString = format(givenString)
  newString = format(givenString)

  #we only need to include $ if there are any 
  return f"${newString}$"    

def randomBetweenNot(minNum, maxNum, notList=[]):
  return random.choice([num for num in range(minNum,maxNum+1) if num not in notList])

def getPrimes(max = 10):
	n = max
	numbers = set(range(n, 1, -1))
	primes = []
	while numbers:
		p = numbers.pop()
		primes.append(p)
		numbers.difference_update(set(range(p*2, n+1, p)))
	return primes