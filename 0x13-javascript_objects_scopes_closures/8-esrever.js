#!/usr/bin/node

exports.esrever = function (list) {
  const arr = [];

  while (list.length > 0) {
    arr.push(list.pop());
  }
  return arr;
};
