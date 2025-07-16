# Caesar cipher

You are given a lowercase alphabet string `s`, and an offset integer `k`. Replace every letter in `s` with a letter `k` positions further along the alphabet.

> Note: If the letter overflows past a or z, it gets wrapped around the other side.

## Example 1

### Input

```javascript
s = "abc"
k = 2
```

### Output

```javascript
"cde"
```

### Explanation

"abc" gets moved 2 positions to the right.

## Example 2

### Input

```javascript
s = "aaa"
k = -1
```

### Output

```javascript
"zzz"
```

## Example 3

### Input

```javascript
s = "zzz"
k = 1
```

### Output

```javascript
"aaa"
```

### Explanation

The "z" gets wrapped to "a"
