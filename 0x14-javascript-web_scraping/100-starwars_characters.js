#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const content = JSON.parse(body);
  content.characters.forEach(function (item) {
    request(item, (error, response, body2) => {
      if (error) {
        console.log(error);
      }
      const cont = JSON.parse(body2);
      console.log(cont.name);
    });
  });
});
