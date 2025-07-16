# Pascal's triangle

Given an integer `n`, return the `nth` (0-indexed) row of Pascal's triangle.

Pascal's triangle can be created as follows: In the top row, there is an array of 1. Subsequent row is created by adding the number above and to the left with the number above and to the right, treating empty elements as `0`.

The first few rows are:

![Pascal's Triangle](https://wikimedia.org/api/rest_v1/media/math/render/svg/23050fcb53d6083d9e42043bebf2863fa9746043)

## Example 1

### Input

```typescript
n = 3
```

### Output

```typescript
[1, 3, 3, 1]
```

### Explanation

This is row `3` in

```typescript
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
```
