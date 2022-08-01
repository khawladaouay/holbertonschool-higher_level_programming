#!/usr/bin/node
function factorial (n) {
  if (!n) {
    return (1);
  } else {
    return ((n) * factorial(n - 1));
  }
}
const args = process.argv;
console.log(factorial(parseInt(args[2])));
