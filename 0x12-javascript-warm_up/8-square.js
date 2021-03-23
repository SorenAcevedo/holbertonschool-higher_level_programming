#!/usr/bin/node
const first = process.argv[2];
let i;
if (isNaN(parseInt(first)) || first === undefined) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < process.argv[2]; i++) {
    console.log('X'.repeat(process.argv[2]));
  }
}
