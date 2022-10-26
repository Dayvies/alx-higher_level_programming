#!/usr/bin/node
const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
$.getJSON(url, function (result) {
  $('#hello').text(result.hello);
});
