
exports.seed = function(knex) {
  // Deletes ALL existing entries
  return knex('users').del()
    .then(function () {
      // Inserts seed entries
      return knex('users').insert([
        {id: 1, username: "Devin", password: "Devin", age: 14, subscription: true, name: "Devin"}
      ]);
    });
};
