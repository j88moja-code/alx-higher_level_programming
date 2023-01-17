#!/usr/bin/node
const request = require('request');
const list = process.argv;
request(list[2], function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    console.log('code:', response.statusCode);
  }
});
