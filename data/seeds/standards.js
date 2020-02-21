exports.seed = function(knex) {
  const { spawn } = require("child_process");
  const child = spawn("python", [
    "./creatingWorksheets/updateDatabase.py",
    "id",
    "standards"
  ]);

  let standards;
  child.stdout.on("data", function(data) {
    standards = JSON.parse(data);
  });

  return knex("standards")
    .del()
    .then(function() {
      // Inserts seed entries
      return knex("standards").insert([...standards]);
    });
};
