let a = "abcdFg";
let b = "huecXv";

let sa = new Set(a);
let sb = new Set(b);
// console.log(s2);

let intersection = [...sa].filter((i) => sb.has(i));

console.log(intersection);

for (let c of [...sa]) console.log(typeof c);

let ta1 = [2, 4, 5];
console.log([...ta1].filter((i) => i % 2 == 0));

// console.log(a.slice(0,2))

// let splitRucksack = r =>{
//     let midPoint = r.length / 2;
//     let r1 = r.slice(0,midPoint), r2 = r.slice(midPoint);
//     return {r1,r2};
// }

// console.log(splitRucksack(a));

console.log("A".codePointAt(0));

// console.log('A'.);

// console.log(Array.from({length:26},(_,i) =>0))

console.log("abc".charCodeAt(0));

let s2 = Array.from({ length: 26 }, (_, i) => 0);

s2[2] += 1;
console.log(s2);

let strtest = "abcd";
console.log(strtest[2]);

let display = Array.from(Array(6), () => Array.from({ length: 20 }, () => "."));
console.log(display);

console.log(11 / 4);

let lut = {"2":2,"1":1,"0":0};
console.log(lut["2"]);

let snafuToDecimal = (num) =>{
    let lut = {"2":2,"1":1,"0":0,"-":-1,"=":-2};
    let mult = 1, val = 0;
    for (let i = num.length -1 ;i>=0;i--){
        val += lut[num[i]]*mult;
        mult *= 5;
    }
    return val;
}

console.log(snafuToDecimal("2=0="));