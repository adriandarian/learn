class LLNode {
    val: number;
    next: LLNode | null;

    constructor(val: number, next: LLNode | null) {
        this.val = val;
        this.next = next;
    }
}

class Solution {
    solve(node: LLNode): number {
        let length: number = 0,
            current: LLNode = node;

        while (current.next !== null && current.next !== undefined) {
            length++;
            current = current.next;
        }

        return length + 1;
    }
}
