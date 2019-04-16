strict
var fs = require("fs");

var data = "New File Contents";
fs.writeFile("/temp.txt", data, console.log);
var result = fs.writeFileSync("temp1.txt", "1234");
console.log("result is", result);
