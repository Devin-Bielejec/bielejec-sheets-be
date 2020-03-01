from pylatex import Document, Section, Subsection, Command
from pylatex.utils import italic, NoEscape
import sys


def fill_document(doc):
    """Add a section, a subsection and some text to the document.

    :param doc: the document
    :type doc: :class:`pylatex.document.Document` instance
    """
    with doc.create(Section('A section')):
        doc.append('Some regular text and some ')
        doc.append(italic('italic text. '))

        with doc.create(Subsection('A subsection')):
            doc.append('Also some crazy characters: $&#{}')


if __name__ == '__main__':
    print("in this python file")
    name_of_doc = sys.argv[1]
    # Document with `\maketitle` command activated
    doc = Document()

    doc.preamble.append(Command('title', 'Awesome Title'))
    doc.preamble.append(Command('author', 'Anonymous author'))
    doc.preamble.append(Command('date', NoEscape(r'\today')))
    doc.append(NoEscape(r'\maketitle'))

    fill_document(doc)

    doc.generate_pdf(f'./images/{name_of_doc}')

    from pdf2image import convert_from_path
    pages = convert_from_path(f"./images/{name_of_doc}.pdf", 500)
    for page in pages:
        page.save(f"./images/{name_of_doc}.jpg", "JPEG")




