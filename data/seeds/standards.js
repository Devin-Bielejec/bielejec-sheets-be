const spawnChild = require("../utils/index.js");

exports.seed = function(knex) {
  let items;
  return spawnChild("id", "standards").then(data => {
    console.log("RES", data);
    items = JSON.parse(data);

    return knex("standards")
      .del()
      .then(function() {
        // Inserts seed entries
        return knex("standards").insert([...items]);
      });
  });
};
