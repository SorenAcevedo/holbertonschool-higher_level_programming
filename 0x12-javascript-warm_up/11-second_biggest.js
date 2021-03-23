#!/usr/bin/node
const len = process.argv.length;
const max = Math.max(...process.argv.slice(2, len - 1));
let second = Math.min(...process.argv.slice(2, len - 1));
if (len <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < len; i++) {
    if (process.argv[i] > second && process.argv[i] < max) {
      second = process.argv[i];
    }
  }
  console.log(second);
}
