# The lonely product

Given three numbers, `a`, `b`, and `c`, return their product, but if any two numbers are the same, they do not count.

## Example 1

### Input

```javascript
a = 2
b = 3
c = 4
```

### Output

```javascript
24
```

### Explanation

All three numbers are unique so their product is `2 * 3 * 4 = 24`

## Example 2

### Input

```javascript
a = 3
b = 3
c = 5
```

### Output

```javascript
5
```

### Explanation

There's two `3`s so the product is `5`

## Example 3

### Input

```javascript
a = 3
b = 3
c = 3
```

### Output

```javascript
1
```

### Explanation

All three numbers are the same, so they don't count toward the product.
