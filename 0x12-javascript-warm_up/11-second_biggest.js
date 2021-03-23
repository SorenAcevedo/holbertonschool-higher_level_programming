#!/usr/bin/node
const len = process.argv.length;
const arr = process.argv.slice(2, len).sort();
if (len <= 3) {
  console.log(0);
} else {
  console.log(arr[len - 4]);
}
