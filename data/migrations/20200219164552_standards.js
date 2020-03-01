exports.up = function(knex) {
  return knex.schema.createTable("standards", tbl => {
    tbl.string("id");
    tbl.string("standard");
  });
};

exports.down = function(knex) {
  return knex.schema.dropTableIfExists("standards");
};
