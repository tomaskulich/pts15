var Promise = require("bluebird");
var fs = require("fs");

Promise.promisifyAll(fs);

var p = Promise.delay(0)
.then(function(result){ throw Error();});


Promise.delay(3)
.then(function(result){
  p.catch(function(result){
    console.log('cought');
  });
});

console.log(p);
Promise.delay(10000);

