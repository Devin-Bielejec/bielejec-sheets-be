from flask import Flask, g
from flask_restful import Resource, Api
from requests import put, get
import sqlite3

DATABASE = 'eagerSheets.db'

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

            #Get kwargs
            print(d["id"])
            kwargs = query_db("SELECT * FROM questionsKwargs WHERE questionID=:id", {"id":d["id"]})
            print(kwargs)
            d["kwargs"] = {}
            for row in kwargs:
                key = row[1]
                value = row[2]
                toolTip = row[3]
                if key in d["kwargs"]:
                    d["kwargs"][key].append({"value": value, "toolTip": toolTip})
                else:
                    d["kwargs"][key] = [{"value": value, "toolTip": toolTip}]
            
            questionsDicts.append(d)

        return questionsDicts

#Get Questions from Eager Sheet DB
api.add_resource(Questions, "/questions")


"""
getQuestions
createDocument

probably something about a snippet


"""

if __name__ == '__main__':
    app.run(debug=True)