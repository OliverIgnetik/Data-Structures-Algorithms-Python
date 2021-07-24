"""
Search A Linked List With Jump References
Given a singly linked list with jump references annotate each list item's order field with its position in a "jump order traversal".

The jump pointer jumps to any random node in the linked list.

A "jump first" traversal is an iteration of the list giving priority to following jump pointers first before following next pointers.

The first node in the list is position 1 in the traversal.

Example:
Input:
                  ------------
                 |            |
                 ˅            |
Node{'a'} -> Node{'b'} -> Node{'c'} -> Node{'d'} -> X
   |             ^ |                       ^
   |             | |                       |
    -------------   -----------------------

Resulting Jump Order:
| Jump Order |   Node    |
| ---------- | --------- |
| 1          | Node{'a'} |
| 2          | Node{'b'} |
| 3          | Node{'d'} |
| 4          | Node{'c'} |

(Detailed) Explanation:
1.) We visit the head node first, Node{'a'}.
2.) We can follow the .next pointer or the .jump pointer, this is "jump first" so we follow the jump pointer
3.) We arrive at Node{'b'}
4.) Node{'b'} has a jump pointer so we follow it
5.) We arrive at Node{'d'}
6.) Node{'d'} has no jump pointer and no next pointer, so now we conceptually return control to Node{'b'} (where we came from)
7.) Node{'b'} already followed .jump, we follow .next
8.) We arrive at Node{'c'}
9.) Node{'c'}.jump goes to Node{'b'} (already visited), Node{'c'}.next goes to Node{'d'} (already visited)
10.) Control goes back to Node{'b'} (where we came from from the .next pointer)
11.) Node{'b'} already followed .jump and .next, we return to Node{'a'} (where we came from)
12.) Node{'a'} already followed its .jump pointer, Node{'a'}.next is Node{'b'} (already visited)
13.) Node{'a'} can go nowhere, we stop
"""


class JumpNode:
    def __init__(self, val, next=None, jump=None):
        self.val = val
        self.next = next
        self.jump = jump
        self.order = -1


class Solution:
    def setJumpOrder(self, head: JumpNode) -> JumpNode:
        """"
        Interface
        ----
        input  
        head : Jumpnode

        output
        Jumpnode reference with orderings

        Complexity
        ----
        Time : O(N)
        Space : O(N)
        """
        stack = []
        currentOrder = 0
        stack.push(head)

        while len(stack) != 0:
            node = stack.pop()

            if node != None and node.order == -1:
                node.order = currentOrder

                currentOrder += 1

                # priority goes to the jump node so we push it last
                stack.append(node.next)
                stack.append(node.jump)

        return head


class RecursiveSolution:
    def setJumpOrder(self, head: JumpNode) -> JumpNode:
        """"
        Interface
        ----
        input  
        head : Jumpnode

        output
        Jumpnode reference with orderings

        Complexity
        ----
        Time : O(N) its like the binary tree example O(2^log_2(N)) = O(N)
        Space : O(N)
        """
        self.order = 0
        self.setJumpOrderRecursiveHelper(head)
        return head

    def setJumpOrderRecursiveHelper(self, node: JumpNode) -> None:

        # base case
        if node == None or node.order != -1:
            return

        # set order of current node
        node.order = self.order

        # increment order
        self.order += 1

        # investigate jump pointer first
        self.setJumpOrderRecursiveHelper(node.jump)
        # investigate next pointer
        self.setJumpOrderRecursiveHelper(node.next)


a = JumpNode('a')
b = JumpNode('b')
c = JumpNode('c')
d = JumpNode('d')

a.next = b
a.jump = b
b.next = c
b.jump = d
c.next = d
c.jump = b

rs = RecursiveSolution()
a = rs.setJumpOrder(a)
print(a)

Is = Solution()
a = Is.setJumpOrder(a)
print(a)
