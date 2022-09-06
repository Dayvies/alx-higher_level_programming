#!/usr/bin/node

const square = require('./5-square');

class Square extends square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let str = c;
    if (c === undefined) { str = 'X'; }
    const multiStr = str.repeat(this.width);
    for (let i = 0; i < this.height; i++) { console.log(multiStr); }
  }
}
module.exports = Square;
