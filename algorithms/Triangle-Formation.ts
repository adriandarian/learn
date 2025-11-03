//
// Triangle formation
//
// Given three integers `a`, `b`, and `c`, return whether the sum of the smallest two numbers is greater than the largest.
//
// Example 1
//
// Input:
// a = 4
// b = 5
// c = 6
//
// Output:
// true
//
// Example 2
//
// Input:
// a = 1
// b = 2
// c = 3
//
// Output:
// false
//

class Solution {
    solve(a: number, b: number, c: number): boolean {
        let arr = [a, b, c].sort((a, b) => a - b);
        return arr[0] + arr[1] > arr[2];
    }
}

 export {};
