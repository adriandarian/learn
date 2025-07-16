class Solution {
    solve(n: number): Array<string> {
        let arr: Array<string> = [];

        for (let i: number = 1; i <= n; i++) {
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
