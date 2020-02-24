const router = require("express").Router();
const secrets = require("../config/secrets.js");
const { spawn } = require("child_process");

function runPythonScript(name) {
  console.log(__dirname, name);
  let child = spawn("python", [
    "u",
    "./creatingWorksheets/createSingleImage.py",
    name
  ]);
}

runPythonScript("chicken");

module.exports = router;
