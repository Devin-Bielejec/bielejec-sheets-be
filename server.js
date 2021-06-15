const express = require("express");
const server = express();
const cors = require("cors");
const helmet = require("helmet");

const authRouter = require("./auth/auth-router.js");
const usersRouter = require("./users/users-router.js");

server.use(cors());
server.use(helmet());
server.use(express.json());
server.use("/auth", authRouter);
server.use("/users", usersRouter);

//Make node send shit to python file, which creates a file, then send that file to the user through react
module.exports = server;
