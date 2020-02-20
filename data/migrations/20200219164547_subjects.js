exports.up = function(knex) {
  return knex.schema.createTable("subjects", tbl => {
    tbl.uuid("id").primary();
    tbl.string("subject");
  });
};

exports.down = function(knex) {
  return knex.schema.dropTableIfExists("subjects");
};
