//
// 137 Yonge St
//
// Given a list of integers of length 3, determine whether it contains the number 1, 3, or 7.
//
// Example 1
//
// Input:
// nums = [5, 1, 9]
//
// Output:
// true
//
// Explanation:
// This array contains `1`
//
// Example 2
//
// Input:
// nums = [8, 5, 9]
//
// Output:
// false
//
// Explanation:
// This array doesn't contain `1`, `3`, or `7`.
//
// Example 3
//
// Input:
// nums = [1, 3, 7]
//
// Output:
// true
//
// Explanation:
// This array contains `1`, `3`, and `7`.
//

class Solution {
    solve(nums: number[]): boolean {
        return nums.includes(1) || nums.includes(3) || nums.includes(7);
    }
}

 export {};
