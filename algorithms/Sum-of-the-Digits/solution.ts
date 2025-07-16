class Solution {
    solve(num: number): number {
        return Array.from(String(num), Number).reduce((a, r) => a + r);
    }
}
