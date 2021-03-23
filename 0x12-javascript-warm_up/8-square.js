#!/usr/bin/node
const first = process.argv[2];
if (isNaN(first)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < first; i++) {
    console.log('X'.repeat(first));
  }
}
