express = require("express");

app = express();


function hardWork() {
    j = 0;
    for (i = 0; i < 100000000; i++) {
        j = j + i*i;
    }
    return j;
}



app.all("/hard", (req, resp) => {resp.send("hardWork result is " + hardWork())});
app.all("/", (req, resp) => {
    console.log(req);
    resp.send("main handler");

});

app.listen(8080,() => console.log("start listening on port 8080"));