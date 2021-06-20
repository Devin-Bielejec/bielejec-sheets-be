import sqlite3

def addQuestionToDB(questionClass):
    #The class holds the information that we need to add to our database
    i = questionClass()

    db = sqlite3.connect('eagerSheets.db')

    cur = db.cursor()

    #Add question to questions table - This will only be one row
    if i.worksheetQuestion:
        typeOfQuestion = "Worksheet"
    else:
        typeOfQuestion = "Test"

    print(i.id, i.standard, i.skill, i.subSkill, i.topic, i.subTopic, i.notes, typeOfQuestion)
    cur.execute("INSERT INTO questions VALUES (?,?,?,?,?,?,?,?)", (i.id,i.standard,i.skill,i.subSkill,i.topic,i.subTopic,i.notes,typeOfQuestion))

    for key in i.kwargs:
        #Kwargs is a list of choices
        if isinstance(i.kwargs[key], list):
            #There is a tool tip for each kwarg
            if isinstance(i.toolTips[key], dict):
                for item in i.kwargs[key]:
                    print(item, i.kwargs[key])
                    cur.execute(f"INSERT INTO questionsKwargs VALUES (?,?,?,?)",(i.id,key,item,i.toolTips[key][item]))
            #Tool tip is same for everything
            else:
                for item in i.kwargs[key]:
                    print(i.id, key, item, i.toolTips[key])
                    cur.execute(f"INSERT INTO questionsKwargs VALUES (?,?,?,?)",(i.id,key,item,i.toolTips[key]))
        else:
            cur.execute(f"INSERT INTO questionsKwargs VALUES (?,?,?,?)", (i.id,key,i.kwargs[key],i.toolTips[key]))

    # # Save (commit) the changes
    db.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    db.close()

import sys
sys.path.append('../')

from creatingWorksheets.questions.Algebra import questionsDict

for key in questionsDict:
    addQuestionToDB(questionsDict[key])