const spawnChild = require("../utils/index.js");

exports.seed = function(knex) {
  let items;
  return spawnChild("id", "type").then(data => {
    console.log("RES", data);
    items = JSON.parse(data);
    items = items.map(item => {
      let copyItem = { ...item };
      copyItem.imgURL = `https://storage.googleapis.com/questions-images/${item.id}.jpg`;
      console.log(copyItem);
      return copyItem;
    });

    return knex("questions")
      .del()
      .then(function() {
        // Inserts seed entries
        return knex("questions").insert([...items]);
      });
  });
};
