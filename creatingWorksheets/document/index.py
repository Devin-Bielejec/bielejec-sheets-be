"""
document creation of the actual pdf
-takes in different options
-takes in all the classes of questions created
-halfsheet/quarter sheet etc
-snippets to store on FE / firebase
-automatic process from finishing a question -> uploading info to datase, snippet to image datebase, etc
"""

"""
Options:
1) name
2) questions [(classID, kwargs), etc] -> look up class for instance inside of dictionary

don't worry about right now
spacebetween questions -> chose a default
question order
columns
font
pageNumbers
answers
versions
collation
double sided
reference sheet
halfsheet/quarter sheet
"""
#https://jeltef.github.io/PyLaTeX/current/pylatex/pylatex.document.html
def createDocument(nameOfDoc = 'default', font = 'normalsize', pageNumbers = True, spaceBetween = 'noraml', spaceBetweenMC = 'normal', spaceBetweenSA = 'normal', standalone = False):
	
	if standalone == False:
		#Can make rmargin bigger for more work etc usually for MC to provide a column of work
		geometry_options = {"top": "1in", "lmargin": ".5in", "rmargin": ".5in"}
		doc = Document(documentclass='article', document_options = 'twoside', geometry_options = geometry_options, indent=False, font_size=font, page_numbers=pageNumbers)


	# float separation, does something important
	doc.append(Command('setlength{\\floatsep}{1.0pt plus 5.0pt minus 2.0pt}'))
	doc.append(Command('setlength{\\intextsep}{1.0pt plus 5.0pt minus 2.0pt}'))
	doc.append(Command('setlength{\\textfloatsep}{1.0pt plus 5.0pt minus 2.0pt}'))
	doc.append(Command('setcounter{topnumber}{10}'))
	doc.append(Command('setcounter{bottomnumber}{10}'))
	doc.append(Command('setcounter{totalnumber}{10}'))

	# makes float appear at top of page at the last page
	doc.append(Command('makeatletter'))
	doc.append(Command('setlength{\\@fptop}{0pt}'))
	doc.append(Command('setlength{\\@fpbot}{0pt plus 1fil}'))
	doc.append(Command('makeatother'))

	doc.packages.append(Package('subfig'))
	doc.append(Command('usetikzlibrary{calc}'))
	doc.packages.append(Command('usepackage{tkz-euclide}'))
	doc.append(Command('usetkzobj{all}'))
	#used
	'''
	header = PageStyle('header')

	#LEFT HEADER
	with header.create(Head('L')):
		header.append("Name:")
		header.append(LineBreak())
		header.append('%s' % nameOfDoc)

	#RIGHT HEADER
	with header.create(Head('R')):
		header.append('Date: ')

	doc.preamble.append(header)
	doc.change_document_style("header")
	'''
	return doc