from flask import Flask, g, request, send_file, send_from_directory, Response, jsonify
from flask_restful import Resource, Api, reqparse
from requests import put, get
import sqlite3
import sys
sys.path.insert(0, "./creatingWorksheets")
from documentCreation import createVersions
import os
import json
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_bcrypt import Bcrypt
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()
import pprint
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/test", methods = ["GET"])
def helloWorld():
    return "<p>hello world<p>"

bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")
app.config["JWT_ALGORITHM"] = "HS256" 
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

client = MongoClient(os.environ.get("MONGO_URI"))

db = client["bielejecSheets"]

# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
@app.route("/login", methods=["POST"])
def login():
    email = request.json.get("email", None)
    password = request.json.get("password", None)

    passwordHash = bcrypt.generate_password_hash(password).decode('utf-8') 
    #Check if email already exists in db and is valid
    if not db.users.find_one({"email":email}):
        return jsonify({"msg": "Bad email or password"}), 401

    #Check if hash from db doesn't match with current password given
    hashFromDB = db.users.find_one({"email": email})["password"]
    if not bcrypt.check_password_hash(passwordHash, hashFromDB):
        return jsonify({"msg": "Bad email or password"}), 401

    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token)

@app.route("/register", methods=["POST"])
def register():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    passwordHash = bcrypt.generate_password_hash(password).decode('utf-8') 
    #Check if email is already taken
    if not db.users.find_one({"email": email}):
        db.users.insert_one({"email": email, "password": passwordHash}).inserted_id
        access_token = create_access_token(identity=email)
        return jsonify(access_token=access_token)
    else:
        return jsonify({"msg": "Email already exists"}), 401



@app.route("/questions", methods=["GET"])
def getQuestions():
    #Query for all that we need
    f = open('./creatingWorksheets/questions.json')
    data = json.load(f)
    questions = []
    for i in data:
        questions.append(data[i])

    questionsDicts = []
    for d in questions:
        f = open('./creatingWorksheets/questionsKwargs.json')
        kwargs = json.load(f)
        #Get kwargs by id
        kwargs = [item for item in kwargs if item["questionID"] == d["id"]]

        #turn database return into kwargs from class structure
        #(id,key,value,toolTip) -> kwargs = {key1: bool, key2: [o1,o2]}
        newKwargs = {}
        for (i,k) in enumerate(kwargs):
            curKey = k["key"]
            curValue = k["value"]
            
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
    data = request.get_json()["data"]           

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