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

    cur.execute("SELECT questionID FROM questionsKwargs")
    idsFromKwargs = [i[0] for i in cur.fetchall()]
    print(ids)
    
    print(idsFromKwargs)
    idsToAdd = [x for x in ids if x not in idsFromKwargs]
    print("ids to add",ids)

    #instantiate class instances to get kwargs and toolTips
    for _id in idsToAdd:
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
            elif isinstance(i.kwargs[key], bool):
                cur.execute(f"INSERT INTO questionsKwargs VALUES (?,?,?,?)", (_id,key,True,i.toolTips[key]))
                cur.execute(f"INSERT INTO questionsKwargs VALUES (?,?,?,?)", (_id,key,False,i.toolTips[key]))

    #Make snippet if doesn't exists - nice for troulbe shooting
    for _id in ids:
        from pathlib import Path
        mod = import_module(f"questions.{_id}")
        class_ = getattr(mod, f"_{_id}")
        i = class_()   

        #Create all possible combinations from kwargs
        import itertools

        kwargsValues = []
        for key in i.kwargs:
            values = []
            if isinstance(i.kwargs[key], bool):
                values.append(True)
                values.append(False)
            elif isinstance(i.kwargs[key], list):
                for item in i.kwargs[key]:
                    values.append(item)
            kwargsValues.append(values)
        
        combos = list(itertools.product(*kwargsValues))
        keys = [x for x in i.kwargs.keys()]

        for combo in combos:
            currentKwargs = {}
            filePath = f"{_id}"
            for key, value in zip(keys, combo):
                currentKwargs[key] = value
                filePath += f",{key}={value}"
            if not Path(f"../creatingWorksheets/images/{filePath}.jpg").is_file():
                createSnippet(class_, currentKwargs, filePath)


    # # Save (commit) the changes
    db.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    db.close()



addQuestionKwargsToDB()
