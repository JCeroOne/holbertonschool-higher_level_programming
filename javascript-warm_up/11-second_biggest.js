#!/usr/bin/node
const args = process.argv.splice(0, 2);

args.sort((a, b) => a - b);
console.log(args[1]);
