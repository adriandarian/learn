class Solution {
    solve(nums) {
        return nums.map((e) => e * e).sort((a, b) => a - b);
    }
}
