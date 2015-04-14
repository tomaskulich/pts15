var Promise = require("bluebird");
var fs = require("fs");
Promise.promisifyAll(fs);

//getFromServer(data, 
//  function(res){
//      getFromServer(res, 
//        function(res){
//            getFromServer(data,
//                function(res){},
//                function(err){});
//
//        },
//        function(err){
//        });
//  },
//
//  function(err){
//      daco
//  });



function getFromServer(request){
    return Promise.delay(1000).then(
        function(_){
          if (request === 'zlezle') {
              throw new Error('mumu')
          } 
          return 'response ' + request;
        });
}

// var g = function(h){return function(x){return h(h(x))}}
// var inc2 = g(f);
// console.log(inc2(2));

//var f = function(x){return x+1}
//
//var p = Promise.delay(1000)
//  .then(function(_){ return 10;})
//  .then(f)
//  .then(function(res){console.log(res);});
//
//console.log(p);

//getFromServer('ahoj').then(function(result){
//  r1 = result;
//  console.log(result);
//  return getFromServer('svet');
//}).then(function(result){
//  r2 = result;
//  console.log(result);
//  return getFromServer('zlezle');
//}).then(function(result){
//  console.log('tuto sa asi nedostanem, ze');
//}).then(function(result){
//  console.log('tuto sa asi nedostanem, ze');
//}).catch(function(e){
//  console.log(e + ' caught. Keeping calm and carrying on');
//  return fs.readFileAsync('text.txt', 'utf8');
//}).then(function(result){
//  console.log(result);
//});

//timer = function(x){
//    return Promise.delay(100).then(function(_){ console.log(x); return timer(x+1)});
//}
//
//timer(0);
      
getFromServer('ahoj').then(function(result)  {
  console.log(result);
  return getFromServer('svet');
}).then(function(result)  {
  console.log(result);
  return getFromServer('zlezle');
}).then(function(result)  {
  console.log('tuto sa asi nedostanem, ze');
}).catch(function(e)  {
  console.log(e + ' caught. Keeping calm and carrying on');
  return fs.readFileAsync('text.txt', 'utf8');
}).then(function(result)  {
  console.log(result);
});
