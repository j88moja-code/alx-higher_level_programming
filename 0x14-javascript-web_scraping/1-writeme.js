#!/usr/bin/node

const list = process.argv;
const fs = require('fs');
try {
  if (list[2] && list[3]) {
    fs.writeFileSync('./' + list[2], list[3]);
  }
} catch (error) {
  console.log(error);
}
