from pylatex import (TikZNode, TikZDraw, TikZCoordinate, TikZOptions, TikZUserPath, Plot)

def axisOptions(xmin=-5, xmax=5, ymin=-5, ymax=5):
     #start axis for grid
    xmin = -5
    xmax = 5
    ymin = -5
    ymax = 5

    kwargs = {
        "grid":"both",
        "xmin":f"{xmin}",
        "xmax":f"{xmax}",
        "ymin":f"{ymin}",
        "ymax":f"{ymax}",
        "xticklabel":"\empty",
        "yticklabel":"\empty",
        "minor x tick num":"1",
        "minor y tick num":"1",
        "axis lines":"middle",
        "xlabel":"$x$",
        "ylabel":"$y$",
        "axis line style":"latex-latex",
        "label style":"{at={(ticklabel cs:1.1)}}"}
        
    axisOptions1 = TikZOptions(
        "axis equal image", 
        **kwargs)

    return axisOptions1

def graphLinearFunction(xmin=-5, xmax=5, ymin=-5, ymax=5, slope=1, yIntercept=1, dashed = False, axis = None):
    #Find domain range, y=mx+b --> (y-b)/m
    rangeY = [y for y in range(ymin, ymax+1)]
    domainX = [(y-yIntercept)/slope for y in rangeY if xmin <= (y-yIntercept)/slope <= xmax]
    
    functionEquation = f"{slope}*x+{yIntercept}"
    if dashed:
        dashed = "dashed"
    else:
        dashed = ""
    functionOptions = TikZOptions("<->", f"{dashed}", "smooth", "thick", **{"mark":"none", "domain":f"{domainX[0]}:{domainX[-1]}"})
    axis.append(Plot(options=functionOptions, func=f"{functionEquation}"))

def shadeLinearInequality(xmin=-5, xmax=5, ymin=-5, ymax=5, slope=1, yIntercept=1, greaterThan = False, axis = None): 
    #inequality shading

    #we'll start with the lines we want to make, so every 1/3 of the line going to the edge of the graph
    #we have two ways we could go, so find both points, check which one is valid, then we know which way for the rest
    #we test towards xmin OR xmax
    #step is considered 1111/10,0000
    step = 1111
    #points on exisiting line
    shadingX1 = [x/10000 for x in range(xmin*10000, (xmax+1)*10000, step)]
    shadingY1 = [slope*x+yIntercept for x in shadingX1]

    #Checking if we should go towards xmin or xmax (will add special cases for horizontal/vertical lines)
    testY2 = 1/slope * (shadingX1[1] - xmin) + shadingY1[1]
    if greaterThan:
        if testY2 > slope * xmin + yIntercept:
            shadingX2 = xmin
        else:
            shadingX2 = xmax
    else:
        if testY2 < slope * xmin + yIntercept:
            shadingX2 = xmin
        else:
            shadingX2 = xmax
    #(y1 - y2) = m(x1 - x2)
    #-y2 = m(x1-x2)-y1
    #y2 = -m(x1-x2)+y1
    #So if we do opposite reciprocal, we get y2 = m(x1-x2) + y1

    for x1, y1 in zip(shadingX1, shadingY1):
        x2 = shadingX2
        y2 = 1/slope*(x1-x2)+y1
        axis.append(Plot(coordinates=[(x1,y1), (x2,y2)], options=TikZOptions("smooth", **{"mark":"none"})))
