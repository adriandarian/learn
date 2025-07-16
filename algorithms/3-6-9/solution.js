class Solution {
    solve(n) {
        let arr = [];

        for (let i = 1; i <= n; i++) {
            if (
                i % 3 === 0 ||
                `${i}`.includes("3") ||
                `${i}`.includes("6") ||
                `${i}`.includes("9")
            ) {
                arr.push("clap");
            } else {
                arr.push(`${i}`);
            }
        }

        return arr;
    }
}
