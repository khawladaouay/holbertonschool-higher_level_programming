#!/usr/bin/node
const args = process.argv;
let bignum = args[2];
if (args.length <= 3) {
  console.log(0);
} else {
  for (let i = 0; i < args.length; i++) {
    if (bignum < args[i]) {
      bignum = args[i];
    }
  }
  console.log(bignum);
}
