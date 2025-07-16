class Solution {
    solve(n) {
        let f = [];

        for (let i = 0; i < n; i++) {
            if (i === 0) {
                f.push(1);
            } else if (i === 1) {
                f.push(1);
            } else {
                f.push(f[i - 1] + f[i - 2]);
            }
        }

        return f[f.length - 1];
    }
}
