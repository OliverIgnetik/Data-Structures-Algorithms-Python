# Heaps Fundamentals

A heap is a data structure that implements the priority queue ADT (Abstract Data Type).

The most common manifestation you will see of the heap is the binary heap.

A binary heap is arranged such that:

- Max Heap: Each node is >= all elements in its left and right subtrees (if they exist)
- Min Heap: Each node is <= all elements in its left and right subtrees (if they exist)

## Index from 0

- Left child : 2\*i + 1
- Right child : 2\*i + 2
- Parent : (i-1)//2

## Index from 1 (index 0 is dummy)

- Left child : 2\*i
- Right child : 2\*i+1
- Parent : i//2

The easiest way to implement a binary heap is by encoding the binary tree structure into an array like so (notice the pattern):

Array Form: [100, 70, 50, 60]

# Max Heap Conceptualization:

        100
       /   \
      70   50
     /
    60

If you read off the array (left to right) and fill out the tree top-to-bottom, left-to-right, you will understand the mapping system.

We will get plenty of practice with heaps and the above encoding concept (so we won't go too detail heavy here).

## The key things to remember are:

- Heaps support O(1) access to min items (in a "min-heap") and max items (in a "max-heap")
- Binary heaps support O(log(n)) removal of the min/max item (the "last" item is swapped to the root and "bubbled down" O(log(n)) levels)
- Binary heaps support O(log(n)) insertion (the item must be "sifted-up" O(log(n)) levels)
- When you hear "largest item" or "smallest item" think about using a heap to optimize min/max look-ups
- Binary heaps are complete binary trees. This will help you conceptualize what insert() and remove() look like
