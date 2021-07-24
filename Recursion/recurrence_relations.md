# Master Theorem for Recurrence Relations

```
T(n) = aT(n/b) + cn^k
```

```
- T(n) is O(n^k) if a < b^k
- T(n) is O(n^k log_b(n)) if a = b^k
- T(n) is O(n^(log_b(a))) if a < b^k
```

# Typical Recurrences

1.

```
T(N) = 2T(N/2) + O(N)
T(N) is O(NlogN)
```

Examples : mergesort

2.

```
T(N) = qT(N/2) + O(N)
T(N) is O(N^(log_2(q)))
```

Examples : very academic

3.

```
T(N) = T(N/2) + O(N)
T(N) is O(N)
```

Examples : quickselect

## Example Recurrence relation

```
T(n) = T(n/2) + O(n)
```

Using the master theorem

- a = 1, b = 2, c = 1, k = 1
- b^k = 2 > a

Thus T(n) is O(n)
