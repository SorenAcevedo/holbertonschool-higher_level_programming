#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const outputObj = {};
request(url, function (error, response) {
  if (error) {
    return console.log(error);
  }
  const json = JSON.parse(response.body);
  for (let i = 0; json[i]; i++) {
    if (outputObj[json[i].userId]) {
      if (json[i].completed === true) { outputObj[json[i].userId] += 1; }
    } else {
      if (json[i].completed === true) { outputObj[json[i].userId] = 1; }
    }
  }
  console.log(outputObj);
});
