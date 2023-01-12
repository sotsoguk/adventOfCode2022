const path = require("path");
const fs = require("fs");

const input = fs
  .readFileSync(path.join(__dirname, "../../inputs/day04.txt"), "utf8")
//   .readFileSync(path.join(__dirname, "../../inputs/day04_debug.txt"), "utf8")
  .toString()
  .trim()
  .split("\n");

module.exports = { input };

// console.log(input);
