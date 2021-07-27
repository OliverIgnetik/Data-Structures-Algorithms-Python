"""
Implement An LRU Cache
An LRU cache is a cache that uses the LRU replacement policy.

The cache has the following api:
- get(int key): Returns the value corresponding to the key key. 
If the key does not exist null is returned instead.
- put(int key, int value): Inserts the key-value pair into the cache.
If an item with key key already exists then the value will just be updated.

These are the special properties of the cache:
- When an item is retrieved by key it moves to the conceptual "front" of the cache (it is the most recently used item)
- When an item is updated it moves to the conceptual "front" of the cache (it is the most recently used item)
- When a new item is inserted it is inserted to the "front"
- When the cache goes over-capacity it will remove the least recently used item which will sit at the conceptual "end" 
of the cache to make room for the new item inserted

Implement an LRU cache.
"""


class LRUNode:
    def __init__(self, key, value, next=None, prev=None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev


class LRUCache:
    """
    Approach
    ----
    1. Use a linked list they are a better choice then an array because of the shifting of items (O(N)).
    - Linked Lists are great for removal and insertion
    - Even if we use a hashtable to index to items there is no way to index to the item before the tail
    - Doubly Linked Lists would be a better choice as we have the prev pointer. We can use a doubly linked list 
    in combination with a hashtable to index straight into the items of interest
    - the keys of values would map to the memory address of the nodes

    NOTE: HASHTABLES CAN AUGMENT MANY DATA STRUCTURES, THE INDEXED PRIORITY QUEUE IS A GREAT EXAMPLE

    2. Time complexities should be on the order:
    get - O(1)
    put - O(1)

    3. Model use cases
    insert - insert item to head of queue
    remove - remove from the front of the queue 
    get - move item to front of the queue 
    update - move item to front of the queue 
    capacityCheck - if the cache goes over capacity we remove the end of the queue
    """

    def __init__(self):
        self.capacity = 0
        self.maxCapacity = 5
        # store references to nodes
        self.hashtable = {}
        self.head = None
        self.tail = self.head

    def put(self, key, value):
        if key not in self.hashtable:
            # we put it at the front of the queue and place it in the hashtable
            newNode = LRUNode(key, value)
            self.hashtable[key] = newNode
            if self.capacity == 0:
                self.head = newNode
                self.capacity += 1
            else:
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
                # increment capacity and check
                self.capacity += 1
                self.checkCapacity()
                return
        else:
            node_reference = self.hashtable[key]
            node_reference.value = value
            self.moveToFront(key)
            return

    def get(self, key):
        if key not in self.hashtable:
            raise KeyError(f'{key} not in LRU Cache')
        else:
            node_reference = self.hashtable[key]
            self.moveToFront(key)
            return node_reference.value

    def moveToFront(self, key):
        node_reference = self.hashtable[key]
        # check if its already the head
        # we don't want to touch it then
        if node_reference is self.head:
            return
        # check if its the tail
        if node_reference is self.tail:
            new_tail = self.tail.prev
            new_tail.next = None
            self.tail = new_tail
            node_reference.next = self.head
            self.head.prev = node_reference
            node_reference.prev = None
            self.head = node_reference
        else:
            # pull it out
            node_reference.prev.next = node_reference.next
            node_reference.next = self.head
            self.head.prev = node_reference
            self.head = node_reference
            node_reference.prev = None

    def checkCapacity(self):
        if self.capacity > self.maxCapacity:
            new_tail = self.tail.prev
            new_tail.next = None
            self.capacity -= 1
            return


cache = LRUCache()
cache.put('a', 3)
cache.put('b', 10)
cache.put('c', 3)
cache.put('d', 1)
cache.put('a', 1)
cache.put('a', 2)
cache.put('d', -10)
cache.put('e', 9)

print(cache.get('d'))
