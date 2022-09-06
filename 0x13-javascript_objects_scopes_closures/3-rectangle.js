#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 1 && h > 1) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const str = 'X';
    const multiStr = str.repeat(this.width);
    for (let i = 0; i < this.height; i++) { console.log(multiStr); }
  }
}
module.exports = Rectangle;
