const spawnChild = require("../utils/index.js");

exports.seed = function(knex) {
  let items;
  return spawnChild("id", "subject").then(data => {
    console.log("RES", data);
    items = JSON.parse(data);

    return knex("subjects")
      .del()
      .then(function() {
        // Inserts seed entries
        return knex("subjects").insert([...items]);
      });
  });
};
