class Solution {
    solve(nums) {
        let largest = Math.max(...nums);

        nums.splice(nums.indexOf(largest), 1);

        let second_largest = Math.max(...nums);

        return largest > second_largest * 2;
    }
}
