#!/usr/bin/node

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (typeof c !== 'undefined') {
      let string = '';
      for (let i = 0; i < this.width; i++) { string += c; }
      for (let i = 0; i < this.height; i++) {
        console.log(string);
      }
    } else {
      let string = '';
      for (let i = 0; i < this.width; i++) { string += 'X'; }
      for (let i = 0; i < this.height; i++) {
        console.log(string);
      }
    }
  }
};
