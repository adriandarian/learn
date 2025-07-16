# Sum of two numbers

Given a list of numbers `nums` and a number `k`, return whether any two numbers from the list add up to `k`. You may **not** use the same element twice.

> Note: Numbers can be negative or 0.
>
> Bonus: Can you do this in one pass?

## Example 1

### Input

```javascript
nums = [35, 8, 18, 3, 22]
k = 11
```

### Output

```javascript
true
```

### Explanation

8 + 3 = 11

## Example 2

### Input

```javascript
nums = [10, 36, 22, 14]
k = 4
```

### Output

```javascript
false
```

### Explanation

No two numbers in this list add up to 4.

## Example 3

### Input

```javascript
nums = [24, 10, 11, 4]
k = 15
```

### Output

```javascript
true
```

### Explanation

11 + 4 = 15

## Example 4

### Input

```javascript
nums = [-22, 22, -11, 11]
k = 0
```

### Output

```javascript
true
```

### Explanation

-11 + 11 = 0

## Example 5

### Input

```javascript
nums = [15, 0, 3, 2]
k = 15
```

### Output

```javascript
true
```

### Explanation

15 + 0 = 15
