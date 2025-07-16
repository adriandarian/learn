class Solution {
    solve(s, k) {
        return s
            .split("")
            .map((c) => c.charCodeAt(0) + (k % 26))
            .map((x) => (x > 122 ? x - 26 : x))
            .map((x) => (x < 97 ? x + 26 : x))
            .map((x) => String.fromCharCode(x))
            .join("");
    }
}
