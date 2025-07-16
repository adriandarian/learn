class LLNode {
    val: number;
    next: LLNode | null;

    constructor(val: number, next: LLNode | null) {
        this.val = val;
        this.next = next;
    }
}

class Solution {
    solve(head: LLNode): boolean {
        if (!head || !head.next) {
            return true;
        }

        if (head.next.val <= head.val) {
            return false;
        }

        return this.solve(head.next);
    }
}
