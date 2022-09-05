#!/usr/bin/node

const process = require('process');
const args = process.argv;
const numx = parseInt(args[2]);
if (isNaN(numx)) { console.log('Not a number'); } else { console.log('My number: ' + numx); }
