class Solution {
    solve(n: number): Array<number> {
        let arr: Array<number> = [2, 3];

        if (n < 2) return [];
        else if (n === 2) return [2];
        else {
            for (let i: number = 5; i <= n; i += 2) {
                if (arr.every((p: number) => i % p)) {
                    arr.push(i);
                }
            }
        }

        return arr;
    }
}
