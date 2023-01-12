const { input } = require("./input");
const day = 4;
const year = 2022;
let part1 = 0;
let part2 = 0;


let parseInput = (arr) => {
  return arr
    .trim()
    .split(",")
    .map((s) => s.split(`-`).map((i) => parseInt(i, 10)))
    .flat();
};

let containEachOther = ([x1,y1,x2,y2]) => {
  return (x1 >= x2 && y1 <= y2) || (x2 >= x1 && y2 <= y1);
};

// in order to check if two ranges overlap, it is easier to test for NOT overlapping.
// looking at the data, we can safely assume x1<=y1 && x2 << y2
let overlap = ([x1,y1,x2,y2]) => {
    return !(y2<x1 || y1<x2);
}

part1 = input
  .map((l) => parseInput(l))
  .filter((l) => containEachOther(l)).length;

part2 = input
  .map((l) => parseInput(l))
  .filter((l) => overlap(l)).length;

console.log(
  `Advent of Code ${year} - Day ${String(day).padStart(2, "0")} \n${"#".repeat(
    28
  )}\nPart 1:\t${part1}\nPart 2:\t${part2}`
);
