//
// Merging two sorted lists
//
// Given two sorted lists of integers, merge them into one large sorted list.
//
// For example, given these two lists:
//
// lst0 = [5, 10, 15]
// lst1 = [3, 8, 9]
//
// Return [3, 5, 8, 9, 10, 15].
//
// Example 1
//
// Input:
// lst0 = [5, 10, 15]
// lst1 = [3, 8, 9]
//
// Output:
// [3, 5, 8, 9, 10, 15]
//

class Solution {
    solve(lst0: number[], lst1: number[]): number[] {
        return [...lst0, ...lst1].sort((a: number, b: number) => a - b);
    }
}

 export {};
