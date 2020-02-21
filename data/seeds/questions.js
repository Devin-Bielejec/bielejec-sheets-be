exports.seed = function(knex) {
  const { spawn } = require("child_process");
  const child = spawn("python", [
    "./creatingWorksheets/updateDatabase.py",
    "id"
  ]);

  let questions;
  child.stdout.on("data", function(data) {
    console.log(JSON.parse(data));
    questions = JSON.parse(data);
    // questions = JSON.parse(data.toString());
    // console.log(questions);
  });

  // Deletes ALL existing entries
  return knex("questions")
    .del()
    .then(function() {
      // Inserts seed entries
      return knex("questions").insert([...questions]);
    });
};
