#!/usr/bin/node
const request = require('request');
let cont = 0;

request(process.argv[2], function (error, response) {
  if (error) {
    return console.log(error);
  }
  const json = JSON.parse(response.body).results;
  for (let i = 0; json[i]; i++) {
    for (let j = 0; json[i].characters[j]; j++) {
      if (json[i].characters[j].endsWith('18/')) { cont++; }
    }
  }
  console.log(cont);
});
