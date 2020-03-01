exports.seed = function(knex) {
  const { spawn } = require("child_process");
  const child = spawn("python", [
    "./creatingWorksheets/updateDatabase.py",
    "id",
    "subject"
  ]);

  let subjects;
  child.stdout.on("data", function(data) {
    subjects = JSON.parse(data);
  });

  return knex("subjects")
    .del()
    .then(function() {
      // Inserts seed entries
      return knex("subjects").insert([...subjects]);
    });
};
