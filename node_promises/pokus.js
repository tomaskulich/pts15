
var arr = [0, '', false, undefined, null, [], {}, NaN];

for(var i=0; i<arr.length; i++){
for(var j=0; j<arr.length; j++){
for(var k=0; k<arr.length; k++){
    if (arr[i]==arr[j] && arr[j]==arr[k] && !(arr[i] == arr[k])) {
        console.log(i);
        console.log(j);
        console.log(k);
    }
}
}
}
