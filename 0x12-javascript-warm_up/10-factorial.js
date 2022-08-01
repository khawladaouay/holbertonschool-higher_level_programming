#!/usr/bin/node
function factorial (n) {
  if (n === 1) {
    return (1);
  } else {
    return parseInt(n) * parseInt(factorial(n - 1));
  }
}
const args = process.argv;
if (parseInt(args[2]) >= 200) {
  console.log('Infinity');
} else if (!parseInt(args[2])) {
  console.log(1);
} else {
  console.log(factorial(args[2]));
}
