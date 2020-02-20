exports.up = function(knex) {
  return knex.schema.createTable("topics", tbl => {
    tbl.uuid("id").primary();
    tbl.string("topic");
  });
};

exports.down = function(knex) {
  return knex.schema.dropTableIfExists("topics");
};
