from pylatex import Document, MiniPage, LineBreak, VerticalSpace, Figure, HorizontalSpace, NewLine, Command
from pylatex import (Document, TikZ, TikZNode,
                     TikZDraw, TikZCoordinate,
                     TikZUserPath, TikZOptions)

def generate_labels():
    geometry_options = {"margin": "0.5in"}
    doc = Document(geometry_options=geometry_options)

    doc.change_document_style("empty")
    
    #8.5 - 2 margins = 7.5 /2 = 3.25
    columns = 3

    for i in range(100):
        if i == 0:
            doc.append(Command("noindent"))
        with doc.create(MiniPage(width=fr"{1/columns}\textwidth")):
            doc.append(f"({i+1}) Vladimir Gorovikov")
            doc.append("\n")
            doc.append(f"is so")
            doc.append("\n")
            doc.append(f"is cool")
            doc.append("\n")
        
        # if (i+1) % 2 != 0:
        #     doc.append(HorizontalSpace(".2in"))
        if (i+1) % columns == 0:
            doc.append(NewLine())

    doc.generate_pdf("minipage", clean_tex=False)


generate_labels()