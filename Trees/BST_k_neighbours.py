from queue import Queue


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
            return
        else:
            curr_node = self.root
            while True:
                if data < curr_node.data:
                    # Left
                    if curr_node.left == None:
                        curr_node.left = new_node
                        return
                    else:
                        curr_node = curr_node.left
                elif data > curr_node.data:
                    # Right
                    if curr_node.right == None:
                        curr_node.right = new_node
                        return
                    else:
                        curr_node = curr_node.right

    def lookup(self, data):
        curr_node = self.root
        while True:
            if curr_node == None:
                return False
            if curr_node.data == data:
                return curr_node
            elif data < curr_node.data:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right

    def print_tree(self):
        if self.root != None:
            self.printt(self.root)
# Inorder Traversal (We get sorted order of elements in tree)

    def printt(self, curr_node):
        if curr_node != None:
            self.printt(curr_node.left)
            print(str(curr_node.data))
            self.printt(curr_node.right)

    def set_parents(self):
        # level_order_traversal of tree
        parents = {}
        queue = Queue()
        queue.put([self.root, None])

        while not queue.empty():
            curr_node, parent = queue.get()
            if parent:
                parents[curr_node.data] = parent
            if curr_node.left:
                queue.put([curr_node.left, curr_node])
            if curr_node.right:
                queue.put([curr_node.right, curr_node])
        return parents

    def k_neighbors_alt(self, starting_node_value, k):
        parents = self.set_parents()
        start_node = self.lookup(starting_node_value)
        if k == 0:
            return start_node.value

        # queue for BFS traversal
        queue = Queue()
        # seen to keep track of nodes we have processed
        seen = set()
        res = []
        queue.put((start_node, 0))

        while not queue.empty() != 0:
            # process each node
            curr_node, level = queue.get()
            # keep track of what we have seen?
            seen.add(curr_node.data)
            if level == k:
                res.append(curr_node.data)
                continue
            if curr_node.left:
                if curr_node.left.data not in seen:
                    queue.put((curr_node.left, level + 1))

            if curr_node.right:
                if curr_node.right.data not in seen:
                    queue.put((curr_node.right, level + 1))

            # does this node have a parent?
            if parents.get(curr_node.data):
                parent_node = parents.get(curr_node.data)
                if parent_node.data not in seen:
                    queue.put((parent_node, level + 1))

        return res

    def k_neighbors(self, starting_node_value, k):
        """
        Returns all nodes k distance away in a binary tree

        BFS type problem
        Typical BFS type traversal
        Time : O(M + N)
        NOTE: M = # edges = N - 1, N = # of nodes

        We need a hashtable to store parents for N nodes
        Space : O(N)
        """
        parents = self.set_parents()
        start_node = self.lookup(starting_node_value)
        if k == 0:
            return start_node.value

        # queue for BFS traversal
        queue = Queue()
        # seen to keep track of nodes we have processed
        seen = set()
        # level counter
        currentLevel = next_level_nodes = 0
        current_level_nodes = 1

        queue.put(start_node)
        while currentLevel != k:
            curr_node = queue.get()
            current_level_nodes -= 1

            seen.add(curr_node.data)
            if curr_node.left:
                if curr_node.left.data not in seen:
                    queue.put(curr_node.left)
                    next_level_nodes += 1

            if curr_node.right:
                if curr_node.right.data not in seen:
                    queue.put(curr_node.right)
                    next_level_nodes += 1

            # does this node have a parent?
            if parents.get(curr_node.data):
                parent_node = parents.get(curr_node.data)
                if parent_node.data not in seen:
                    queue.put(parent_node)
                    next_level_nodes += 1

            if current_level_nodes == 0:
                currentLevel += 1
                current_level_nodes = next_level_nodes
                next_level_nodes = 0

        values = []
        while not queue.empty():
            node = queue.get()
            values.append(node.data)

        return values


bst = BinarySearchTree()
bst.insert(10)
bst.insert(3)
bst.insert(6)
bst.insert(12)
bst.insert(8)
bst.insert(5)
bst.insert(1)

print(bst.k_neighbors_alt(5, 2))
