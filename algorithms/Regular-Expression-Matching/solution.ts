class Solution {
    solve(pattern: string, s: string): boolean {
        return s.match(new RegExp(`^${pattern}$`, "g")) === null ? false : true;
    }
}
