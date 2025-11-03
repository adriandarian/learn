//
// Multiples of 3, 4, 7
//
// If we list all positive integers 10 or below that are multiples of 3, 4, or 7 we get: [3, 4, 6, 7, 8, 9]. The sum of the list is 37.
//
// Given a positive integer `n`, return the sum of all numbers less than or equal to `n` that are multiples of 3, 4, or 7.
//
// Example 1
//
// Input:
// n = 7
//
// Output:
// 20
//
// Explanation:
// The solution includes [3, 4, 6, 7] and its sum is 20.
//

class Solution {
    solve(n: number): number {
        let nums: Array<number> = [];

        for (let i: number = 5; i <= n; i++) {
            if (i % 3 === 0 || i % 4 === 0 || i % 7 === 0) {
                nums.push(i);
            }
        }

        return [3, 4, ...nums].reduce((acc: number, cur: number) => acc + cur);
    }
}

 export {};
