//
// A unique string
//
// Given a string `s`, determine whether it has all unique characters.
//
// Example 1
//
// Input:
// s = "abcde"
//
// Output:
// true
//
// Explanation:
// All characters only occur once
//
// Example 2
//
// Input:
// s = "aab"
//
// Output:
// false
//
// Explanation:
// There's two `a`'s
//
// Example 3
//
// Input:
// s = ""
//
// Output:
// true
//
// Explanation:
// All characters occur once (of which there are none)
//

class Solution {
    solve(s: string): boolean {
        for (const e of s) {
            const matches = s.match(new RegExp(e, "g"));
            if (matches && matches.length > 1) {
                return false;
            }
        }

        return true;
    }
}

 export {};
