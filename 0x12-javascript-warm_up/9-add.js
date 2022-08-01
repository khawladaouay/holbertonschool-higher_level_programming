#!/usr/bin/node
function add (a, b) {
  let sum = 0;
  sum = parseInt(a) + parseInt(b);
  console.log(sum);
}
const args = process.argv;

if (!parseInt(args[2]) || !parseInt(args[3])) {
  console.log('NaN');
} else {
  add(args[2], args[3]);
}
