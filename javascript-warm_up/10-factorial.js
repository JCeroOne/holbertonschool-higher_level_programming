#!/usr/bin/node
const n = process.argv[2];

function factorial (n) {
  if (isNaN(n)) return 1;
  return factorial(n - 1);
}

console.log(factorial(n));
