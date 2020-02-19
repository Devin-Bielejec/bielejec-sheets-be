exports.up = function(knex) {
  return knex.schema.createTable("questions", tbl => {
    tbl.string("id").primary();
  });
};

exports.down = function(knex) {
  return knex.schema.dropTableIfExists("questions");
};
