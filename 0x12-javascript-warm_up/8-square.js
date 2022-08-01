#!/usr/bin/node
const args = process.argv;
let square = '';
if (!parseInt(args[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < args[2]; i++) {
    square += 'X';
  }
  for (let j = 0; j < args[2]; j++) {
    console.log(square);
  }
}
