#!/usr/bin/node

const dict = require('./101-data').dict;

const dict2 = {};
const keys = Object.keys(dict);
keys.forEach(
  function (number) {
    const arr = dict2[dict[number]];
    if (arr === undefined) { dict2[dict[number]] = []; }
    dict2[dict[number]].push(number);
  });
console.log(dict2);
