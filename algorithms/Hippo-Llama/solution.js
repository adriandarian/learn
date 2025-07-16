class Solution {
    solve(s) {
        return (
            (s.match(/hippo/g) || []).length ===
            (s.match(/llama/g) || []).length
        );
    }
}
