const db = require("../data/dbConfig.js");

const getByFilter = filter => {
  let query = db("questions")
    .join("topics", "questions.id", "=", "topics.id")
    .join("standards", "questions.id", "=", "standards.id")
    .join("subjects", "questions.id", "=", "subjects.id");

  for (let key in filter) {
    query = query.whereIn(key, filter[key]);
  }

  return query.select("questions.id").distinct();
};

module.exports = {
  getByFilter
};
