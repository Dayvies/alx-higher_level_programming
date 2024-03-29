#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
const dict = {};
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const content = JSON.parse(body);
  content.forEach(function (item) {
    if (item.completed === true) {
      if (item.userId in dict) { dict[item.userId] += 1; } else { dict[item.userId] = 1; }
    }
  });
  console.log(dict);
});
