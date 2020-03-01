const spawnChild = require("../utils/index.js");

exports.seed = function(knex) {
  let items;
  return spawnChild("id", "topics").then(data => {
    console.log("RES", data);
    items = JSON.parse(data);

    return knex("topics")
      .del()
      .then(function() {
        // Inserts seed entries
        return knex("topics").insert([...items]);
      });
  });
};
