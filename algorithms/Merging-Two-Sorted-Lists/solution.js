class Solution {
    solve(lst0, lst1) {
        return [...lst0, ...lst1].sort((a, b) => a - b);
    }
}
