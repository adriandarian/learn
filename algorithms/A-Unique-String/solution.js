class Solution {
    solve(s) {
        for (const e of s) {
            if (s.match(new RegExp(e, "g")).length > 1) {
                return false;
            }
        }

        return true;
    }
}
