# bielejec-sheets-be

##Process

1. Create python classes in creatingWorksheets/questions
   -Make sure to add them to the most parent file (createDocument)
   -export a dictionary of the class (see other files for examples)

2. Knex
   -migrations should be good for a while, but don't mess up users
   -seeds get info from classes in updateDatabase.py file
   -seeds also add a property to link to storage of photo online

3. Image Storage online
   -createSnippets.py will create the snippets for a particular folder
   -then manually add those files (id's as names) to the google site
   -console.cloud.google.com
