class Solution {
    solve(nums: Array<number>, k: number): boolean {
        let map: Object = {};

        for (let i: number = 0; i < nums.length; i++) {
            if (map[nums[i]] !== undefined) {
                return true;
            }

            map[k - nums[i]] = true;
        }

        return false;
    }
}
