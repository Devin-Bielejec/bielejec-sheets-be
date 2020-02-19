exports.up = function(knex) {
  return knex.schema.createTable("topics", tbl => {
    tbl.string("id").primary();
    tbl.string("topic");
  });
};

exports.down = function(knex) {
  return knex.schema.dropTableIfExists("topics");
};
