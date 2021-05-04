#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/people/18/';
request(url, function (error, response) {
  if (error) {
    return console.log(error);
  }
  const json = JSON.parse(response.body);
  console.log(json.films.length);
});
