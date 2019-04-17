const fs = require("fs");


var promise = new Promise((resolve, reject) => {
    fs.readFile("1.txt" , (err, data) => {if (!!err) {reject(err)}; resolve(data)})
    });


promise
    .then(data => data.toString())
    .then(console.log)
    .catch(error => console.error("err!!!", error));

setTimeout(function () {
    console.log("timed out!!!");
}, 5000);


p2 = new Promise(function (resolve) {
    setTimeout(resolve, 1000)
});

p2.then(() => console.log("p2 timed out!!"));



promisedTimeout = function (number) {
    return new Promise(resolve => setTimeout(resolve, number));
};

promisedTimeout(3000).then(() => console.log("promisedTimeout timed out!!!"));