#!/usr/bin/node

const process = require('process');
const args = process.argv;
function maxArr (arr) {
  let max = 0;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > arr[max]) {
      max = i;
    }
  }
  return max;
}

if (args.length < 4) { console.log(0); } else {
  const arr = [];
  for (let i = 2; i < args.length; i++) {
    const j = parseInt(args[i]);
    if (isNaN(j)) { continue; } else { arr.push(j); }
  }
  let x = maxArr(arr);
  arr.splice(x, 1);
  x = maxArr(arr);
  console.log(arr[x]);
}
