import sys
from importlib import import_module
import questions
from createSnippet import createSnippet
import json


def addQuestionKwargsToDB():
    #questions as list
    f = open('questions.json')
    data = json.load(f)
    questions = []
    for i in data:
        questions.append(data[i])

    #get ids from questions - create all new questionsKwargs everytime
    ids = [i["id"] for i in questions]
    
    questionsKwargs = []

    #instantiate class instances to get kwargs and toolTips
    for _id in ids:
        mod = import_module(f"questions.{_id}")
        class_ = getattr(mod, f"_{_id}")
        i = class_()

        for key in i.kwargs:
            #Kwargs is a list of choices
            if isinstance(i.kwargs[key], list):
                #There is a tool tip for each kwarg
                if isinstance(i.toolTips[key], dict):
                    for item in i.kwargs[key]:
                        questionsKwargs.append({"questionID": _id, "key": key, "value": item, "toolTip": i.toolTips[key][item]})
                #Tool tip is same for everything
                else:
                    for item in i.kwargs[key]:
                        questionsKwargs.append({"questionID": _id, "key": key, "value": item, "toolTip": i.toolTips[key]})
            elif isinstance(i.kwargs[key], bool):
                questionsKwargs.append({"questionID": _id, "key": key, "value": True, "toolTip": i.toolTips[key]})
                questionsKwargs.append({"questionID": _id, "key": key, "value": False, "toolTip": i.toolTips[key]})

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

        with open("./questionsKwargs.json", "w") as outfile:
            json.dump(questionsKwargs, outfile, indent=2)



addQuestionKwargsToDB()
