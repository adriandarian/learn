//
// Middle of the list
//
// Given a sorted list `nums` of integers, return the value of the middle element. If the length of the list is even, return the first middle element.
//
// Example 1
//
// Input:
// nums = [10, 20, 30]
//
// Output:
// 20
//
// Example 2
//
// Input:
// nums = [10, 20, 30, 40]
//
// Output:
// 20
//
// Explanation:
// 20 and 30 are both middle elements but 20 is the first one.
//

class Solution {
    solve(nums: number[]): number {
        return nums[Math.floor((nums.length - 1) / 2)];
    }
}

 export {};
