#!/usr/bin/node
const process = require('process');
const request = require('request');
const args = process.argv;

const url = args[2];
const id = 18;
request(url, function (error, response, body) {
  const content = JSON.parse(body);
  if (error) { console.log(error); }
  let count = 0;
  content.results.forEach(function (item) {
    const z = item.characters;
    z.forEach(function (item) {
      if (item.includes(id)) { count++; }
    });
  });
  console.log(count);
});
