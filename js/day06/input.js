const path = require("path");
const fs = require("fs");

const input = fs
  .readFileSync(path.join(__dirname, "../../inputs/day06.txt"), "utf8")
  // .readFileSync(path.join(__dirname, "../../inputs/day06_debug1.txt"), "utf8")
  .toString()
  .trim()
  .split("\n");

module.exports = { input };

// console.log(input);

let tmpArray = [1, 2, 3, 4, 5];
console.log(tmpArray.slice(-1));
