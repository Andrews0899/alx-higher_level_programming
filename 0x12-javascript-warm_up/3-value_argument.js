#!/usr/bin/node
const myArgs = process.argv.slice(2);
if (!process.argv[2]) {
  console.log('No argument');
} else {
  console.log(myArgs[0]);
}
