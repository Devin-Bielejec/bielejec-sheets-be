const router = require("express").Router();
const Questions = require("../questions/questions-model.js");
const restricted = require("../auth/restricted-middleware");
const fs = require("fs");

//restricted,
router.post("/createDocument", (req, res) => {
  //question ids
  let { nameOfDoc, ids } = req.body;

  console.log("req.body", req.body);

  if (!ids || !nameOfDoc) {
    res.status(400).json({ message: "You need to supply ids for questions!" });
    return;
  }

  spawnChild(JSON.stringify(req.body))
    .then(data => {
      res
        .status(200)
        .download(
          `./creatingWorksheets/pdfs/${nameOfDoc}.pdf`,
          `${nameOfDoc}.pdf`,
          err => {
            if (err) {
              console.log("download err", err);
            } else {
              //remove file
              fs.unlink(`./creatingWorksheets/pdfs/${nameOfDoc}.pdf`, function(
                err
              ) {
                if (err) throw err;
                //if no error, file has been deleted
                console.log("File Deleted");
              });
            }
          }
        );
    })
    .catch(err => {
      res.status(400).json({ message: `there was an error ${err}` });
    });
});

async function spawnChild(jsonObject) {
  const { spawn } = require("child_process");
  const child = spawn("python", [
    "./creatingWorksheets/createDocument.py",
    jsonObject
  ]);

  let data = "";
  for await (const chunk of child.stdout) {
    console.log("stdout chunk: " + chunk);
    data += chunk;
  }
  let error = "";
  for await (const chunk of child.stderr) {
    console.error("stderr chunk: " + chunk);
    error += chunk;
  }
  const exitCode = await new Promise((resolve, reject) => {
    child.on("close", resolve);
  });

  if (exitCode) {
    throw new Error(`subprocess error exit ${exitCode}, ${error}`);
  }
  return data;
}

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
