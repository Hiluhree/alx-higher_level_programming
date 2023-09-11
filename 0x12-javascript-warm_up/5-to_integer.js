#!/usr/bin/node
const arg = process.argv[2];

if (!isNaN(parseInt(arg))) {
  const number = parseInt(arg);
  console.log(`My number: ${number}`);
} else {
  console.log("Not a number");
}
