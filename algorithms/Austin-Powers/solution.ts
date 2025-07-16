class Solution {
    solve(n: number): boolean {
        return n != 0 && (n & (n - 1)) == 0;
    }
}
