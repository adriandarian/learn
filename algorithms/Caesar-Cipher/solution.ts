class Solution {
    solve(s: string, k: number): string {
        return s
            .split("")
            .map((c: string) => c.charCodeAt(0) + (k % 26))
            .map((x: number) => (x > 122 ? x - 26 : x))
            .map((x: number) => (x < 97 ? x + 26 : x))
            .map((x: number) => String.fromCharCode(x))
            .join("");
    }
}
