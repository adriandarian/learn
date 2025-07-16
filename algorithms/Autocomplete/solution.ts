class Solution {
    solve(s: string, words: Array<string>): Array<string> {
        return words.filter((e: string) => e.startsWith(s))
    }
}
