class Solution {
    solve(n: number): number {
        let result = Array.from(String(n), Number).reduce(
            (acc, cur) => acc + cur
        );
        return result > 10 ? this.solve(result) : result;
    }
}
