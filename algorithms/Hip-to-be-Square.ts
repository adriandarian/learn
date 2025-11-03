//
// Hip to Be Square
//
// Given a sorted list of integers, square the elements and give the output in sorted order.
//
// Note: The integers can be 0 or negative.
//
// Example 1
//
// Input:
// nums = [-9, -2, 0, 2, 3]
//
// Output:
// [0, 4, 4, 9, 81]
//
// Example 2
//
// Input:
// nums = [1, 2, 3, 4, 5]
//
// Output:
// [1, 4, 9, 16, 25]
//

class Solution {
    solve(nums: number[]): number[] {
        return nums.map((e: number) => e * e).sort((a: number, b: number) => a - b);
    }
}

 export {};
