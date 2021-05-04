#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/people/18/';
request(process.argv[2], function (error, response) {
  if (error) {
    return console.log(error);
  }
  const json = JSON.parse(response.body).results;
  let cont = 0;
  for (let i = 0; json[i]; i++) {
    for (let j = 0; json[i].characters[j]; j++) {
      if (json[i].characters[j] === url) { cont++; }
    }
  }
  console.log(cont);
});
