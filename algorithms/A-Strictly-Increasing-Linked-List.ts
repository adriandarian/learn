//
// A strictly increasing linked list
//
// Given the head of a singly linked list head, return whether the values of the nodes are sorted in a strictly ascending order.
//
// Example 1
//
// Input:
// head = 1 → 51 → 101 → 101
//
// Output:
// false
//
// Explanation:
// Even though this list is sorted, it's not strictly increasing since 101 is repeated.
//
// Example 2
//
// Input:
// head = 1 → 51 → 101 → 151
//
// Output:
// true
//
// Explanation:
// The values 1, 51, 101, 151 are strictly increasing.
//

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

 export {};
