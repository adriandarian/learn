# Run-length encoding

Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent
repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would
be encoded as "4A3B2C1D2A".

Implement run-length encoding. You can assume the string to be encoded have no digits
and consists solely of alphabetic characters.

## Example 1

### Input

```javascript
s = "AAAABBBCCDAA"
```

### Output

```javascript
"4A3B2C1D2A"
```

## Example 2

### Input

```javascript
s = "ABCDE"
```

### Output

```javascript
"1A1B1C1D1E"
```

## Example 3

### Input

```javascript
s = "AABBA"
```

### Output

```javascript
"2A2B1A"
```
