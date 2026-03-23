#!/usr/bin/node
let args = [...process.argv];
args.splice(0, 2);
if (args.length < 2) {
  console.log(0);
} else {
  args.sort((a, b) => Number(b) - Number(a));
  console.log(args[1]);
}
