from flask import Flask, g, request, send_file, send_from_directory, Response, jsonify
from flask_restful import Resource, Api, reqparse
from requests import put, get
import sqlite3
from flask_cors import CORS, cross_origin
import sys
sys.path.insert(0, "F:/code/bielejec-sheets-be/creatingWorksheets")
from documentCreation import createVersions
import os
import json
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_bcrypt import Bcrypt

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
#Configure Flask-CORS
cors = CORS(app, resources={r'/*' : {"origins": ["http://localhost:3000", "https://bielejec-sheets-fe.vercel.app"]}})
app.config['CORS_HEADERS'] = 'Content-Type'


bcrypt = Bcrypt(app)

# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "super secret"
app.config["JWT_ALGORITHM"] = "HS256" 
jwt = JWTManager(app)

# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
@app.route("/login", methods=["POST"])
def login():
    email = request.json.get("email", None)
    password = request.json.get("password", None)

    passwordHash = bcrypt.generate_password_hash(password).decode('utf-8') 
    isValid = bcrypt.check_password_hash(passwordHash, password)
    print(email,passwordHash)
    if not isValid or not query_db(f"SELECT email from login where email='{email}'"):
        return jsonify({"msg": "Bad email or password"}), 401
    
    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token)

@app.route("/register", methods=["POST"])
def register():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    passwordHash = bcrypt.generate_password_hash(password).decode('utf-8') 
    if not query_db(f"SELECT email from login where email='{email}'"):
        query_db(f"INSERT into login(email,password) VALUES('{email}','{passwordHash}')")
        get_db().commit()
        get_db().close()
        access_token = create_access_token(identity=email)
        return jsonify(access_token=access_token)
    else:
        return jsonify({msg: "Email already exists"}), 401

@app.route("/questions", methods=["GET"])
def getQuestions():
    #Query for all that we need
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
    return jsonify(questionsDicts)


@app.route("/createDocument", methods=["POST"])
@jwt_required()
def CreateDocument():
    print('inside createoducment')

    data = request.get_json()["data"]           
    print(data, request)
    document = data["document"]

    ids = [question["id"] for question in document["questions"]]
    kwargs = [question["kwargs"] for question in document["questions"]]

    #Path safe username and doc
    nameOfDoc = "".join([c for c in document["nameOfDoc"] if c.isalpha() or c.isdigit() or c==' ']).rstrip()

    #Testing BELOW
    documentOptions = {"ids": ids, "kwargs": kwargs, "nameOfDoc": nameOfDoc, "spacingBetween": document["spacingBetween"], "font":"Huge"}

    createVersions(documentOptions, collatedAnswerKey = document["collatedAnswerKey"], columns = document["columns"], numberOfVersions = document["numberOfVersions"])

    return nameOfDoc

@app.route("/getFile/<userID>/<nameOfDoc>", methods=["GET"])
def getFile(userID, nameOfDoc):
    #Path safe doc name
    nameOfDoc = "".join([c for c in nameOfDoc if c.isalpha() or c.isdigit() or c==' ']).rstrip()

    file = send_file(f"./creatingWorksheets/pdfs/{nameOfDoc}.pdf", download_name = f"{nameOfDoc}.pdf")
    
    # os.remove(f"./creatingWorksheets/pdfs/{nameOfDoc}.pdf")

    return file

@app.route("/<path>", methods=["GET"])
def getImage(path):
    path = "".join([c for c in path if c.isalpha() or c.isdigit() or c==' ' or c == "=" or c == "," or c=="."]).rstrip()
    return send_from_directory('creatingWorksheets/images', path)

if __name__ == '__main__':
    app.run(debug=True)