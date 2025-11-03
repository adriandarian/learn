//
// Chunky strings
//
// Given a string `s` and an integer `n`, split up `s` into `n`-sized pieces.
//
// For example, given:
//
// s = "abcdefg"
// n = 3
//
// Return ["abc", "def", "g"].
//
// If there are extra characters left over, they should be in its own piece.
//
// Example 1
//
// Input:
// s = "abcdef"
// n = 2
//
// Output:
// ["ab", "cd", "ef"]
//

class Solution {
    solve(s: string, n: number): Array<string> {
        return s.match(new RegExp(`.{1,${n}}`, "g"));
    }
}

 export {};
