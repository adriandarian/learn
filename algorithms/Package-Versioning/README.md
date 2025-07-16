# Package versioning

Given strings older and newer, each representing software package versions in the format major.minor.patch, return whether the newer version is actually newer than the older.

## Example 1

### Input

```python
older = "11.1.2"
newer = "11.1.3"
```

### Output

```python
True
```

### Explanation

The patch version of the `new` string is more recent.

## Example 2

### Input

```python
older = "3.1.2"
newer = "1.1.3"
```

### Output

```python
False
```

### Explanation

The old version has a newer major version since `3 > 1`

## Example 3

### Input

```python
older = "3.1.2"
newer = "3.2.3"
```

### Output

```python
True
```

### Explanation

The minor version of the new package is more recent

## Example 4

### Input

```python
older = "13.1.2"
newer = "3.2.3"
```

### Output

```python
False
```

### Explanation

Old version has a newer major version since `13 > 3`
