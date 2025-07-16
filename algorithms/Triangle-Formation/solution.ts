class Solution {
    solve(a: number, b: number, c: number): boolean {
        let arr = [a, b, c].sort((a, b) => a - b);
        return arr[0] + arr[1] > arr[2];
    }
}
