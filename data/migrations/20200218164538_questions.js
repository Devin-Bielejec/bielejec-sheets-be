exports.up = function(knex) {
  return knex.schema.createTable("questions", tbl => {
    tbl.string("id");
    tbl.string("type");
    tbl.string("imgURL");
  });
};

exports.down = function(knex) {
  return knex.schema.dropTableIfExists("questions");
};
