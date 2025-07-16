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
