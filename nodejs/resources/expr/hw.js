const express = require('express');
const app = express();
const util = require("util");

const port = 8080;
const all_handler = require("./all_handler");


app.get('/', function (req, res) {
    res.send('Hello World!');
});

app.all("/all-requests", all_handler);



app.listen(port, function () {
    console.log(util.format('Example app listening on port%s', port));
});