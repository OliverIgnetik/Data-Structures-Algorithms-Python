from queue import PriorityQueue


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __le__(self, other):
        if self.val <= other.val:
            return 1
        else:
            return 0

    def __lt__(self, other):
        if self.val < other.val:
            return 1
        else:
            return 0


# O(kN)
"""
You are comparing the first element from each linked list 
O(k) to find the linked list with the smallest head
N final nodes in the last linked list   
"""


def mergeKLists(lists: list[ListNode]) -> ListNode:

    def get_min_node(lists):
        min_node = ListNode(val=float('inf'))
        min_node_index = 0
        for i, lstNode in enumerate(lists):
            if lstNode != None and lstNode.val < min_node.val:
                min_node = lstNode
                min_node_index = i

        if min_node.val == float('inf'):
            return None
        else:
            ref = lists[min_node_index]
            lists[min_node_index] = ref.next

        return min_node

    original_head = get_min_node(lists)
    if original_head == None:
        return original_head

    nextNode = None
    currentNode = original_head

    while True:
        nextNode = get_min_node(lists)
        if nextNode == None:
            return original_head
        else:
            currentNode.next = nextNode
            currentNode = currentNode.next


# O(N*logk)
"""
Every pop and insertion takes O(logk)
Finding the smallest value takes O(1)
There are N nodes in the final linked list
"""


def mergeKLists_optimized(lists: list[ListNode]) -> ListNode:
    if len(lists) == 0:
        return None

    def get_min_node():
        min_node = q.get()[2]
        if min_node.next != None:
            ref = min_node.next
            q.put((ref.val, id(ref), ref))
        return min_node

    q = PriorityQueue()
    for listNode in lists:
        if listNode:
            q.put((listNode.val, id(listNode), listNode))

    original_head = get_min_node()

    nextNode = None
    currentNode = original_head
    while not q.empty():
        nextNode = get_min_node()
        currentNode.next = nextNode
        currentNode = nextNode

    return original_head


ll_a = ListNode(1, ListNode(4, ListNode(5, None)))
ll_b = ListNode(1, ListNode(3, ListNode(4, None)))
ll_c = ListNode(2, ListNode(6, None))

res = mergeKLists_optimized([ll_a, ll_b, ll_c])
print(res)
