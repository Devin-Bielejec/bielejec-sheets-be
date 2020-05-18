def formatEquation(data):
    #this is also useful to add a list of different parts rather than concatenate them
    string = ""
    for item in data:
        string += item
    
    return string
 
def formatExpression(data):
    #data comes in as an array of tuples [(coeffecient, term as string without coefficient)], such as [(4,"x^2")]
    string = ""
    startingIndex = 0

    #For aligned - we need the first term to have & infront and && for all preceding
    for i, pair in enumerate(data):
        if pair[0] == "&" or pair[0] == "&&":
            align = pair[0]
            coVal = pair[1]
            term = pair[2]
        else:
            align = ""
            coVal = pair[0]
            term = pair[1]

        currentString = align
        
        if coVal < -1:
            currentString += f"{coVal}{term}"
        elif coVal == -1:
            currentString += f"-{term}"
        elif coVal == 0:
            #if first term is 0, we want to treat the second term as the first term
            currentString += f""
            if i == startingIndex:
              startingIndex += 1
        elif coVal == 1:
            if startingIndex == i:
              currentString += f"{term}"
            else:
              currentString += f"+{term}"
        elif coVal > 1:
            if i == startingIndex:            
                currentString += f"{coVal}{term}"
            else:
                currentString += f"+{coVal}{term}"
        else:
            print("coVal is not an integer!")

        string += currentString 
    print(string)
    return string