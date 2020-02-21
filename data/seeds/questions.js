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
  });

  return knex("questions")
    .del()
    .then(function() {
      // Inserts seed entries
      return knex("questions").insert([...questions]);
    });
};
