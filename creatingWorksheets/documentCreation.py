from pylatex.base_classes import Environment, CommandBase, Arguments
from pylatex.package import Package
from pylatex import UnsafeCommand, TikZ, Command, Figure, VerticalSpace, NewPage, NewLine, SubFigure, HorizontalSpace, Center, Package, Alignat, TextBlock, Document, PageStyle, Head, MiniPage, Foot, LargeText, MediumText, LineBreak, simple_page_number, Subsection
import math
from pylatex.utils import NoEscape, escape_latex
import time
import random
import os
import sys
from importlib import import_module
import questions
sys.path.append('./utils/')
from utils.questionFormatting import multipleChoice
from utils.shapes import *
from utils.transformations import *
from utils.pdfFunctions import *

def createDocument(
	path="/", 
	nameOfDoc = 'default', 
	font = 'normalsize', 
	pageNumbers = True, 
	spaceBetween = 'normal', 
	spaceBetweenMC = 'normal', 
	spaceBetweenSA = 'normal', 
	standalone = False):
	
	if standalone == False:
		#Can make rmargin bigger for more work etc usually for MC to provide a column of work
		geometry_options = {"top": "1in", "lmargin": ".5in", "rmargin": ".5in"}
		doc = Document(documentclass='article', document_options = 'twoside', geometry_options = geometry_options, indent=False, font_size=font, page_numbers=pageNumbers)


	# # float separation, does something important
	# doc.append(Command('setlength{\\floatsep}{1.0pt plus 5.0pt minus 2.0pt}'))
	# doc.append(Command('setlength{\\intextsep}{1.0pt plus 5.0pt minus 2.0pt}'))
	# doc.append(Command('setlength{\\textfloatsep}{1.0pt plus 5.0pt minus 2.0pt}'))
	# doc.append(Command('setcounter{topnumber}{10}'))
	# doc.append(Command('setcounter{bottomnumber}{10}'))
	# doc.append(Command('setcounter{totalnumber}{10}'))

	# # makes float appear at top of page at the last page
	# doc.append(Command('makeatletter'))
	# doc.append(Command('setlength{\\@fptop}{0pt}'))
	# doc.append(Command('setlength{\\@fpbot}{0pt plus 1fil}'))
	# doc.append(Command('makeatother'))
	doc.append(Command('linespread{1.3}'))

	doc.packages.append(Package('subfig'))
	doc.append(Command('usetikzlibrary{calc}'))
	doc.packages.append(Command('usepackage{tkz-euclide}'))
	#used
	
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
	
	return doc

def handleQuestionPart(doc, questionPart):
	# {"text": "followingText"
	# {"multipleChoice": choices}

	if "text" in questionPart:
		#Center environment
		if "center" in questionPart["text"]:
			with doc.create(Center()):
				for part in questionPart["text"]["center"]:
					doc.append(NoEscape(part))
					doc.append(NewLine())
		#for aligning equations that are centered
		elif "center-aligned" in questionPart["text"]:
			with doc.create(Center()):
				with doc.create(Alignat(numbering=False,escape=False)) as agn:
					for part in questionPart["text"]["center-aligned"]:
						#add & before =
						part = part.replace("=", "&=")
						#aligned env dont' need $
						part = part.replace("$","")
						agn.append(part+r"\\")						
		else:
			doc.append(NoEscape(questionPart["text"]))
	elif "multipleChoice" in questionPart:
		correctAnswerNum = multipleChoice(choices = questionPart["multipleChoice"], doc = doc)
	elif "picture" in questionPart:
		dicty = questionPart["picture"]
		if "cube" in dicty:
			kwargs = dicty["cube"]
			with doc.create(Center()):
				cube(options = 'rotate=%d, x=2.5cm, y=2.5cm' % (kwargs["wholeFigureRotation"]), 
					doc = doc, 
					sideLabeledOnDiagram = kwargs["sideLabeledOnDiagram"], 
					sideValue = kwargs["sideValue"])
		elif "rectangular prism" in dicty:
			kwargs = dicty["rectangular prism"]
			with doc.create(Center()):
				rectangularPrism(options = 'rotate=%d, x=2.5cm, y=2.5cm' % (kwargs["wholeFigureRotation"]), 
					doc = doc, 
					heightLabeledOnDiagram = kwargs["diagramLabeled"], 
					widthLabeledOnDiagram = kwargs["diagramLabeled"],
					lengthLabeledOnDiagram = kwargs["diagramLabeled"], 
					heightValue = kwargs["height"],
					widthValue = kwargs["width"],
					lengthValue = kwargs["length"],
					baseRotation = kwargs["baseRotation"])
		elif "regular square pyramid" in dicty:
			kwargs = dicty["regular square pyramid"]
			with doc.create(Center()):
				regularPyramid(options = 'rotate=%d, x=2.5cm, y=2.5cm' % (kwargs["wholeFigureRotation"]), 
					doc = doc, 
					sideLabeledOnDiagram = kwargs["diagramLabeled"], 
					sideValue = kwargs["sideValue"],
					heightLabeledOnDiagram = kwargs["diagramLabeled"],
					heightValue = kwargs["height"])
		elif "cylinder" in dicty:
			kwargs = dicty["cylinder"]
			with doc.create(Center()):
				cylinder(options = 'rotate=%d, x=2.5cm, y=2.5cm' % (kwargs["wholeFigureRotation"]), 
					doc = doc, 
					radiusDrawn = kwargs["radiusDrawn"], 
					diameterDrawn = kwargs["diameterDrawn"], 
					radiusLabeledOnDiagram = kwargs["diagramLabeled"] and kwargs["radiusDrawn"], 
					heightLabeledOnDiagram = kwargs["diagramLabeled"], 
					diameterLabeledOnDiagram = kwargs["diagramLabeled"] and kwargs["diameterDrawn"], 
					radiusValue = kwargs["radius"], 
					diameterValue = kwargs["diameter"], 
					heightValue = kwargs["height"])
		elif "cone" in dicty:
			kwargs = dicty["cone"]
			with doc.create(Center()):
				cone(options = 'rotate=%d, x=2.5cm, y=2.5cm' % (kwargs["wholeFigureRotation"]), 
					doc = doc, 
					radiusDrawn = kwargs["radiusDrawn"], 
					diameterDrawn = kwargs["diameterDrawn"], 
					radiusLabeledOnDiagram = kwargs["diagramLabeled"] and kwargs["radiusDrawn"], 
					heightLabeledOnDiagram = kwargs["diagramLabeled"], 
					diameterLabeledOnDiagram = kwargs["diagramLabeled"] and kwargs["diameterDrawn"], 
					radiusValue = kwargs["radius"], 
					diameterValue = kwargs["diameter"], 
					heightValue = kwargs["height"])
		elif "sphere" in dicty:
			kwargs = dicty["sphere"]
			with doc.create(Center()):
				sphere(options = 'rotate=%d, x=2.5cm, y=2.5cm' % (kwargs["wholeFigureRotation"]), 
					doc = doc, 
					radiusDrawn = kwargs["radiusDrawn"], 
					diameterDrawn = kwargs["diameterDrawn"], 
					radiusLabeledOnDiagram = kwargs["diagramLabeled"] and kwargs["radiusDrawn"], 
					diameterLabeledOnDiagram = kwargs["diagramLabeled"] and kwargs["diameterDrawn"], 
					radiusValue = kwargs["radius"], 
					diameterValue = kwargs["diameter"])
	elif "graph" in questionPart:
		currentDict = questionPart["graph"]
		picLength = sizingXY(minn = -10, maxx = 10, size = 'small')
		with doc.create(Center()):
			with doc.create(TikZ(options='x=%gcm, y=%gcm' % (picLength, picLength))):
				grid(doc = doc)
				graphPolygon(doc = doc, x = currentDict["x"], y = currentDict["y"], annotations = currentDict["annotations"], color = currentDict["color"])

def createPDF(path="/", nameOfDoc = "default", versionQuestions = [], columns = 1, font = "normalsize", answers = False, collatedAnswerKey = False, solutions = False, spacingBetween="0in", worksheet = False, texOnly = False):
	doc = createDocument(path=path, nameOfDoc=nameOfDoc, font=font)

	#List of lists used indexed by version to provide answer key information - HELPFUL FOR MULTIPLE CHOICE!
	answerKeyVersions = []

	curDirections = None
	print("versionQuestions", versionQuestions)
	#Loop through each set of questions representing each version	
	for i, version in enumerate(versionQuestions, start=0):
		#Version is a list of questions
		answerKeyQuestions = []
		
		#Currenlty adding version number messes up spacing

		# Remove version # from one versioned things
		# if len(versionQuestions) > 1:
		# 	# # with doc.create(Center()):
		# 	# with doc.create(LargeText(f"Version {i+1}!")):
		# 	# 	doc.append(NewLine())
		# 	doc.append(NoEscape(f"Version {i+1}!"))

		#Question is the question from that specific version
		for j, question in enumerate(versionQuestions[i], start=0):

			#Force first line to not indent
			if i == 0:
				doc.append(Command("noindent"))
			
			correctAnswerNum = None

			#If Directions, create new line, add directions
			if hasattr(question, "directions") and question.directions != curDirections:
				doc.append(NewLine())
				doc.append(NoEscape(question.directions))
				doc.append(NewLine())
				 
				curDirections = question.directions
				
			#.2 for gap between
			with doc.create(MiniPage(width=fr"{1/(columns)}\textwidth")):
				#Add Question Number
				doc.append(NoEscape(f"({j+1}) "))
				
				#If question contains multiple parts
				if type(question.question) == list:
					for questionPart in question.question:
						handleQuestionPart(doc, questionPart)
						# doc.append(NewLine())
						
					#Add answer to answerKey
					answerKeyQuestions.append(question.answer)
				else:
					#question is a single string
					doc.append(NoEscape(question.question))
					
			if (j+1) % columns == 0:
				#Example: 3 columns, we only have to add vertical space when we're on the 3rd question (i+1) for Q Number
				#would add vertical space here
				doc.append(VerticalSpace(spacingBetween, star=False))
				doc.append(NewLine())

	
		answerKeyVersions.append(answerKeyQuestions)

		#After version is printed to PDF, clear page
		doc.append(Command("clearpage"))


		if collatedAnswerKey:
			#Add corresponding answer key if
			#Add title!!!
			
			#Remove version # from one versioned things
			if len(versionQuestions) > 1:
				with doc.create(Center()):
					with doc.create(LargeText(f"Answer Key!")):
						doc.append(NewLine())
			else:
				with doc.create(Center()):
					with doc.create(LargeText(f"Version {i+1} Answer Key!")):
						doc.append(NewLine())

			for j, question in enumerate(versionQuestions[i], start=0):
				worksheet = question.directions != None
				if not worksheet:
					correctAnswerNum = answerKeyQuestions[j]
				else:
					correctAnswerNum = None

				if correctAnswerNum is not None:
					doc.append(NoEscape(f"({j+1}) Choice {correctAnswerNum}: {question.answer}"))
				else:
					doc.append(NoEscape(f"({j+1}) {question.answer}"))
				doc.append(NewLine())
				doc.append(NewLine())

		if i < len(versionQuestions):
			#Clear Page - Before Next Version
			doc.append(Command("clearpage"))

	#If collatedAnswerKey is False, then loop and add answer key pages
	if not collatedAnswerKey:
		print(answerKeyVersions)
		for i, version in enumerate(versionQuestions, start=0):
			
			#Answer Key based on length of versions
			if len(versionQuestions) > 1:
				with doc.create(Center()):
					with doc.create(LargeText(f"Version {i+1} Answer Key!")):
						doc.append(NewLine())
			else:
				with doc.create(Center()):
					with doc.create(LargeText(f"Answer Key!")):
						doc.append(NewLine())

			for j, question in enumerate(versionQuestions[i], start=0):
				worksheet = question.directions != None
				if not worksheet:
					correctAnswerNum = answerKeyVersions[i][j]
				else:
					correctAnswerNum = None
				
				if correctAnswerNum is not None:
					doc.append(NoEscape(f"({j+1}) Choice {correctAnswerNum}: {question.answer}"))
				else:					
					doc.append(NoEscape(f"({j+1}) {question.answer}"))
				doc.append(NewLine())
	
			#Clear Page Before next Version Answer Key
			doc.append(Command("clearpage"))
	
	if texOnly == True:
		doc.generate_tex(path + nameOfDoc)
	else:
		doc.generate_pdf(path + nameOfDoc, clean=True)

def createVersions(documentOptions, numberOfVersions, columns = 1, worksheet = False, collatedAnswerKey = False, path="/"):
	#Attempt for no duplicates
	hash = {}
	defaultDocName = documentOptions["nameOfDoc"]

	#Questions - list of lists for each version of the PDF
	questions = []
	for v in range(numberOfVersions):
		versionQuestions = []
		nameOfDoc = documentOptions["nameOfDoc"]

		print(documentOptions["ids"])
		for questionID, kwargs in zip(documentOptions["ids"], documentOptions["kwargs"]):
			duplicate = True
			loop = 0
			while duplicate:
				loop += 1
				#If finite number of versions, this will prevent infinite loop
				if loop == 100:
					break

				#Get class from file based on integer id
				mod = import_module(f"questions.{questionID}")
				class_ = getattr(mod, f"_{questionID}")
				instance = class_(**kwargs)

				question = ""

				#For duplicates and questions with multiple parts - only look at text parts
				if type(instance.question) == list:
					#Some questions with have question.duplicateCheck (center aligned etc nonsense) while others will just have text to compare for duplicates
					for part in instance.question:
						if not hasattr(instance, "duplicateCheck"):
							if "text" in part:
								question += part["text"]
						else:
							question += instance.duplicateCheck
				else:
					question = instance.question
				
				print(question)
				
				if question+questionID not in hash:
					print("not in hash", question)
					hash[question+questionID] = True
					versionQuestions.append(instance)

					#Stopping the loop for creating a new instance
					duplicate = False
		
		questions.append(versionQuestions)

	#Now have createWorksheet or Assessment take a list of lists
	createPDF(worksheet=worksheet, path=path, nameOfDoc=nameOfDoc, versionQuestions=questions, answers = True, collatedAnswerKey=collatedAnswerKey, spacingBetween=documentOptions["spacingBetween"], columns=columns, texOnly = documentOptions['texOnly'])
	

def createPDFsnippet(path="/", nameOfDoc = 'default', font = 'normalsize', questionClass = "", questionKwargs = {}):
	#This is for displaying a single question, so it can them be converted to an image.
	#Documentclass standlone and removed options for preview == smaller
	doc = Document(documentclass='standalone', indent=False, font_size=font)

	doc.packages.append(Package('tikz'))
	doc.packages.append(Command('usetikzlibrary{calc}'))
	doc.packages.append(Command('usepackage{tkz-euclide}'))
	doc.packages.append(Package('subfig'))
	
	#Add instance of question from questions list
		#List of lists used indexed by version to provide answer key information - HELPFUL FOR MULTIPLE CHOICE!
	if questionKwargs:
		question = questionClass(**questionKwargs)
	else:
		question = questionClass()
	

		
	if type(question.question) == list:		
		with doc.create(MiniPage(width=fr"{1/2}\textwidth")):
			doc.append(NoEscape(question.directions))
			doc.append(NewLine())
	
			for questionPart in question.question:
				handleQuestionPart(doc, questionPart)
	else:
		doc.append(NoEscape(question.directions))
		doc.append(NewLine())

		#question is a single string
		doc.append(NoEscape(question.question))


			
	doc.generate_pdf(path + nameOfDoc, clean=True)
	
def addHeader(doc = None, nameOfDoc = "Default"):
	pageNameTemp = nameOfDoc.replace('#', "")
	pageNameTemp = pageNameTemp.replace(' ', '')
	pageNameTemp = pageNameTemp.replace('_', '')

	pageStyleName = pageNameTemp + 'pageName'
	header = PageStyle(pageStyleName)

	#LEFT HEADER
	with header.create(Head('L')):
		header.append("Name:")
		header.append("________________________________________")
		if 'CW' in nameOfDoc:
			header.append('CLASS WORK')
		elif 'ET' in nameOfDoc:
			header.append('EXIT TICKET')
		elif 'HW' in nameOfDoc:
			header.append('HOME WORK')
		elif 'Quiz' in nameOfDoc:
			header.append('QUIZ')
		elif 'Test' in nameOfDoc:
			header.append('TEST')
		header.append(LineBreak())
		header.append('%s' % nameOfDoc)



	#RIGHT HEADER
	with header.create(Head('R')):
		header.append('#:_____ ')

	doc.preamble.append(header)
	doc.change_page_style(pageStyleName)


