#!/usr/bin/node
const request = require('request');

const dict = {};
let chars = [];
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const content = JSON.parse(body);

  chars = content.characters;
  let count = 0;
  content.characters.forEach(function (item) {
    request(item, (error, response, body2) => {
      if (error) {
        console.log(error);
      }
      const cont = JSON.parse(body2);
      dict[item] = cont.name;
      count += 1;
      if (count === chars.length) {
        chars.forEach(function (item) {
          console.log(dict[item]);
        });
      }
    });
  });
});
