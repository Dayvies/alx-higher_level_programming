#!/usr/bin/node

const process = require('process');
const args = process.argv;
function add (a, b) {
  return a + b;
}
const numx = parseInt(args[2]);
const numy = parseInt(args[3]);

console.log(add(numx, numy));
