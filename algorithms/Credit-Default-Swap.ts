//
// Credit default swap
//
// Given a list of integers nums, swap each consecutive even indexes with each other, and swap each consecutive odd indexes with each other.
//
// Example 1
//
// Input:
// nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]
//
// Output:
// [2, 3, 0, 1, 6, 7, 4, 5, 8]
//
// Explanation:
// - 0 and 2 gets swapped
// - 1 and 3 gets swapped
// - 4 and 6 gets swapped
// - 5 and 7 gets swapped
// - 8 remains the same
//

class Solution {
    solve(nums: Array<number>): Array<number> {
        for (let i: number = 0; i < 2; i++) {
            for (let j: number = i; j < nums.length - 2; j += 4) {
                nums[j] = nums[j] + nums[j + 2];
                nums[j + 2] = nums[j] - nums[j + 2];
                nums[j] = nums[j] - nums[j + 2];
            }
        }

        return nums;
    }
}

 export {};
