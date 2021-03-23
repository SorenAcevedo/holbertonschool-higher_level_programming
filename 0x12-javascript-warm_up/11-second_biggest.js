#!/usr/bin/node
const len = process.argv.length;
const max = Math.max(...process.argv.slice(2, len));
let second = Math.min(...process.argv.slice(2, len));
if (len <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < len; i++) {
    if (parseInt(process.argv[i]) >= second && parseInt(process.argv[i]) < max) {
      second = parseInt(process.argv[i]);
    }
  }
  console.log(second);
}
