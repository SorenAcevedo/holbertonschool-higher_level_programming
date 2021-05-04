#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
request(url + process.argv[2], function (error, response) {
  if (error) {
    return console.log(error);
  }
  const json = JSON.parse(response.body);
  console.log(json.title);
});
