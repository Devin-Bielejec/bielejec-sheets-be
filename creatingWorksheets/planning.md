###Different moving parts

##document creation of the actual pdf
-takes in different options
-takes in all the classes of questions created
-halfsheet/quarter sheet etc
-snippets to store on FE / firebase
-automatic process from finishing a question -> uploading info to datase, snippet to image datebase, etc
-create the DOC inside this function then create the instatiation and pass DOC into the methods on each question class

##answers/solutions
-answer sheets
-solutions sheets??

##storage of all the classes and such
-can we store them in a database?
-database should definitely hold information and classID
-PROBLEM: DB will hold all question information but will need to have a reference to the class that will hold the logic for creating the actual question/will actually add it to the document. In my mind, putting the class instantiation into the DB makes sense but I don't think that's possible. The only solution I have thus far is to hardcode (cache if you will) a dictionary {"CLASSID": class(\**kwargs, *args)} and have a function take the current kwargs args and classID to generate the given question etc.

##DB
-standard
-topic
-subtopic
-skills
-regentsExam
-state

##mathy stuff
-different graphical functions
-algebraic functions
-topic questions

##the actual questions
-group by regents exams? topic?
-storing all of this informatmion into the database
-classes handle interacting with the latex
-function actually handle the math aspects
-function formatting questions (multiple choice answers, multiple choice question, short answer, etc, etc)
