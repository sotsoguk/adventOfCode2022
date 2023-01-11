const { input } = require("./input");
const day = 3;
const year = 2022;
// Split each line at the midpoint (Part 1)
let splitRucksack = (r) => {
  let midPoint = r.length / 2;
  let r1 = r.slice(0, midPoint),
    r2 = r.slice(midPoint).trim();
  return { r1, r2 };
};

// Find the one element common in both rucksacks
let findCommon = (rs) => {
  let { r1, r2 } = rs;
  let r1Set = new Set(r1);
  let r2Set = new Set(r2);
  return [...r1Set].filter((i) => r2Set.has(i))[0];
};

// Find the common element of each group (= three lines)
let findCommon3 = (a, b, c) => {
  let aSet = new Set(a),
    bSet = new Set(b),
    cSet = new Set(c);
  return [...aSet].filter((i) => bSet.has(i) && cSet.has(i))[0];
};

// Convert character to value (not equal to ASCII code)
let computeValue = (elem) => {
  if (elem == elem.toLowerCase()) {
    return elem.codePointAt() - 96;
  } else {
    return elem.codePointAt() - 38;
  }
};
// Part 1
let part1 = input
  .map(splitRucksack)
  .map(findCommon)
  .map(computeValue)
  .reduce((a, b) => a + b, 0);

// Part 2
let part2 = 0;
for (let i = 0; i < input.length; i += 3) {
  part2 += computeValue(findCommon3(input[i], input[i + 1], input[i + 2]));
}
console.log(
  `Advent of Code ${year} - Day ${String(day).padStart(2, "0")} \n${"#".repeat(
    28
  )}\nPart 1:\t${part1}\nPart 2:\t${part2}`
);
