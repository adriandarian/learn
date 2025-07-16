class Solution {
    solve(n) {
        if (n === 0) {
            return 0;
        }

        return (n >>> 0)
            .toString(2)
            .split("")
            .filter((e) => e > 0).length;
    }
}
