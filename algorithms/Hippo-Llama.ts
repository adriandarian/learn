//
// Hippo llama
//
// Give a string `s`, return whether the number of occurrences of `hippo` and `llama` in `s` are the same.
//
// Example 1
//
// Input:
// s = "llama"
//
// Output:
// false
//
// Explanation:
// `llama` occurs once but `hippo` is not in the string.
//
// Example 2
//
// Input:
// s = "llamahippo"
//
// Output:
// true
//
// Explanation:
// `llama` and `hippo` both occur once.
//
// Example 3
//
// Input:
// s = "hippollamahippohelloworldllama"
//
// Output:
// true
//
// Explanation:
// `llama` and `hippo` both occur twice.
//

class Solution {
    solve(s: string): boolean {
        return (
            (s.match(/hippo/g) || []).length ===
            (s.match(/llama/g) || []).length
        );
    }
}

 export {};
