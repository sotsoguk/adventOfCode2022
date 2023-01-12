let { input } = require("./input");
const day = 6;
const year = 2022;
let part1 = 0;
let part2 = 0;

input = input[0].trim();

// part 1
// use an array as alternative for a hashmap to store the current 4 characters ([0] = a,...[25] = z)
let charToIdx = (c) => {
  return c.codePointAt(0) - 97;
};

let exactlyNOnes = (array, n) => {
  return array.every((i) => i <= 1) && array.reduce((a, b) => a + b, 0) == n;
};

let findStartMarker = (sequence, len) => {
  let seen = Array.from({ length: 26 }, (_, i) => 0);
  let marker = 0;
  for (let i = 0; i < sequence.length; i++) {
    // remove the old character
    if (i > len - 1) seen[charToIdx(sequence[i - len])] -= 1;
    seen[charToIdx(sequence[i])] += 1;
    //   console.log(i,input[i],seen)
    if (exactlyNOnes(seen, len)) {
      marker = i + 1;
      break;
    }
  }
  return marker;
};

part1 = findStartMarker(input, 4);
part2 = findStartMarker(input, 14);

console.log(
  `Advent of Code ${year} - Day ${String(day).padStart(2, "0")} \n${"#".repeat(
    28
  )}\nPart 1:\t${part1}\nPart 2:\t${part2}`
);

