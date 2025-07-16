class Solution {
    solve(s: string, n: number): Array<string> {
        return s.match(new RegExp(`.{1,${n}}`, "g"));
    }
}
