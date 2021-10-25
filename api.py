from flask import Flask, g, request, send_file
from flask_restful import Resource, Api, reqparse
from requests import put, get
import sqlite3
from flask_cors import CORS
import sys
sys.path.insert(0, "F:/code/bielejec-sheets-be/creatingWorksheets")
from documentCreation import createVersions
import os

DATABASE = 'eagerSheets.db'
parser = reqparse.RequestParser()
parser.add_argument("data")

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

app = Flask(__name__)
CORS(app)
api = Api(app)

class Questions(Resource):
    def get(self):
        #Query for all that shit we need
        questions = query_db("SELECT * FROM questions")

        questionsDicts = []
        for q in questions:
            d = {}
            d["id"] = q[0]
            d["standard"] = q[1]
            d["skill"] = q[2]
            d["subSkill"] = q[3]
            d["topic"] = q[4]
            d["subTopic"] = q[5]
            d["notes"] = q[6]
            d["type"] = q[7]
            d["subject"] = q[8]

            #Get kwargs
            kwargs = query_db("SELECT * FROM questionsKwargs WHERE questionID=:id", {"id":d["id"]})

            #turn database return into kwargs from class structure
            #(id,key,value,toolTip) -> kwargs = {key1: bool, key2: [o1,o2]}
            newKwargs = {}
            for (i,row) in enumerate(kwargs):
                curKey = row[1]
                curValue = row[2]
                
                if curKey in newKwargs:
                    #Already a list
                    newKwargs[curKey].append(curValue)
                else:
                    newKwargs[curKey] = [curValue]

            #Change any kwargs that has options 1 and 0 to boolean
            for key in newKwargs:
                if len(newKwargs[key]) == 2 and "1" in newKwargs[key] and "0" in newKwargs[key]:
                    newKwargs[key] = [True, False]
                else:
                    #Check if all integers and change to integers or integers and a None
                    allIntegers = True
                    newVals = []
                    for val in newKwargs[key]:
                        try:
                            int(val)
                            newVals.append(int(val))
                        except:
                            if val is not None:
                                allIntegers = False
                            else:
                                newVals.append(val)

                    if allIntegers:
                        newKwargs[key] = newVals
                    


            #Add each combination of kwargs to questionDicts
            #Create all possible combinations from kwargs

            import itertools
            kwargs = newKwargs
            kwargsValues = []

            for key in kwargs:
                values = []
                if isinstance(kwargs[key], bool):
                    values.append(True)
                    values.append(False)
                elif isinstance(kwargs[key], list):
                    for item in kwargs[key]:
                        values.append(item)
                kwargsValues.append(values)
            
            combos = list(itertools.product(*kwargsValues))
            keys = [x for x in kwargs.keys()]

            for combo in combos:
                newQuestion = {**d}
                currentKwargs = {}
                filePath = f"{d['id']}"
                for key, value in zip(keys, combo):
                    currentKwargs[key] = value
                    filePath += f",{key}={value}"
                # print("kwargs for a question", currentKwargs)
                # print(filePath)
                newQuestion["kwargs"] = currentKwargs
                newQuestion["fileName"] = filePath
                questionsDicts.append(newQuestion)
        return questionsDicts

class CreateDocument(Resource):
    def post(self):    
        data = request.get_json()["data"]           
        document = data["document"]

        print(document["questions"])

        ids = [question["id"] for question in document["questions"]]
        kwargs = [question["kwargs"] for question in document["questions"]]

        #Path safe username and doc
        nameOfDoc = "".join([c for c in document["nameOfDoc"] if c.isalpha() or c.isdigit() or c==' ']).rstrip()

        #Testing BELOW
        documentOptions = {"ids": ids, "kwargs": kwargs, "nameOfDoc": nameOfDoc, "spacingBetween": document["spacingBetween"], "font":"Huge"}

        createVersions(documentOptions, collatedAnswerKey = document["collatedAnswerKey"], columns = document["columns"], numberOfVersions = document["numberOfVersions"])

        return nameOfDoc

class GetFile(Resource):
    def get(self, userID, nameOfDoc):
        #Path safe doc name
        nameOfDoc = "".join([c for c in nameOfDoc if c.isalpha() or c.isdigit() or c==' ']).rstrip()

        file = send_file(f"./creatingWorksheets/pdfs/{nameOfDoc}.pdf", download_name = f"{nameOfDoc}.pdf")
        
        # os.remove(f"./creatingWorksheets/pdfs/{nameOfDoc}.pdf")

        return file

#Get Questions from Eager Sheet DB
api.add_resource(Questions, "/questions")
api.add_resource(CreateDocument, "/createDocument")
api.add_resource(GetFile, "/getFile/<userID>/<nameOfDoc>")

"""
getQuestions
createDocument

probably something about a snippet


"""

if __name__ == '__main__':
    app.run(debug=True)