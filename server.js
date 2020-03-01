const express = require("express");
const server = express();
const cors = require("cors");
const helmet = require("helmet");

const authRouter = require("./auth/auth-router.js");
const usersRouter = require("./users/users-router.js");
const questionsRouter = require("./questions/questions-router.js");

server.use(helmet());
server.use(cors());
server.use(express.json());
server.use("/", cors(), authRouter);
server.use("/users", cors(), usersRouter);
server.use("/questions", cors(), questionsRouter);

//Make node send shit to python file, which creates a file, then send that file to the user through react
module.exports = server;
