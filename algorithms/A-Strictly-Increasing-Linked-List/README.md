# A strictly increasing linked list

Given the head of a singly linked list head, return whether the values of the nodes are sorted in a strictly ascending order.

## Example 1

### Input

```javascript
head = 1 → 51 → 101 → 101
```

### Output

```javascript
false
```

### Explanation

Even though this list is sorted, it's not strictly increasing since 101 is repeated.

## Example 2

### Input

```javascript
head = 1 → 51 → 101 → 151
```

### Output

```javascript
true
```

### Explanation

The values 1, 51, 101, 151 are strictly increasing.