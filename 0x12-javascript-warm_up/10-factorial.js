#!/usr/bin/node

const process = require('process');
const args = process.argv;
function factorial (num) {
  if (isNaN(num) || num === 0) { return 1; } else { return num * factorial(num - 1); }
}
const numx = parseInt(args[2]);
const z = factorial(numx);

console.log(z);
