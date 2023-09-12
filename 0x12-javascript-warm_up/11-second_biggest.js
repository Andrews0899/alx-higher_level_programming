#!/usr/bin/node
const myList = process.argv.slice(2);
if (!myList.sort((a, b) => b - a)[1]) {
  console.log(0);
} else {
  console.log(myList.sort((a, b) => b - a)[1]);
}
