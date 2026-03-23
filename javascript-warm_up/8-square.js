#!/usr/bin/node
const arg = process.argv[2];

if (isNaN(arg)) {
  console.log('Missing size');
} else {
  for (let y = 0; y < Math.floor(arg); y++) {
    let str = "";
    for (let x = 0; x < Math.floor(arg); x++) {
      str += 'X';
    }
    console.log(str);
  }
}
