class Solution {
    solve(n: number): number {
        let nums: Array<number> = [];

        for (let i: number = 5; i <= n; i++) {
            if (i % 3 === 0 || i % 4 === 0 || i % 7 === 0) {
                nums.push(i);
            }
        }

        return [3, 4, ...nums].reduce((acc: number, cur: number) => acc + cur);
    }
}
