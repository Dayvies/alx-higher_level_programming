#!/usr/bin/node

const process = require('process');
const args = process.argv;
const numx = parseInt(args[2]);
if (isNaN(numx)) { console.log('Missing number of occurrences'); } else {
  for (let i = 0; i < numx; i++) { console.log('C is fun'); }
}
