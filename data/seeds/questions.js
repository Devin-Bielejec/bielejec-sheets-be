exports.seed = function(knex) {
  const { spawn } = require("child_process");
  const child = spawn("python", [
    "./creatingWorksheets/updateDatabase.py",
    "id",
    "type"
  ]);

  let questions;
  child.stdout.on("data", function(data) {
    questions = JSON.parse(data);
    //Add in imgURL
    questions = questions.map(question => {
      let copyQuestion = { ...question };

      copyQuestion.imgURL = `https://storage.googleapis.com/questions-images/${question.id}.jpg`;
      console.log(copyQuestion);
      return copyQuestion;
    });
  });

  return knex("questions")
    .del()
    .then(function() {
      // Inserts seed entries
      return knex("questions").insert([...questions]);
    });
};
