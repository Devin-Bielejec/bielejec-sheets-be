exports.up = function(knex) {
  return knex.schema.createTable("standards", tbl => {
    tbl.uuid("id").primary();
    tbl.string("standard");
  });
};

exports.down = function(knex) {
  return knex.schema.dropTableIfExists("standards");
};
