var Promise = require("bluebird");
var fs = require("fs");

Promise.promisifyAll(fs);

function getFromServer(request){
    return Promise.delay(1000).then(
        function(_){
          if (request === 'zlezle') {
              throw new Error('mumu')
          } 
          return 'response ' + request;
        });

}


getFromServer('ahoj').then(function(result){
  console.log(result);
  return getFromServer('svet');
}).then(function(result){
  console.log(result);
  return getFromServer('zlezle');
}).then(function(result){
  console.log('tuto sa asi nedostanem, ze');
}).catch(function(e){
  console.log(e + ' caught. Keeping calm and carrying on');
  return fs.readFileAsync('text.txt', 'utf8');
}).then(function(result){
  console.log(result);
});

      
