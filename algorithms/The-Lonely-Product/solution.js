class Solution {
    solve(a, b, c) {
        if (a === b && a === c) return 1;
        else if (a === b) return c;
        else if (b === c) return a;
        else if (a === c) return b;
        else return a * b * c;
    }
}
