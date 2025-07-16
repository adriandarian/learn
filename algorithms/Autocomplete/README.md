# Autocomplete

Given a query string s and a list of all possible words, return all words that have s as a prefix.

## Example 1

### Input

```typescript
s = "de"
words = ["dog", "deal", "deer"]
```

### Output

```typescript
["deal", "deer"]
```

### Explanation

Only deal and deer begin with de.

## Example 2

### Input

```typescript
s = "b"
words = ["banana", "binary", "carrot", "bit", "boar"]
```

### Output

```typescript
["banana", "binary", "bit", "boar"]
```

### Explanation

All these words start with b, except for "carrot".
