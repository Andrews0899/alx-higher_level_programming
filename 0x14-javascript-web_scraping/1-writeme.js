#!/usr/bin/node
const fs = require('fs');
const filename = process.argv[2];
fs.writeFile(filename, process.argv[3], 'utf8', function (err, data) {
  if (err) return console.log(err);
});
