//
// Sum of the digits
//
// Given a positive integer num, return the sum of its digits.
//
// Bonus: Can you do it without using strings?
//
// Example 1
//
// Input:
// num = 123
//
// Output:
// 6
//
// Explanation:
// Since 6 = 1 + 2 + 3
//

class Solution {
    solve(num: number): number {
        return Array.from(String(num), Number).reduce((a, r) => a + r);
    }
}

 export {};
