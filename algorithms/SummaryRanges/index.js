/**
 * @param {number[]} nums
 * @return {string[]}
 */
var summaryRanges = function(nums) {
  let result = [],
    start = nums[0];

  if (nums === []) {
    return [];
  }

  if (nums.length === 2) {
    if (start + 1 === nums[1]) {
      return [start + "->" + nums[1]];
    } else return [nums[0].toString(), nums[1].toString()];
  }

  for (let i = 0, count = 0; i < nums.length; i++) {
    if (nums[i] + 1 !== nums[i + 1] || nums[i + 1] === undefined) {
      if (count > 0) {
        result.push(start + "->" + nums[i]);
      } else {
        result.push(start.toString());
      }
      start = nums[i + 1];
      count = 0;
    } else {
      count++;
    }
  }

  return result;
};
