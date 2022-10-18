#!/usr/bin/node
const process = require('process');
const request = require('request');
const args = process.argv;

const url = `https://swapi-api.hbtn.io/api/films/${args[2]}`;
request(url, function (error, response, body) {
  const content = JSON.parse(body);
  console.log(content.title);
});
