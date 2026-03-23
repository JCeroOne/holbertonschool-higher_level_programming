#!/usr/bin/node
let args = process.argv;

args.splice(0, 2).sort((a, b) => Number(b) - Number(a));
console.log(args[1]);
