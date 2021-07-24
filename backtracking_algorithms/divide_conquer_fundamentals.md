# Divide and Conquer Methodology

A divide-and-conquer algorithm is an algorithm that divides its input and often runs a subroutine on each split section to solve the overarching problem.

A good recurrence relation to keep in your pocket is:

```
T(N) = T(N/2) + O(N)
```

- Divide your work and make a decision
- Notice the 2 is missing as a coefficient next to T(N/2)

## Divide-and-conquer algorithms are characterized by:

- Some sort of "splitting" subroutine that divides input
- A conquering subroutine that performs the valuable computation that relates and solves across many split sections of the input

The "conquering" subroutine is of most interest to us. This is where the core value of the algorithm comes from as it is often easy to see how input can be split (we often split in halves, rarely thirds).

1. If we have a quadratic time algorithm (notated O(N^2)), we can improve it by trying a divide-and-conquer approach. We can see this by looking at the recurrence relations of problems like mergesort. But, we need to conceptualize a linear merging operation.

2. We first determine if the input can be split and solved in subproblems. Then we see if we can find an O(N) time merging algorithm to bring the overall time complexity down to O(N \* log(N)).

## Another proof for deriving O(N^2)

If we have to compare every pair and order doesn't matter and we have N items.

```
T(N) = (N choose 2)
     = N!/(2!(N-2)!)
     = N(N-1)/2 is O(N^2)
```

## Recurrence Relations

T(N) <= 2T(N/2) + O(N)

T(N) is O(NlogN)

Using the **master theorem**

### Master Theorem for Recurrence Relations

```
T(n) = aT(n/b) + cn^k
```

```
- T(n) is O(n^k) if a < b^k
- T(n) is O(n^k log_b(n)) if a = b^k
- T(n) is O(n^(log_b(a))) if a < b^k
```

Split and merge -> mergesort
