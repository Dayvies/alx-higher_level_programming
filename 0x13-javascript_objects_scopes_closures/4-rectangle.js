#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    w = parseInt(w);
    h = parseInt(h);
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

  rotate () {
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
}
module.exports = Rectangle;
