#!/usr/bin/node

// imports a dictionary of occurrences by user id and computes
// a dictionary of user ids by occurrence

const dict = require('./101-data');

const usersByOccurrence = {};

for (const key in dict) {
  if (dict.hasOwnProperty(key)) {
    const occurrence = dict[key];
    if (!usersByOccurrence[occurrence]) {
      usersByOccurrence[occurrence] = [];
    }
    usersByOccurrence[occurrence].push(key);
  }
}

console.log(usersByOccurrence);
