from pylatex import (Alignat, NoEscape)

def alignedEquations(data, explanation = "", doc = None):
    """
    data: [[numberOfColumns, first equation, *optional: second equation]]
    """
    #Creates a subsection
    #Creates an aligned environment
    for item in data:
        aligns = item[0]
        equation = item[1]

        if len(item) > 2:
            step = item[2]
        else:
            step = False

        with doc.create(Alignat(aligns=aligns, numbering=False, escape=False)) as agn:
            agn.append(rf"{equation} \\")
            if step:
                agn.append(rf"{step}")
    doc.append(NoEscape(explanation))