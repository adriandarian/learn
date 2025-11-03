//
// Length of a linked list
//
// Given a singly linked list, return its length. The linked list has fields next and val.
//
// Example 1
//
// Input:
// node = 350
//
// Output:
// 1
//
// Explanation:
// This linked list has 1 node.
//
// Example 2
//
// Input:
// node = 1 → 2
//
// Output:
// 2
//
// Explanation:
// This linked list has 2 nodes.
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

 export {};
