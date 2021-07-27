"""
The Most Visited Pages Problem
We are tasked with implementing a LogProcessor. 
Our LogProcessor is passed a stream of pages and at any point in time it must be able to list
the top k most visited pages as fast as possible (asymptotically).

The LogProcessor supports this API:
insert(String visitedPageId): Inserts a visited page's id into the LogProcessor
topKVisitedPages(int k): Returns the ids of the top k most visited pages

Example:
insert("page 1")
insert("page 1")
insert("page 1")
insert("page 1")
insert("page 2")
insert("page 2")
insert("page 3")
topKVisitedPages(1) # ["page 1"]
topKVisitedPages(2) # ["page 1", "page 2"]
topKVisitedPages(3) # ["page 1", "page 2", "page 3"]

Explanation:
"page 1" is seen the most (4 occurrences)
"page 2" is seen the second most (2 occurrences)
"page 3" is seen the thrid most (1 occurrence)

Constraints:
0 < k < total unique pages
"""


class LogProcessor:
    """
    Approaches
    ----
    1. An Indexed Priority Queue (IPQ) could be a good implementation, this is because each 
    page has:
    - a hash value : unique page identifier 
    - priority : number of visits
    - updates are efficient

    How to update? 
    - the update API is built in to the fundamental nature of this data structure
    - it is the most efficient choice
    - insert (O(logN)) update (O(logN)) remove (O(logN))

    * Complexity 
    topK() time : O(klogN)
    Space : O(N)

    2. BST (height balanced with hashtable wiring) read the reverse inorder traversal up to the kth item. 
    How to update? 
    - We can store our nodes for each page in a hash table and increment the counter 
    when there is a page visit.
    - When we update a node that is in the tree we can remove it from the tree and increment the count and insert it back in the tree.
    (this will have O(2logN) -> O(logN) time complexity which will have a wall time that is slightly worse then the IPQ)
    - insert (O(logN)) 
    - update (O(2logN)) 
    - remove (O(logN))

    Inorder traversal : L N R 
    Inorder traversal reversed : R N L 

    * Complexity 
    inorder traversal : O(N)
    topK() time : O(logN + k) -> O(k) asymptotically, but in reality N might be like 1 billion and k would be something like 3
    NOTE: (it takes logN calls to get to the bottom of the tree and k traversals to get the top k items)
    Space : O(N)

    3. Heap 
    We need completeness of data so we can't use the heap sorting approach were we throw away the smallest
    item when our heap has a size bigger then k.(ie. leaving the k biggest items). 
    We could implement a heap where each node is an object with a reference in a hash map. 

    How to update? 
    - Each time we record a page visit we could query the hashtable and then update the node in the heap. 
    - We would then have to check the heap invariant is satisfied.
    - insert (O(logN)) 
    - update would be very difficult to implement due to the fact we can only typically remove the root node 
    - remove (O(logN))

    * Complexity 
    topK() time : O(klogN)
    Space : O(N)

    WINNER 
    ----
    BST WITH HASHTABLE IS THE EASIEST TO IMPLEMENT
    """
