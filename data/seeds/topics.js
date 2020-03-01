exports.seed = function(knex) {
  const { spawn } = require("child_process");
  const child = spawn("python", [
    "./creatingWorksheets/updateDatabase.py",
    "id",
    "topics"
  ]);

  let topics;
  child.stdout.on("data", function(data) {
    topics = JSON.parse(data);
  });

  return knex("topics")
    .del()
    .then(function() {
      // Inserts seed entries
      return knex("topics").insert([...topics]);
    });
};
