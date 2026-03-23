#!/usr/bin/node
let args = process.argv;

args.splice(0, 2).sort((a, b) => b - a);
console.log(args[1]);
