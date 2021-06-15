# bielejec-sheets-be

##Process

1. Create python classes in creatingWorksheets/questions
   -Make sure to add them to the most parent file (createDocument)
   -export a dictionary of the class (see other files for examples)

2. Knex
   -migrations should be good for a while, but don't mess up users
   -seeds get info from classes in updateDatabase.py file
   -seeds also add a property to link to storage of photo online

3. Image Storage online
   -createSnippets.py will create the snippets for a particular folder
   -then manually add those files (id's as names) to the google site
   -console.cloud.google.com

##Database planning

Tables

\*\*document creation can be stored

Questions -
id
Standard
PrimarySkill
SecondarySkill
PrimaryTopic
SecondaryTopic
Notes
Type
Points

QuestionsKwargs -
questionID references id in questions
key
value
tooltip
**if value is bool, assume checkbox
**if value is not bool, assume group of

Assignments -
id
name
type
points
date

AssignmentQuestions -
assignmentid from id in assignments
questionnumber
questionid from id in questions

Students -
id
first
last
sport
interest
birthday
schoolID

Attendance -
studentid references id in students
date
late - integer late
present - bool

CompletedAssignments -
studentid references id in students
assignmentid refernces id in assignments
questionnumber ref questionumber in assignments

##What does the document creation app look like

1.Pick questions
-edit for more specificity
2.Create Document with document options
-create document

Behind the Scenes
-python flask
-gets specifics for questions
-gets questions
-get default already created worksheets
-creates worksheets

-node BE for authentication login etc
