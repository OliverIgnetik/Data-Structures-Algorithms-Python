# The Backtracking Blueprint

Backtracking is an algorithmic technique that involves trying possibilities along a "search path" and cutting off paths of search that will no longer yield a solution.

These "search paths" can manifest as:

- Actual search paths in a graph or searchable structure
- Chosen characters placed in a progress string
- Moves played in a puzzle, etc.

### Words to pick up on

- Generate all
- Compute all
- Exhaustive searches -> DFS

## The 3 core ideas behind backtracking are:

1. The Choice: What fundamental choice is being made at every step of the algorithm to advance to a solution?
2. The Constraints: When is a path of decision no longer fruitful? When does the algorithm know for sure that it is wasting time following a certain path? If it is determined a path will no longer yield a solution an algorithm is said to "backtrack" when it returns control to a previous decision that can be advanced from.
3. The Goal: When do we know that the solution has been found?

Backtracking algorithms are most naturally modeled **recursively**, though not all recursion is backtracking as backtracking is characterized by **the actual act of backtracking when a path is no longer solvable**.

**There must be an element of reflecting on the algorithm's state and deciding to backtrack.**
