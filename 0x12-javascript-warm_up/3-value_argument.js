#!/usr/bin/node

const process = require('process');
const args = process.argv;

let count = 0;
args.forEach(function () { count = count + 1; }
);
if (count === 3) console.log(args[2]);
else if (count > 3) console.log(args[2]);
else console.log('No Argument');
