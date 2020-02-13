/* 
a) incrementing id 
b) username unique notNull
c) password notNull
d) name [optional]
e) age integer [optional]
f) subscription bool [optional] - default to false
*/ 

exports.up = function(knex) {
    return knex.schema.createTable("users", tbl => {
        tbl.increments();
        tbl.string("username").notNullable().unique();
        tbl.string("password").notNullable();
        tbl.string("name");
        tbl.integer("age");
        tbl.boolean("subscription").defaultTo(false)
    });
};

exports.down = function(knex) {
    return knex.schema.dropTableIfExists("users");
};
