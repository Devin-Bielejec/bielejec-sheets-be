const router = require("express").Router();
const Questions = require("../questions/questions-model.js");

router.post("/questionsByFilter", (req, res) => {
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

module.exports = router;
