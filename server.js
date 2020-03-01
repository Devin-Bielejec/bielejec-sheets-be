const express = require("express");
const server = express();
const cors = require("cors");

const authRouter = require("./auth/auth-router.js");
const usersRouter = require("./users/users-router.js");
const questionsRouter = require("./questions/questions-router.js");

server.use(cors());
server.use(express.json());
server.use("/", authRouter);
server.use("/users", usersRouter);
server.use("/questions", questionsRouter);

server.post("/getImage", (req, res) => {
  const name = req.body.name;
  if (!name) {
    res.status(400).json({ message: "You need to supply a name!" });
  }

  spawnChild(name)
    .then(data => {
      res.status(200).json({
        message: "Success",
        src: `./creatingWorksheets/${name}.jpg`
      });
    })
    .catch(err => {
      res.status(400).json({ message: `there was an error ${err}` });
    });
});

async function spawnChild(name) {
  const { spawn } = require("child_process");
  const child = spawn("python", [
    "./creatingWorksheets/createSingleImage.py",
    name
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

//Make node send shit to python file, which creates a file, then send that file to the user through react
module.exports = server;
