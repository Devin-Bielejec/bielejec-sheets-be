const router = require("express").Router();
const Questions = require("../questions/questions-model.js");

router.post("/questionsByFilter", (req, res) => {
  console.log(req.body);
  const changes = req.body;

  //ensure that user is sending only correct column names
  let correctColumns = ["topic", "subject", "standard", "type"];

  for (let key in changes) {
    if (!correctColumns.includes(key) || !Array.isArray(changes[key])) {
      res.status(404).json({
        message:
          "You need to include 'topic: [stuff]', 'subject: [stuff]', 'standard: [stuff]', or 'type: [stuff]'"
      });
    }
  }

  Questions.getByFilter(changes)
    .then(data => {
      if (data) {
        res.status(200).json({ data });
      } else {
        res.status(404).json({ message: "No information matching those!" });
      }
    })
    .catch(err => {
      res.status(500).json({ message: "Database error", error: err });
    });
});

router.post("/sideBarBySubject", (req, res) => {
  const subjects = req.body;

  if (subjects.length === 0) {
    res.status(404).json({
      message: "You need to include a [subject]"
    });
  }

  Questions.getListOfByFilter("topic", subjects)
    .then(topicData => {
      Questions.getListOfByFilter("standard", subjects).then(standardData => {
        Questions.getListOfByFilter("type", subjects).then(typeData => {
          const topics = topicData.map(currentTopic => currentTopic.topic);
          const standards = standardData.map(
            currentStandard => currentStandard.standard
          );
          const types = typeData.map(currentType => currentType.type);

          if (topics.length > 0 || standards.length > 0 || types.length > 0) {
            res
              .status(200)
              .json({ topics: topics, standards: standards, types: types });
          } else {
            res.status(404).json({ message: "Error occured!" });
          }
        });
      });
    })
    .catch(err => res.status(500).json({ message: `Database Error ${err}` }));
});

module.exports = router;
