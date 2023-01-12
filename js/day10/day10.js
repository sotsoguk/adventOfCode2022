let { input } = require("./input");
const day = 10;
const year = 2022;
let part1 = 0;
let part2 = 0;

function range(start, end, step = 1) {
  let result = [];
  if (step > 0) {
    for (let i = start; i < end; i += step) result.push(i);
  }
  if (step < 0) {
    for (let i = start; i > end; i += step) result.push(i);
  }
  return result;
}

// input = input[0].trim();
let commands = [];
for (let l of input) {
  tmp = l.trim().split(" ");
  if (tmp.length == 1) {
    commands.push({ op: 0, arg: 0 });
  } else {
    commands.push({ op: 1, arg: parseInt(tmp[1], 10) });
  }
}
// part 1
let registerValues = [1];

for (let { op, arg } of commands) {
  lastValue = registerValues.slice(-1)[0];
  registerValues.push(lastValue);
  if (op != 0) {
    registerValues.push(lastValue + arg);
  }
}
// console.log(registerValues)
for (let i of range(20, registerValues.length, (step = 40))) {
  part1 += registerValues[i - 1] * i;
}
// part2
let height = 6,
  width = 40;
let display = Array.from(Array(height), () =>
  Array.from({ length: width }, () => ".")
);
for (let i=0;i<height*width;i++){
    let row = ~~(i/width), col = i%width;
    if (Math.abs(col-registerValues[i])<=1){
        display[row][col] = '#';
    }
}
let output = display.map((line) => line.join()).join('\n');
console.log(
  `Advent of Code ${year} - Day ${String(day).padStart(2, "0")} \n${"#".repeat(
    28
  )}\nPart 1:\t${part1}\nPart 2:\t${part2}`
);
console.log(output);