#!/usr/bin/node
const process = require('process');
const request = require('request');
const args = process.argv;

request(args[2], function (error, response, body) {
  console.log('code: ', response.statusCode);
});
