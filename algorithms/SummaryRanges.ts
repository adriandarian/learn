//
// Summary Ranges
//
// Given a sorted integer array without duplicates, return the summary of its ranges.
//
// Example 1:
//
// Input:  [0,1,2,4,5,7]
// Output: ["0->2","4->5","7"]
// Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
//
// Example 2:
//
// Input:  [0,2,3,4,6,8,9]
// Output: ["0","2->4","6","8->9"]
// Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
//
// Javascript Solution
//
// Runtime: 44 ms, faster than 96.26% of JavaScript online submissions for Summary Ranges.
// Memory Usage: 33.8 MB, less than 100.00% of JavaScript online submissions for Summary Ranges.
//

function summaryRanges(nums: number[]): string[] {
    const result: string[] = [];
    let start: number = nums[0];

    if (nums.length === 0) {
        return [];
    }

    if (nums.length === 2) {
        if (start + 1 === nums[1]) {
            return [start + "->" + nums[1]];
        } else {
            return [nums[0].toString(), nums[1].toString()];
        }
    }

    for (let i: number = 0, count: number = 0; i < nums.length; i++) {
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
}

 export {};
