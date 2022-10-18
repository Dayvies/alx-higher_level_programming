#!/usr/bin/node
const process = require('process');
const args = process.argv;
const fs = require('fs');

try {
  fs.writeFileSync(args[2], args[3], { encoding: 'utf8' });
} catch (err) {
  console.log(err);
}
