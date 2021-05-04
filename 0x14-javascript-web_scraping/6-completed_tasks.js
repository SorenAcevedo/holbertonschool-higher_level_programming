#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let output_obj = {};
request(url, function (error, response) {
  if (error) {
    return console.log(error);
  }
  const json = JSON.parse(response.body);
  console.log(json);
});
