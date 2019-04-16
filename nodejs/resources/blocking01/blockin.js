var http = require('http');
var fs = require('fs');

const handler = function (req, res) {
    data = fs.readFileSync('html.html');
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write(data);
    res.end();
    console.log("01 request processed!!!");
    console.log("02 finished");
    // var x = 1000000000000000000;
    // while (1 === 1) {
    //     x * x;
    // }
}

http.createServer(handler).listen(8080);