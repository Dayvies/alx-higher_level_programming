#!/usr/bin/node
const process = require('process');
const args = process.argv;
const fs = require('fs');

try {
  const data = fs.readFileSync(args[2], 'utf8');
  console.log(data);
} catch (err) {
  console.log(err);
}
