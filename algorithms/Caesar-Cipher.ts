//
// Caesar cipher
//
// You are given a lowercase alphabet string `s`, and an offset integer `k`. Replace every letter in `s` with a letter `k` positions further along the alphabet.
//
// Note: If the letter overflows past a or z, it gets wrapped around the other side.
//
// Example 1
//
// Input:
// s = "abc"
// k = 2
//
// Output:
// "cde"
//
// Explanation:
// "abc" gets moved 2 positions to the right.
//
// Example 2
//
// Input:
// s = "aaa"
// k = -1
//
// Output:
// "zzz"
//
// Example 3
//
// Input:
// s = "zzz"
// k = 1
//
// Output:
// "aaa"
//
// Explanation:
// The "z" gets wrapped to "a"
//

class Solution {
    solve(s: string, k: number): string {
        return s
            .split("")
            .map((c: string) => c.charCodeAt(0) + (k % 26))
            .map((x: number) => (x > 122 ? x - 26 : x))
            .map((x: number) => (x < 97 ? x + 26 : x))
            .map((x: number) => String.fromCharCode(x))
            .join("");
    }
}

 export {};
