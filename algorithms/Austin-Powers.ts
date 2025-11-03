//
// Austin Powers
//
// Given an integer n greater than or equal to 0, return whether it is a power of two.
//
// Example 1
//
// Input:
// n = 0
//
// Output:
// false
//
// Example 2
//
// Input:
// n = 1
//
// Output:
// true
//
// Explanation:
// 2^0 = 1
//
// Example 3
//
// Input:
// n = 2
//
// Output:
// true
//
// Explanation:
// 2^1 = 2
//

class Solution {
    solve(n: number): boolean {
        return n != 0 && (n & (n - 1)) == 0;
    }
}

 export {};
