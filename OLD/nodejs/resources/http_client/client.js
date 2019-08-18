const http_client = require("request");


http_client('http://localhost:8080/', {}, function (err, res, body) {
    if (err) { return console.log(err); }
    console.log(body.url);
    console.log(body);
});