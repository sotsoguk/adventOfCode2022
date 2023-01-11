let a="abcdFg";
let b="huecXv";

let sa = new Set(a);
let sb = new Set(b);
// console.log(s2);

let intersection = [...sa].filter( i => sb.has(i))

console.log(intersection);

for (let c of [...sa]) console.log(typeof(c))

let ta1 = [2,4,5]
console.log([...ta1].filter(i=>i%2==0))



// console.log(a.slice(0,2))

// let splitRucksack = r =>{
//     let midPoint = r.length / 2;
//     let r1 = r.slice(0,midPoint), r2 = r.slice(midPoint);
//     return {r1,r2};
// }

// console.log(splitRucksack(a));

console.log('A'.codePointAt(0));

// console.log('A'.);