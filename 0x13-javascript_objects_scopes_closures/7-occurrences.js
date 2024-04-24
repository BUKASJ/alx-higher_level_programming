#!/usr/bin/node

// returns the number of occurrences in a list

exports.nbOccurences = function (list, searchElement) {
  return (list.filter(e => e === searchElement).length);
};
