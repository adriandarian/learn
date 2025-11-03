//
// Two Sum
//
// Given an array of integers, return indices of the two numbers such that they add up to a specific target.
//
// You may assume that each input would have exactly one solution, and you may not use the same element twice.
//
// Example:
//
// Given nums = [2, 7, 11, 15], target = 9,
//
// Because nums[0] + nums[1] = 2 + 7 = 9,
// return [0, 1].
//
// Java Submission
//
// Runtime: 1 ms, faster than 99.89% of Java online submissions for Two Sum.
// Memory Usage: 41.3 MB, less than 5.65% of Java online submissions for Two Sum.
//

public class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] arr = new int[2];
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++) {
            if (map.get(nums[i]) != null) {
                arr[0] = map.get(nums[i]);
                arr[1] = i;
                break;
            } else {
                map.put(target - nums[i], i);
            }
        }
        return arr;

    }
}
