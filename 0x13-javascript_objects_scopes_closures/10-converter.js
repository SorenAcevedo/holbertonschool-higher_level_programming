#!/usr/bin/node
exports.converter = function (base) {
  return function number (n) {
    return n.toString(base);
  };
};
