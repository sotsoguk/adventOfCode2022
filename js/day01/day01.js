const { input } = require("./input");
const day = 1,
  year = 2022;

// Part 1
// The input is split on blank lines, so each element of the input array contains the lines of one elf.
// So in order to compute the sum of all lines they have to be split, converted to integers and summed up.
const sortedElves = input
  .map((e) => {
    return e
      .split("\n")
      .map((i) => parseInt(i, 10))
      .reduce((sum, curr) => sum + curr, 0);
  })
  .sort((a, b) => b - a);

let part1 = sortedElves[0];

// Part 2
// Just sum the first three elements, (no sum function, use reduce)
let part2 = sortedElves.slice(0, 3).reduce((a, b) => a + b, 0);

console.log(
  `Advent of Code ${year} - Day ${String(day).padStart(2, "0")} \n${"#".repeat(
    28
  )}\nPart 1:\t${part1}\nPart 2:\t${part2}`
);
