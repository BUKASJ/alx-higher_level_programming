#!/usr/bin/node
// script that prints My number

if (!isNaN(process.argv[2])) {
  console.log('My number: ' + parseInt(process.argv[2]));
} else {
  console.log('Not a number');
}
