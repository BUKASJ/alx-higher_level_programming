#!/usr/bin/node

'use strict';

const [,, ...args] = process.argv;

if (args[0]) {
  console.log(args[0]);
} else {
  console.log('No argument');
}
