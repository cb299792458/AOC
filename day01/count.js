console.log('Counting the Calories');

const fs = require('fs');

const allFileContents = fs.readFileSync('input.txt', 'utf-8');

const arr = [];
// allFileContents.split(/\r?\n/).forEach(line =>  {
//   console.log(`Line from file: ${line}`);
// });

console.log(allFileContents.split(/\r?\n/))
let temp = [];
let max = 0;
for(let str of allFileContents.split(/\r?\n/)){
    if(str){
        temp.push(parseInt(str));
    } else {
        let sum = temp.reduce((a,c)=>a+c)
        max = Math.max(max,sum);


        arr.push(temp);
        temp = [];
    }
}
console.log(max)