const router = require("express").Router();
const secrets = require("../config/secrets.js");
const spawn = require("child_process");

function runPythonScript(name) {
  console.log(__dirname, name);
  return spawn("python", [
    "u",
    "./creatingWorksheets/createSingleImage.py",
    name
  ]);
}

router.post("/getImage", (req, res) => {
  const name = req.body.name;
  console.log(name);
  if (!name) {
    res.status(400).json({ message: "You need to supply a name!" });
  }

  const process = runPythonScript(name);
  console.log("after process");
  // Takes stdout data from script which executed
  // with arguments and send this data to res object
  process.stdout.on("data", function(data) {
    console.log(data);
    console.log("DONEZO");
    res.status(200).json({
      message: "Success",
      src: `./creatingWorksheets/${name}.jpg`
    });
  });
});

module.exports = router;
