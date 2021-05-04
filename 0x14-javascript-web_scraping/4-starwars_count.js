#!/usr/bin/node
const request = require('request');
const urlRequest = 'https://swapi-api.hbtn.io/api/films/';
let cont = 0;

request(urlRequest, function (error, response) {
  if (error) {
    return console.log(error);
  }
  const json = JSON.parse(response.body);
  for (let i = 0; json.results[i]; i++) {
    for (let j = 0; json.results[i].characters[j]; j++) {
      if (json.results[i].characters[j].endsWith('18/')) { cont++; }
    }
  }
  console.log(cont);
});
