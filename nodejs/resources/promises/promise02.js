const util = require('util');
let fs = require("fs");


fs.readFileAsync = util.promisify(fs.readFile);

fs.readFileAsync("1.txt")
    .then(data => data.toString())
    .then(console.log)
    .catch(console.error);