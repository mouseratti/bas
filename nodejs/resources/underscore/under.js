const fs = require("fs");

const a = 'ffffffffffffffffffffffffffffffffffffffffff';

const _ = require("underscore");
const l1 = [1,2,3 ]

_.each(l1, function (elem, index, list) {
    console.log(elem);

});

l2 = _.map([1,2,3], x => x*2);

console.log(l2);
