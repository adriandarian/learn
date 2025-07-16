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
