#!/usr/bin/node

const process = require('process');
const args = process.argv;
const numx = parseInt(args[2]);
if (isNaN(numx)) { console.log('Missing size'); } else {
  const str = 'X';
  const multiStr = str.repeat(numx);
  for (let i = 0; i < numx; i++) { console.log(multiStr); }
}
