class Solution {
    solve(a, b) {
        let result = 0;

        a.forEach((e, i) => {
            result += e * b[i];
        });

        return result;
    }
}
