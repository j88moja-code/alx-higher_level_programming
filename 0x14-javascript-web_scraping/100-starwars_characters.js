#!/usr/bin/node
const list = process.argv;
const request = require('request');
request('https://swapi-api.alx-tools.com/api/films' + list[2], function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }
  let i = 0;
  const actors = JSON.parse(body).characters;
  for (i = 0; i < actors.length; i++) {
    request(actors[i], function (error, response, body) {
      if (error) {
        console.error('error:', error);
      }
      console.log(JSON.parse(body).name);
    });
  }
});
