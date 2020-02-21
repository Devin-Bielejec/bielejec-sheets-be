exports.up = function(knex) {
  return knex.schema.createTable("topics", tbl => {
    tbl.string("id");
    tbl.string("topic");
  });
};

exports.down = function(knex) {
  return knex.schema.dropTableIfExists("topics");
};
