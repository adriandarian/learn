class Solution {
    solve(n: number): number {
        return n === 0
            ? 0
            : (n >>> 0)
                  .toString(2)
                  .split("")
                  .filter((e) => ~~e > 0).length;
    }
}
