import sys
from fractions import Fraction
sys.path.insert(0, "F:/code/bielejec-sheets-be/creatingWorksheets/utils")
from equations import formatMathString, toLatexFraction, randomBetweenNot
import math
import string
import random

class _4():
  def __init__(self, difficulty=1):
    self.kwargs = {"difficulty":[1,2,3]}
    self.toolTips = {"difficulty": {1:"a(bx+c)=d", 2:"a(bx+c)=dx", 3:"a(bx+c)=d(ex+f)"}}
    """
    a(bx+c) = d diff1 -> abx + ac = d -> (d-ac)/(ab) = ans
    a(bx+c) = dx diff2 -> abx + ac = dx -> (ab-d)x = ac -> ac/(ab-d) = ans
    a(bx+c) = d(ex+f) diff3 -> abx + ac = dex + df -> (ab-de)x = (df-ac) -> (df-ac)/(ab-de) = ans
    """
    #x+a=b
    var = random.choice([letter for letter in string.ascii_lowercase if letter not in ["o","b","f","a","q","t","u","v","i","l","c"]])

    ans = random.choice([num for num in range(-10,11) if num != 0])

    if difficulty == 1:
        a = random.choice([num for num in range(-10,11) if num not in [0,1]])
        b = random.choice([num for num in range(-10,11) if num not in [0]])
        c = random.choice([num for num in range(-10,11) if num not in [0]])
        d = a*(b*ans+c)
        self.question = formatMathString(f"{a}({b}{var}+{c})={d}")
        self.answer = formatMathString(f"{var}={ans}")

    elif difficulty == 2:
        #abx+ac = dx, abx - dx = -ac, so define a,b,d,answer
        choices = []
        for ans in range(-10,11):
            for b in range(-10,11):
                for d in range(-10,11):
                    for a in range(-10,11):
                        for c in range(-10,11):
                            if b not in [0] and ans not in [0] and d not in [0] and a not in [0] and c not in [0] and a*b*ans+a*c == d*ans:
                                choices.append([a,b,d,ans,c])
        random.shuffle(choices)

        a = choices[0][0]
        b = choices[0][1]
        d = choices[0][2]
        ans = choices[0][3]
        c = choices[0][4]

        #product of abx-dx must equal -ac
        product = a*b*ans - d*ans
        c = int(product/-a)
        
        self.question = formatMathString(f"{a}({b}{var}+{c})={d}{var}")
        self.answer = formatMathString(f"{var}={ans}")

    elif difficulty == 3:
        #a(bx+c) = d(ex+f)
        a = random.choice([a for a in range(-10,11) if a not in [0,1]])
        b = random.choice([a for a in range(-10,11) if a not in [0]])
        c = random.choice([a for a in range(-10,11) if a not in [0]])
        d = random.choice([a for a in range(-10,11) if a not in [0,1]])
        e = random.choice([e for e in range(-20,21) if a not in [0] and a*b - d*e != 0])
        f = random.choice([f for f in range(-20,21) if a not in [0] and d*f - a*c != 0])

        #get x from this -> abx + ac = dex + df -> abx-dex = df-ac -> df-ac/ab-de
        ansNum = d*f-a*c
        ansDenom = a*b-d*e
        if ansNum % ansDenom == 0:
            self.answer = formatMathString(f"{var}={int(ansNum/ansDenom)}")
        else:

            if ansNum < 0 and ansDenom < 0:
                co = 1
            elif ansNum > 0 and ansDenom > 0:
                co = 1
            else:
                co = -1
            self.answer = formatMathString(fr"{var}=\frac{{{co*abs(ansNum)}}}{{{abs(ansDenom)}}}")
        self.question = formatMathString(f"{a}({b}{var}+{c})={d}({e}{var}+{f})")
    
    self.directions = f"Solve:"
