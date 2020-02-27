const router = require("express").Router();
const Questions = require("../questions/questions-model.js");

router.post("/questionsByFilter", (req, res) => {
  console.log(req.body);
  let changes = req.body;

  //ensure that user is sending only correct column names
  let correctColumns = ["topic", "subject", "standard", "type"];

  for (let key in changes) {
    //removes selected and value properties
    changes[key] = changes[key]
      .filter(item => item.selected)
      .map(item => item.value);
    if (!correctColumns.includes(key) || !Array.isArray(changes[key])) {
      res.status(404).json({
        message:
          "You need to include 'topic: [stuff]', 'subject: [stuff]', 'standard: [stuff]', or 'type: [stuff]'"
      });
    }
  }

  console.log(changes);

  Questions.getByFilter(changes)
    .then(data => {
      if (data) {
        res.status(200).json({ displayedQuestions: data });
      } else {
        res.status(404).json({ message: "No information matching those!" });
      }
    })
    .catch(err => {
      res.status(500).json({ message: "Database error", error: err });
    });
});

router.post("/defaultQuestions", (req, res) => {
  Questions.getAll()
    .then(data => {
      if (data) {
        res.status(200).json({ displayedQuestions: data });
      } else {
        res.status(404).json({ message: "No information matching those!" });
      }
    })
    .catch(err => {
      res.status(500).json({ message: "Database error", error: err });
    });
});

router.post("/sideBarBySubjects", (req, res) => {
  const { subjects } = req.body;
  console.log(subjects);
  if (subjects === null) {
    res.status(404).json({
      message: "You need to include a [subject]"
    });
  }

  if (subjects.length > 0) {
    Questions.getSideBarByFilter(subjects)
      .then(data => {
        console.log(data);
        if (data) {
          res.status(200).json(data);
        } else {
          res.status(404).json({ message: "Error occured!" });
        }
      })
      .catch(err => res.status(500).json({ message: `Database Error ${err}` }));
  } else {
    Questions.getSideBarDefaults()
      .then(data => {
        //get topics etc
        //set removes duplicates
        //next mapping: creates objects for Front End
        let topics = new Set(data.map(item => item.topic));
        topics = [...topics].map(item => {
          return { value: item, selected: false };
        });

        let standards = new Set(data.map(item => item.standard));
        standards = [...standards].map(item => {
          return { value: item, selected: false };
        });

        let types = new Set(data.map(item => item.type));
        types = [...types].map(item => {
          return { value: item, selected: false };
        });

        let subjects = new Set(data.map(item => item.subject));
        subjects = [...subjects].map(item => {
          return { value: item, selected: false };
        });

        if (data) {
          res.status(200).json({
            topics: topics,
            standards: standards,
            types: types,
            subjects: subjects
          });
        } else {
          res.status(404).json({ message: "Error occured!" });
        }
      })
      .catch(err => res.status(500).json({ message: `Database Error ${err}` }));
  }
});

module.exports = router;
