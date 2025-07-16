# Regular Expression Matching

Implement regular expression matching with the following special characters:

- `.` (period) which matches any single character
- `*` (asterisk) which matches zero or more of the preceding element
- 
That is, implement a function that takes in a valid regular expression `pattern` and a string `s`
and returns whether or not the string matches the regular expression.

> Note: The input pattern is guaranteed not to have consecutive asterisks.

## Example 1

### Input

```typescript
pattern = "ra."
s = "ray"
```

### Output

```typescript
true
```

### Explanation

We have ra and then a single character

## Example 2

### Input

```typescript
pattern = "a"
s = "aa"
```

### Output

```typescript
false
```

## Example 3

### Input

```typescript
pattern = "a*"
s = "aa"
```

### Output

```typescript
true
```

### Explanation

We have 0 or more `a`s.

## Example 4

### Input

```typescript
pattern = ".*"
s = "abc"
```

### Output

```typescript
true
```

### Explanation

We have 0 or more of any character
