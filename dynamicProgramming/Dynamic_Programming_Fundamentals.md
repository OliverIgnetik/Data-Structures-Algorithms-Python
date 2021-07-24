# Dynamic Programming Fundamentals

Dynamic programming is a rich and powerful algorithm design tool/strategy that is characterized by:

- Strictly overlapping **subproblems**
- Such subproblems can be **related together** and **overlap**
- Solutions to subproblems can be cached using **memoization**

As you just read, dynamic programming is characterized by **overlapping subproblems**.
**NOTE:** the decision tree is key for understanding dynamic programming problems.

## Interval scheduling with weights

If we have a yes/no style type question then we will typically have a branching factor of 2.
If we are checking N items then:

Assumption of perfect binary tree
Time Complexity : O(2^N)
However, using memoization we can reduce this to O(N)

## More exact derivation of work

T(N-1) -> work to compute the answer when we don't include the item
T(p(N)) -> work to compute the answer to the sub-problem which does not break our constraints
T(p(N) = (N-1) (ie. what if the sub-problem the next smallest sub-problem)
O(1) -> we do constant work at each call

#### Recurrence relation

T(N) = T(N-1) + T(p(N)) + O(1)
T(N) >= 2T(N-1) + O(1)

Using the master theorem the solution is:
T(N) is an element of O(2^N)

### Applications

- weight based problems (knapsack, scheduling problems considering weight etc.)
- intimate connections between subproblems (the decision tree is more complex, ie. choosing the best solution at each stack frame will break us later on)
- overlapping subproblems

## DP vs. Greedy:

Often you will be faced with deciding if a problem should be solved with DP or a greedy algorithm. The key difference to note is DP problems often have subproblems with _intimate_ connections that would render a greedy algorithm useless 5 choices into solving an input.

## DP presents a much more powerful idea:

To find the global optimum of problem p, we first look to what information we need to solve p optimally
We discover that p is just the larger of two other subproblems, q and z. So p = max(q, z)
But then what is the solution to q and z? The same recursive cases happen until a **base case** is reached

## The Base Case:

We should start with what we know for sure. A base case is the "certain answer".

The base case is an input to our algorithm to which the answer is often known in O(1) time (or around that).

It provides out algorithm the "knowledge" it needs to solve the recursive cases.

## Top-Down vs. Bottom-Up

This brings us to how we can craft our DP algorithm. We can either:

- Bottom Up: Start from the base cases (go "bottom-up") and go up to the global subproblem we are trying to solve
- Top Down: Start from the global subproblem (go "top-down") and go to the base cases we know the answer to.

**Top-down** dynamic programming implementations are easiest to come up with first as recursion very naturally models the recursive cases and how they relate (and how you'd naturally think about the problem).

One just has to make sure that they "memoize" the recursion and cache repeated subproblems to eliminate recomputation of function call subtrees.

**Bottom-up** dynamic programming implementations are easiest to implement as they can be iteratively written in a straight-forward manner (often 1 or 2 nested for() loops).
