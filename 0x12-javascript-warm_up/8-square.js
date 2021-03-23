#!/usr/bin/node
const first = process.argv[2];
let i;
if (isNaN(parseInt(first)) || first === undefined) {
  console.log('Missing size');
} else {
  for (i = 0; i < first; i++) {
    console.log('X'.repeat(first));
  }
}
