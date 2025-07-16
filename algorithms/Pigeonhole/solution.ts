class Solution {
    solve(nums: Array<number>): number {
        return nums.filter((item, index) => nums.indexOf(item) != index)[0];
    }
}
