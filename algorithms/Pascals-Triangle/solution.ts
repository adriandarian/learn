class Solution {
    solve(n: number): Array<number> {
        var rows = [1];

        for (var i = 1; i <= n; ++i) {
            rows[i] = (rows[i - 1] * (n - i + 1)) / i;
        }

        return rows;
    }
}
