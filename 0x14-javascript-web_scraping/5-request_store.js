#!/usr/bin/node
const request = require('request');
const fs = require('fs');

request(process.argv[2], function (error, response) {
  if (error) {
    return console.log(error);
  }
  fs.writeFile(process.argv[3], response.body, function (err) {
    if (err) {
      return console.log(err);
    }
  });
});
