import sqlite3

db = sqlite3.connect('eagerSheets.db')

cur = db.cursor()

# # Create table
cur.execute('''CREATE TABLE questions
               (id int PRIMARY KEY, 
               standard text,
               primarySkill text,
               secondarySkill text,
               primaryTopic text,
               secondaryTopic text,
               notes text,
               type text,
               points int
               )''')

cur.execute('''CREATE TABLE questionsKwargs
               (
                   questionID int,
                   key text,
                   value text,
                   tooltip text,
                   FOREIGN KEY (questionID) REFERENCES questions(id)
               )''')

# # Insert a row of data
# cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# # Save (commit) the changes
db.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
db.close()