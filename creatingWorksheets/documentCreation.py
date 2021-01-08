from pylatex.base_classes import Environment, CommandBase, Arguments
from pylatex.package import Package
from pylatex import Document, Section, UnsafeCommand, TikZ, Command, Figure, VerticalSpace, NewPage, NewLine, SubFigure, HorizontalSpace, Center, Package
from pylatex import Document, PageStyle, Head, MiniPage, Foot, LargeText, MediumText, LineBreak, simple_page_number
import math
from pylatex.utils import NoEscape, escape_latex
import time
import random
import os
import sys
sys.path.append('./utils/')
from questionFormatting import multipleChoice
    
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

def createPDFdocument(path="/", nameOfDoc = "default", questions = [], font = "normalsize", answers = False, solutions = False):
	doc = createDocument(path=path, nameOfDoc=nameOfDoc, font=font)

	if answers:
		nameOfDocAnswers = f"answers - {nameOfDoc}"
		docAnswer = createDocument(path=path, nameOfDoc=nameOfDocAnswers, font=font)

	for i, question in enumerate(questions, start=0):
		correctAnswerNum = None
		with doc.create(MiniPage(width=r"\textwidth")): #Preventing questions from splitting between pages
			doc.append(NoEscape(f"({i+1}) "))
			#Start with assessment question, then worksheet after
			for questionParts in question.assessmentData:
				if "text" in questionParts:
					doc.append(NoEscape(questionParts["data"]))
				if "multipleChoice" in questionParts:
					correctAnswerNum = multipleChoice(choices = questionParts["data"], doc = doc)
					print(correctAnswerNum, questionParts["data"])
				doc.append(NewLine())
			
		#line break before next question
		doc.append(LineBreak())

		if answers:
			with docAnswer.create(MiniPage(width=r"\textwidth")):
				if correctAnswerNum is not None:
					docAnswer.append(NoEscape(f"({i+1}) Choice {correctAnswerNum}: {question.answer if question.answer is not None else question.worksheetAnswer}"))
				else:
					docAnswer.append(NoEscape(f"({i+1}) {question.answer if question.answer is not None else question.worksheetAnswer}"))

			#line break before next answer
			docAnswer.append(NewLine())
			docAnswer.append(LineBreak())


	doc.generate_pdf(path + nameOfDoc, clean=True)
	if solutions:
		docSolution.generate_pdf(path + nameOfDocSolutions)
	elif answers:
		docAnswer.generate_pdf(path + nameOfDocAnswers)
	

def createPDFsnippet(path="/", nameOfDoc = 'default', questions = [], font = 'normalsize'):
	print(path, nameOfDoc, questions)
	#This is for displaying a single question, so it can them be converted to an image.
	doc = Document(documentclass='standalone', indent=False, font_size=font)

	doc.packages.append(Package('tikz'))
	doc.packages.append(Command('usetikzlibrary{calc}'))
	doc.packages.append(Command('usepackage{tkz-euclide}'))
	doc.packages.append(Package('subfig'))
	
	# header = PageStyle('header')

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

	# #LEFT HEADER
	# with header.create(Head('L')):
	# 	header.append("Name:")
	# 	header.append(LineBreak())
	# 	header.append('%s' % nameOfDoc)

	# #RIGHT HEADER
	# with header.create(Head('R')):
	# 	header.append('Date: ')

	# if spaceBetween == 'normal':
	# 	space = '1in'

	# doc.preamble.append(header)
	# doc.change_document_style("header")    

	#Add instance of question from questions list
	question = questions[0]
	question.addQuestion(doc = doc)

	print(nameOfDoc)
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


def clearPage(doubleSidedPrinting = True, doc = None):
	if doubleSidedPrinting == True:
		doc.append(Command('cleardoublepage'))
	else:
		doc.append(Command('clearpage'))

# def createWorksheet(path = '/', questions = [], nameOfDoc = 'default', nameOfDocAnswers = 'default', spaceBetween = r'.25in', spaceBetweenMC = 'blah', spaceBetweenSA = 'blah', questionOrder = None, columns = 2, docCreate = None, docAnswerCreate = None, standalone = False, font = 'normalsize', pageNumbers = True, answersAttached = True, numberOfVersions = 1, versionsCombined = True, collatedVersionsWithAnswers = True, doubleSidedPrinting = True, referenceSheet = None):
# 	print('spaceBetweenMC', spaceBetweenMC)
# 	nameOfDocAnswers = nameOfDoc + "Answers"
# 	startTime = time.time()
# 	#answersAttached (doc = docAnswer or NOT)
# 	# - cleardoublepage after doc if doubleSidedPrinting = True
# 	# - clearpage if doubleSidedPrinting = False
# 	# - add answerkey to doc, NOT DOCANSWER
# 	# docAnswer = doc

# 	#versionsCombined (1 doc, 1 docAnswer ELSE 1 doc_AnswersAttached OR X doc etc)
# 	# - if true: all questions for all versions are on same doc, so use cleardoublepage

# 	#collatedVersions with Answers (if vc = True, 1 doc 1 docAnswer)
# 	# - only applicable if versionsCombined - - add question then docAnswer to doc

# 	if versionsCombined == True or numberOfVersions == 1: #1 or 2 files
# 		if docCreate == True:
# 			doc = createDocument(nameOfDoc = nameOfDoc, font = font, pageNumbers = pageNumbers, spaceBetween = spaceBetween)
# 		if docAnswerCreate == True:
# 			docAnswer = createDocument(nameOfDoc = nameOfDocAnswers, font = font, pageNumbers = pageNumbers, spaceBetween = spaceBetween)
# 		if answersAttached == True : #only 1 file now
# 			docAnswer = doc

# 	originalNameOfDoc = nameOfDoc
# 	originalNameOfDocAnswers = nameOfDocAnswers

# 	for version in range(1, numberOfVersions+1):
# 		#declare the names pertaining to the original ones, so versions don't combine
# 		nameOfDocAnswers = originalNameOfDoc + "Answers"
# 		nameOfDoc = originalNameOfDoc

# 		if numberOfVersions > 1:
# 			nameOfDoc += "_Version#%d" % version
# 			nameOfDocAnswers += "_Version#%d" % version

# 			if versionsCombined == False:
# 				if docCreate == True:
# 					doc = createDocument(nameOfDoc = nameOfDoc, font = font, pageNumbers = pageNumbers, spaceBetween = spaceBetween)
			
# 				if docAnswerCreate == True:
# 					docAnswer = createDocument(nameOfDoc = nameOfDocAnswers, font = font, pageNumbers = pageNumbers, spaceBetween = spaceBetween)
# 				if answersAttached == True:
# 					docAnswer = doc

				
# 				#Now I would create the doc and docAnswers and generate the files - it will take just as long etc
# 				for item, questionNumber in zip(questions, range(1, len(questions)+1)):
# 					test = item
# 					#We are going to add spaces before the item, unless it the first item
# 					#if test item about to add is a short answer and spaceBetweenSA == wholepage, then we need to clear the page.
# 					if columns == 1:
# 						if questionNumber != 1:
# 							if 'SA' in test.typeOfQuestionChosen:
# 								if spaceBetweenSA == 'wholepage':
# 									doc.append(Command('newpage'))
# 								else:
# 									doc.append(VerticalSpace(spaceBetweenSA))
# 									doc.append(NewLine())

# 							elif 'MC' in test.typeOfQuestionChosen:
# 								if spaceBetweenMC != 'blah':
# 									doc.append(VerticalSpace(spaceBetweenMC))
# 									doc.append(NewLine())
									
# 									chicken = 2
						
# 					addHeader(doc = doc, nameOfDoc = nameOfDoc)
# 					if doc:
# 						#with doc.create(Figure(position='p')):
# 						with doc.create(MiniPage(width=r'%g\textwidth' % (1/(columns+.2)))):
# 							doc.append(NoEscape('%d. ' % (questionNumber)))
						
# 							test.addQuestion(doc = doc)      
# 							#check if question is MC or not,
# 							if columns > 1:
# 								doc.append(VerticalSpace(spaceBetween))
# 								#doc.append(NewLine())


# 						if columns > 1:
# 							if questionNumber % columns != 0:
# 								#every question besides lasts adds a space between the columns
# 								doc.append(HorizontalSpace('.2in'))
# 							elif questionNumber % columns == 0:
# 								#if last question, add vertical space and new line, so it goes to next row.
# 								doc.append(NewLine())
# 						else:
# 							doc.append(NewLine())

# 				if referenceSheet != None:
# 					clearPage(doubleSidedPrinting = doubleSidedPrinting, doc = doc)
# 					with doc.create(Figure(position="h!")) as referenceSheet:
# 						referenceSheet.add_image('/home/devin/webapp/devins_project/ReferenceSheet.PNG')
				
# 				if doubleSidedPrinting == True:
# 					doc.append(Command('cleardoublepage'))
# 				else:
# 					doc.append(Command('clearpage'))
				
# 				addHeader(doc = docAnswer, nameOfDoc = nameOfDocAnswer)    
# 				for item, questionNumber in zip(questions, range(1, len(questions)+1)):
# 					test = item    
# 					if docAnswer:
# 						#ANSWER KEY
# 						#with docAnswer.create(Figure(position='p')):
# 						#with docAnswer.create(MiniPage(width=r'%g\textwidth' % (1/(columns+.2)))):
# 						docAnswer.append(NoEscape('%d.  ' % (questionNumber)))
# 						test.addAnswer(docAnswer = docAnswer)    
# 						docAnswer.append(NewLine())

# 				if doubleSidedPrinting == True:
# 					docAnswer.append(Command('cleardoublepage'))
# 				else:
# 					docAnswer.append(Command('clearpage'))

# 				if answersAttached == True:
# 					#generates the pdf in the same directory as the file.
# 					doc.generate_pdf(path + nameOfDoc + '_AnswersAttached', clean = True)
# 				else:
# 					#generates answerkey doc
# 					doc.generate_pdf(path + nameOfDoc, clean = True)
# 					docAnswer.generate_pdf(path + nameOfDocAnswers, clean = True)
   
# 			#else when they are combined, we'll make 1 doc, 1 docAnswer outside before loop, so here can add shit to it
# 			else:
# 				if collatedVersionsWithAnswers == True and answersAttached == True:
# 					#we'll add the docQuestion then docAnswer in order, clearing doublepage if true etc
# 					#Now I would create the doc and docAnswers and generate the files - it will take just as long etc
# 					clearPage(doubleSidedPrinting = doubleSidedPrinting, doc = doc)
# 					for item, questionNumber in zip(questions, range(1, len(questions)+1)):
# 						test = item
# 						#We are going to add spaces before the item, unless it the first item
# 						#if test item about to add is a short answer and spaceBetweenSA == wholepage, then we need to clear the page.
# 						if columns == 1:
# 							if questionNumber != 1:
# 								if 'SA' in test.typeOfQuestionChosen:
# 									if spaceBetweenSA == 'wholepage':
# 										doc.append(Command('newpage'))
# 									else:
# 										doc.append(VerticalSpace(spaceBetweenSA))
# 										doc.append(NewLine())
# 								elif 'MC' in test.typeOfQuestionChosen:
# 									if spaceBetweenMC != 'blah':
# 										doc.append(VerticalSpace(spaceBetweenMC))
# 										doc.append(NewLine())
										
# 										chicken = 2

# 						addHeader(doc = doc, nameOfDoc = nameOfDoc)
# 						if doc:
# 							#with doc.create(Figure(position='p')):
# 							with doc.create(MiniPage(width=r'%g\textwidth' % (1/(columns+.2)))):
# 								doc.append(NoEscape('%d. ' % (questionNumber)))

# 								test.addQuestion(doc = doc)
# 								if columns > 1:
# 									doc.append(VerticalSpace(spaceBetween)) 
# 									#doc.append(NewLine())
# 							if columns > 1:
# 								if questionNumber % columns != 0:
# 									#every question besides lasts adds a space between the columns
# 									doc.append(HorizontalSpace('.2in'))
# 								elif questionNumber % columns == 0:
# 									#if last question, add vertical space and new line, so it goes to next row.
# 									doc.append(NewLine())
# 							else:
# 								doc.append(NewLine())
					
# 					if referenceSheet != None:
# 						clearPage(doubleSidedPrinting = doubleSidedPrinting, doc = doc)
# 						with doc.create(Figure(position="h!")) as referenceSheet:
# 							referenceSheet.add_image('/home/devin/webapp/devins_project/ReferenceSheet.PNG')

# 					clearPage(doubleSidedPrinting = doubleSidedPrinting, doc = docAnswer)
# 					for item, questionNumber in zip(questions, range(1, len(questions)+1)):
# 						test = item  
# 						addHeader(doc = docAnswer, nameOfDoc = nameOfDocAnswers)  
# 						if docAnswer:
# 							#ANSWER KEY
# 							#with docAnswer.create(Figure(position='p')):
# 							docAnswer.append(NoEscape('%d.  ' % (questionNumber)))
# 							test.addAnswer(docAnswer = docAnswer)    
# 							docAnswer.append(NewLine())

# 				else: #verions combined but answers not attached, so 2 files
# 					#Going to add questions to the doc, add questions to a dict of sets of questions, so that I can iterate through another loop to add the answers after the first loop is complete. 
# 					clearPage(doubleSidedPrinting = doubleSidedPrinting, doc = doc)
					
# 					for item, questionNumber in zip(questions, range(1, len(questions)+1)):
# 						test = item

# 						#We are going to add spaces before the item, unless it the first item
# 						#if test item about to add is a short answer and spaceBetweenSA == wholepage, then we need to clear the page.
						
# 						if columns == 1:
# 							if questionNumber != 1:
# 								if 'SA' in test.typeOfQuestionChosen:
# 									if spaceBetweenSA == 'wholepage':
# 										doc.append(Command('newpage'))
# 									else:
# 										doc.append(VerticalSpace(spaceBetweenSA))
# 										doc.append(NewLine())
# 								elif 'MC' in test.typeOfQuestionChosen:
# 									if spaceBetweenMC != 'blah':
# 										doc.append(VerticalSpace(spaceBetweenMC))
# 										doc.append(NewLine())
						
# 						addHeader(doc = doc, nameOfDoc = nameOfDoc)
# 						if doc:
# 							#with doc.create(Figure(position='p')):
# 							with doc.create(MiniPage(width=r'%g\textwidth' % (1/(columns+.2)))):

# 								doc.append(NoEscape('%d. ' % (questionNumber)))
# 								test.addQuestion(doc = doc)
# 								if columns > 1:
# 									doc.append(VerticalSpace(spaceBetween))
# 									#doc.append(NewLine())

							
# 							if columns > 1:
# 								if questionNumber % columns != 0:
# 									#every question besides lasts adds a space between the columns
# 									doc.append(HorizontalSpace('.2in'))
# 								elif questionNumber % columns == 0:
# 									#if last question, add vertical space and new line, so it goes to next row.
# 									doc.append(NewLine())
# 							else:
# 								doc.append(NewLine())

# 						with open(path + 'version%dquestion%d.pkl' % (version, questionNumber), 'wb') as output:
# 							pickle.dump(test, output, pickle.HIGHEST_PROTOCOL)
# 						del test

# 					if referenceSheet != None:
# 						clearPage(doubleSidedPrinting = doubleSidedPrinting, doc = doc)
# 						with doc.create(Figure(position="h!")) as referenceSheet:
# 							referenceSheet.add_image('/home/devin/webapp/devins_project/ReferenceSheet.PNG')
						
# 		else: #1 VERSION
# 			clearPage(doubleSidedPrinting = doubleSidedPrinting, doc = doc)
# 			#Now I would create the doc and docAnswers and generate the files - it will take just as long etc
			
# 			for item, questionNumber in zip(questions, range(1, len(questions)+1)):
# 				test = item
			   
# 				#We are going to add spaces before the item, unless it the first item
# 				#if test item about to add is a short answer and spaceBetweenSA == wholepage, then we need to clear the page.
# 				if columns == 1:
# 					if questionNumber != 1:
# 						if 'SA' in test.typeOfQuestionChosen:
# 							if spaceBetweenSA == 'wholepage':
# 								doc.append(Command('newpage'))
# 							else:
# 								doc.append(VerticalSpace(spaceBetweenSA))
# 								doc.append(NewLine())
# 						elif 'MC' in test.typeOfQuestionChosen:
# 							if spaceBetweenMC != 'blah':
# 								doc.append(VerticalSpace(spaceBetweenMC))
# 								doc.append(NewLine())

# 				addHeader(doc = doc, nameOfDoc = nameOfDoc)
# 				if doc:
# 					#with doc.create(Figure(position='p')):
# 					with doc.create(MiniPage(width=r'%g\textwidth' % (1/(columns+.2)))):

# 						doc.append(NoEscape('%d. ' % (questionNumber)))
# 						#check if question is MC or not, 
# 						#for testing for answer
# 						test.addQuestion(doc = doc)
# 						if columns > 1:
# 							doc.append(VerticalSpace(spaceBetween))
# 							#doc.append(NewLine())
# 						else:
# 							dick = 1
# 							#doc.append(NewLine())

# 					if columns > 1:
# 						if questionNumber % columns != 0:
# 							#every question besides lasts adds a space between the columns
# 							doc.append(HorizontalSpace('.2in'))
# 						elif questionNumber % columns == 0:
# 							#if last question, add vertical space and new line, so it goes to next row.
# 							doc.append(NewLine())
# 					else:
# 						doc.append(NewLine())
			
# 			clearPage(doubleSidedPrinting = doubleSidedPrinting, doc = docAnswer)
			
# 			if referenceSheet != None:
# 				clearPage(doubleSidedPrinting = doubleSidedPrinting, doc = doc)
# 				with doc.create(Figure(position="h!")) as referenceSheet:
# 					referenceSheet.add_image('/home/devin/webapp/devins_project/ReferenceSheet.PNG')
			
# 			for item, questionNumber in zip(questions, range(1, len(questions)+1)):
# 				test = item 
# 				addHeader(doc = docAnswer, nameOfDoc = nameOfDocAnswers) 
# 				if docAnswer:
# 					#ANSWER KEY
# 					#with docAnswer.create(Figure(position='p')):
# 					docAnswer.append(NoEscape('%d.  ' % (questionNumber)))
# 					test.addAnswer(docAnswer = docAnswer)
# 					docAnswer.append(NewLine())    
					
	
# 	if ((versionsCombined == True and collatedVersionsWithAnswers == False) or (versionsCombined == True and answersAttached == False)) and numberOfVersions > 1: #2 files and order fucking matters
# 		for version in range(1, numberOfVersions+1):
# 			nameOfDocAnswers = originalNameOfDoc + "Answers"
# 			nameOfDoc = originalNameOfDoc
			
# 			nameOfDoc += "_Version#%d" % version
# 			nameOfDocAnswers += "_Version#%d" % version
# 			clearPage(doubleSidedPrinting = doubleSidedPrinting, doc = docAnswer)
			
# 			for item, questionNumber in zip(questions, range(1, len(questions)+1)):
# 				addHeader(doc = docAnswer, nameOfDoc = nameOfDocAnswers)
# 				with open(path + 'version%dquestion%d.pkl' % (version, questionNumber), 'rb') as input:
# 					whatever = pickle.load(input)
# 				#os.remove(path + 'version%dquestion%d.pk1' % (version, questionNumber))    
	
# 				if docAnswer:
# 					#ANSWER KEY
# 					#with docAnswer.create(Figure(position='p')):
# 					docAnswer.append(NoEscape('%d.  ' % (questionNumber)))
# 					whatever.addAnswer(docAnswer = docAnswer)    
# 					docAnswer.append(NewLine())
				
# 	if versionsCombined == True and numberOfVersions > 1: #1 or 2 files
# 		nameOfDoc = originalNameOfDoc + '_versionsCombined'
# 		nameOfDocAnswers = originalNameOfDocAnswers + "_versionsCombined"

# 		if answersAttached == True : #only 1 file now
# 			nameOfDoc += '_answersAttached'
# 			if collatedVersionsWithAnswers == True:
# 				nameOfDoc += '_collatedVersionsWithAnswers'
# 			else:
# 				nameOfDoc += '_nonCollatedVersionsWithAnswers'

# 			doc.generate_pdf(path + nameOfDoc, clean = True)
		
# 		else: #doc and docAnswer
# 			doc.generate_pdf(path + nameOfDoc, clean = True)
# 			docAnswer.generate_pdf(path + nameOfDocAnswers, clean = True)

# 	if numberOfVersions == 1:
# 		if answersAttached == True: #one doc
# 			nameOfDoc += '_answersAttached'
			
# 			doc.generate_pdf(path + nameOfDoc, clean = True)
# 		else: #two docs
# 			#generates the pdf in the same directory as the file.
			
# 			doc.generate_pdf(path + nameOfDoc, clean = True)
# 			#generates answerkey doc
# 			docAnswer.generate_pdf(path + nameOfDocAnswers, clean = True)
# 	print('createdWorksheet took ', time.time() - startTime, "to run")