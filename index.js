const server = require('./server');
const dotenv = require('dotenv').config();

const PORT = process.env.PORT || 4000;

server.listen(PORT, () => console.log(`WE ARE LISTENING ON PORT: ${PORT}!`))