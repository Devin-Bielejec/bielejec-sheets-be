const jwt = require("jsonwebtoken");

const secrets = require("../config/secrets.js");

module.exports = (req, res, next) => {
  const token = req.headers.authorization;
  console.log(req.headers);
  console.log(token);
  if (token) {
    jwt.verify(token, secrets.jwtSecret, (err, decodeToken) => {
      if (err) {
        res.status(401).json({ message: "You shall not pass!" });
      } else {
        req.user = {

        };
        next();
      }
    });
  } else {
    res.status(400).json({ message: "Please provide a token" });
  }
};
