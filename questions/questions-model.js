const db = require("../data/dbConfig.js");

const getByFilter = filter => {
  let query = db("questions")
    .join("topics", "questions.id", "=", "topics.id")
    .join("standards", "questions.id", "=", "standards.id")
    .join("subjects", "questions.id", "=", "subjects.id");

  for (let key in filter) {
    //if they come in empty
    console.log(key, filter);
    if (filter[key].length > 0) {
      query = query.whereIn(key, filter[key]);
    }
  }

  return query.select("questions.id", "questions.imgURL").distinct();
};

const getAll = () => {
  let query = db("questions")
    .join("topics", "questions.id", "=", "topics.id")
    .join("standards", "questions.id", "=", "standards.id")
    .join("subjects", "questions.id", "=", "subjects.id");

  return query.select("questions.id", "questions.imgURL").distinct();
};

const getSideBarByFilter = filter => {
  //so far
  let choices = ["standard", "topic", "type", "subject"];
  console.log("filter", filter);
  return db("questions")
    .join("topics", "questions.id", "=", "topics.id")
    .join("standards", "questions.id", "=", "standards.id")
    .join("subjects", "questions.id", "=", "subjects.id")
    .whereIn("subject", filter)
    .select(choices)
    .distinct();
};

//assuming no subject is selected, getting topics, standards, types of questions
const getSideBarDefaults = () => {
  //so far
  let choices = ["standard", "topic", "type", "subject"];

  return db("questions")
    .join("topics", "questions.id", "=", "topics.id")
    .join("standards", "questions.id", "=", "standards.id")
    .join("subjects", "questions.id", "=", "subjects.id")
    .select(choices)
    .distinct();
};

module.exports = {
  getByFilter,
  getSideBarByFilter,
  getSideBarDefaults,
  getAll
};
