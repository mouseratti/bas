const { fork } = require('child_process');

const express = require("express");

app = express();


function hardWork() {
    j = 0;
    for (i = 0; i < 100000000; i++) {
        j = j + i*i;
    }
    return j;
}



app.all("/hard", (req, resp) => {
    const hardWork = fork("./hard_work.js");
    hardWork.send(1000000000);
    hardWork.on("message", message => resp.send("hardWork result is " + message));
});

app.all("/", (req, resp) => {
    resp.send("main handler");

});

app.listen(8080,() => console.log("start listening on port 8080"));