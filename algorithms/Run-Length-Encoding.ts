//
// Run-length encoding
//
// Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent
// repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would
// be encoded as "4A3B2C1D2A".
//
// Implement run-length encoding. You can assume the string to be encoded have no digits
// and consists solely of alphabetic characters.
//
// Example 1
//
// Input:
// s = "AAAABBBCCDAA"
//
// Output:
// "4A3B2C1D2A"
//
// Example 2
//
// Input:
// s = "ABCDE"
//
// Output:
// "1A1B1C1D1E"
//
// Example 3
//
// Input:
// s = "AABBA"
//
// Output:
// "2A2B1A"
//

class Solution {
    solve(s: string): string {
        if (s === "") return "";

        let a: Array<string> = s.split(new RegExp("(?<=(.))(?!\\1)", "g")),
            result: string = "";

        for (let i: number = 0; i < a.length; i += 2) {
            if (i === a.length - 1) {
                result += `${a[i].length}${a[i][0]}`;
                break;
            }

            result += `${a[i].length}${a[i + 1]}`;
        }

        return result;
    }
}

 export {};
