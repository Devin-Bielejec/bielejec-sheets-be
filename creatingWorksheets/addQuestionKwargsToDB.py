import sqlite3
import sys
from importlib import import_module
import questions
from createSnippet import createSnippet

def addQuestionKwargsToDB():
    db = sqlite3.connect('../eagerSheets.db')

    cur = db.cursor()
    
    #Get ids - use this to grab classes from files
    cur.execute("SELECT id FROM questions")
    ids = [i[0] for i in cur.fetchall()]

    print(ids)

    #instantiate class instances to get kwargs and toolTips
    for _id in ids:
        print(_id)
        mod = import_module(f"questions.{_id}")
        class_ = getattr(mod, f"_{_id}")

        i = class_()

        for key in i.kwargs:
            #Kwargs is a list of choices
            if isinstance(i.kwargs[key], list):
                #There is a tool tip for each kwarg
                if isinstance(i.toolTips[key], dict):
                    for item in i.kwargs[key]:
                        cur.execute(f"INSERT INTO questionsKwargs VALUES (?,?,?,?)",(_id,key,item,i.toolTips[key][item]))
                #Tool tip is same for everything
                else:
                    for item in i.kwargs[key]:
                        cur.execute(f"INSERT INTO questionsKwargs VALUES (?,?,?,?)",(_id,key,item,i.toolTips[key]))
            else:
                cur.execute(f"INSERT INTO questionsKwargs VALUES (?,?,?,?)", (_id,key,i.kwargs[key],i.toolTips[key]))

        if _id == "6":
            createSnippet(_id, class_, {})

    # # Save (commit) the changes
    db.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    db.close()



addQuestionKwargsToDB()
