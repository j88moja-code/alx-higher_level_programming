#!/usr/bin/node
const list = process.argv;
const fs = require('fs');
let text = '';
try {
  text = fs.readFileSync(list[2], 'utf-8');
} catch (error) {
  console.log(error);
}
process.stdout.write(text);
