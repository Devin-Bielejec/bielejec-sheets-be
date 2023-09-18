from flask import Flask, g, request, send_file, send_from_directory
from flask_restful import Resource, Api, reqparse
from requests import put, get
import sqlite3
from flask_cors import CORS, cross_origin
import sys
sys.path.insert(0, "F:/code/bielejec-sheets-be/creatingWorksheets")
from documentCreation import createVersions
import os
from flask_login import LoginManager, login_required, login_user, logout_user, current_user, UserMixin

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
login_manager = LoginManager(app)

#Configure Flask-Login
login_manager.login_view = "login"
login_manager.refresh_token = True

#Configure Flask-CORS
CORS(app)

class User(UserMixin):
    def __init__(self, id, email, password):
         self.id = unicode(id)
         self.email = email
         self.password = password
         self.authenticated = False
    def is_active(self):
         return self.is_active()
    def is_anonymous(self):
         return False
    def is_authenticated(self):
         return self.authenticated
    def is_active(self):
         return True
    def get_id(self):
         return self.id

@login_manager.user_loader
def load_user(user_id):
   conn = sqlite3.connect('eagerSheets.db')
   curs = conn.cursor()
   curs.execute("SELECT * from login where id = (?)",[user_id])
   lu = curs.fetchone()
   if lu is None:
      return None
   else:
      return User(int(lu[0]), lu[1], lu[2])

@app.route("/auth/login", methods=['GET','POST'])
def login():
    print(request.data)
    username = request.data["username"]
    password = request.data["password"]
    if current_user.is_authenticated:
        return redirect(url_for('profile'))
    conn = sqlite3.connect('eagerSheets.db')
    curs = conn.cursor()
    curs.execute("SELECT * FROM login where email = (?)",    [email])
    user = list(curs.fetchone())
    Us = load_user(user[0])
    print(Us)
    if email == Us.email and password == Us.password:
        login_user(Us)
        Umail = list({form.email.data})[0].split('@')[0]
        flash('Logged in successfully '+Umail)
        redirect(url_for('profile'))
        return 
    else:
        flash('Login Unsuccessfull.')

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
    return questionsDicts

@app.route("/createDocument", methods=["POST"])
def CreateDocument(Resource):
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
def getImage():
    path = "".join([c for c in path if c.isalpha() or c.isdigit() or c==' ' or c == "=" or c == "," or c=="."]).rstrip()
    return send_from_directory('creatingWorksheets/images', path)

if __name__ == '__main__':
    app.run(debug=True)