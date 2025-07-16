class LLNode {
    constructor(val, next = null) {
        this.val = val;
        this.next = next;
    }
}

class Solution {
    solve(head) {
        let current = head.val;

        while ((head = head.next)) {
            if (head.val <= current) {
                return false;
            }
            current = head.val;
        }

        return true;
    }
}
