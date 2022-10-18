#!/usr/bin/node
const process = require('process');
const request = require('request');
const args = process.argv;

const url = args[2];
request(url, function (error, response, body) {
  const content = JSON.parse(body);
  if (error) { console.log(error); }
  let count = 0;
  content.results.forEach(function (item) {
    const z = item.characters;
    if (z.includes('https://swapi-api.hbtn.io/api/people/18/')) {
      count += 1;
    }
  });
  console.log(count);
});
