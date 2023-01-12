let { input } = require("./input");
const day = 25;
const year = 2022;
let part1 = 0;
let part2 = 0;

let snafuToDecimal = (num) => {
  let lut = { 2: 2, 1: 1, 0: 0, "-": -1, "=": -2 };
  let mult = 1,
    val = 0;
  for (let i = num.length - 1; i >= 0; i--) {
    val += lut[num[i]] * mult;
    mult *= 5;
  }
  return val;
};
let decimalToSnafu = (num) => {
  let lut = { 2: "2", 1: "1", 0: "0", "-1": "-", "-2": "=" };
  let result = "";
  let quotient = num;
  while (quotient > 0) {
    const rem = ((quotient + 2) % 5) - 2;
    quotient = Math.trunc((quotient + 2) / 5);
    result = lut[rem] + result;
  }
  return result;
};

part1 = decimalToSnafu(
  input
    .map((i) => i.trim())
    .map((n) => snafuToDecimal(n))
    .reduce((a, b) => a + b, 0)
);
console.log(
  `Advent of Code ${year} - Day ${String(day).padStart(2, "0")} \n${"#".repeat(
    28
  )}\nPart 1:\t${part1}\nPart 2:\t${part2}`
);
