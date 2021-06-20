# bielejec-sheets-be

##Process
FE (React)

-navbar (login)

-one page app

-1) Document options

Filling in a small form will store the document options in state for the given user

-2) pick questions

Filter eventually (but for now display all questions)

Store image thumbnails on backend

SQL Grab all questions and kwargs and pictures by id

Render question component (thumbnail with edit for more specifics/+ and int for how many to add

Adding questions add the questions (pushing to the array of in state questions for the document)

3. Review - shows document - can rearrange order etc - multiple versions - create document

-sends data to python BE and sends back pdf

Python BE

/signup

/login

/getQuestionsBy

/createDocument

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
