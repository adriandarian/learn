//
// Repeated addition
//
// Given a positive integer `n`, sum all of its digits to get a new number. Repeat this operation until it's less than 10.
//
// Example 1
//
// Input:
// n = 8835
//
// Output:
// 6
//
// Explanation:
// - 8 + 8 + 3 + 5 = 24
// - 2 + 4 = 6
//

class Solution {
    solve(n: number): number {
        let result = Array.from(String(n), Number).reduce(
            (acc, cur) => acc + cur
        );
        return result > 10 ? this.solve(result) : result;
    }
}

 export {};
