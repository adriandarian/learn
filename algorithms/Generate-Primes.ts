//
// Generate primes
//
// Given a number `n`, return a list of all prime numbers smaller than or equal to `n` in ascending order.
//
// For example, given the number 10, return the list [2, 3, 5, 7].
//
// Note: 1 is not a prime number.
//
// Example 1
//
// Input:
// n = 3
//
// Output:
// [2, 3]
//
// Example 2
//
// Input:
// n = 10
//
// Output:
// [2, 3, 5, 7]
//
// Example 3
//
// Input:
// n = 20
//
// Output:
// [2, 3, 5, 7, 11, 13, 17, 19]
//

class Solution {
    solve(n: number): Array<number> {
        let arr: Array<number> = [2, 3];

        if (n < 2) return [];
        else if (n === 2) return [2];
        else {
            for (let i: number = 5; i <= n; i += 2) {
                if (arr.every((p: number) => i % p)) {
                    arr.push(i);
                }
            }
        }

        return arr;
    }
}

 export {};
