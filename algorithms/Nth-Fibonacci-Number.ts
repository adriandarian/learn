//
// Nth Fibonacci Number
//
// The Fibonacci sequence goes like this: 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
//
// The next number can be found by adding up the two numbers before it, and the first two numbers are always 1.
//
// Write a function that takes an integer `n` and returns the `n`th Fibonacci number in the sequence.
//
// Note: `n` will be less than or equal to 30.
//
// Example 1
//
// Input:
// n = 1
//
// Output:
// 1
//
// Explanation:
// This is the base case and the first fibonacci number is defined as 1.
//
// Example 2
//
// Input:
// n = 6
//
// Output:
// 8
//
// Explanation:
// Since 8 is the 6th fibonacci number: 1, 1, 2, 3, 5, 8.
//
// Example 3
//
// Input:
// n = 7
//
// Output:
// 13
//
// Explanation:
// Since 13 is the seventh number: 1, 1, 2, 3, 5, 8, 13
//

class Solution {
    solve(n: number): number {
        const f: number[] = [];

        for (let i: number = 0; i < n; i++) {
            if (i === 0) {
                f.push(1);
            } else if (i === 1) {
                f.push(1);
            } else {
                f.push(f[i - 1] + f[i - 2]);
            }
        }

        return f[f.length - 1];
    }
}

 export {};
