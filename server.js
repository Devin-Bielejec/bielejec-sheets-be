const express = require("express");
const server = express();

const authRouter = require("./auth/auth-router.js");
const usersRouter = require("./users/users-router.js");

server.use(express.json());
server.use("/", authRouter);
server.use("/users", usersRouter);

//Testing child processes with Python
server.get("/name", callName);

function callName(req, res) {
  // Use child_process.spawn method from
  // child_process module and assign it
  // to variable spawn
  var spawn = require("child_process").spawn;

  test1 = "Chicken";
  test2 = "Tacos";
  var process = spawn("python", [
    "../bielejecSheets-python/hello.py",
    test1,
    test2
  ]);

  // Takes stdout data from script which executed
  // with arguments and send this data to res object
  process.stdout.on("data", function(data) {
    res.send(data.toString());
  });
}

//Make node send shit to python file, which creates a file, then send that file to the user through react
module.exports = server;
