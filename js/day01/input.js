const path = require("path");
const fs = require("fs");

const input = fs
  .readFileSync(path.join(__dirname, "../../inputs/day01.txt"), "utf8")
  .toString()
  .trim()
  .split("\n\n");

module.exports = { input };

// console.log(input);
