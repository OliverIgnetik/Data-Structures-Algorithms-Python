"""
############################# TRIES #####################################
REFERENCES
https://www.youtube.com/watch?v=-urNrIAQnNo Lukas Vyhnalek
https://www.youtube.com/watch?v=giiaIofn31A Michael Muinos

Tries (also known as radix trees or prefix trees) are tree-based data structures 
that are typically used to store associative arrays where the
keys are usually strings. Since they also implement associative arrays, tries 
are often compared to hash tables.

Tries are interesting for many reasons. For one, nodes in the tree do not store keys.
Instead, they each store parts of keys. Traversing down from the root node to a leaf
allows you to build the key as you progress. Also, there doesn't need to be a value at every node. 
In fact, values are typically only associated with leaf nodes. Building keys as you go is useful 
for specific applications, notably auto-complete.

A trie is, like other tree-based data structures, made up of a set of nodes connected by pointers. 
These pointers indicate a parent-child relationship between the nodes. Parents are above their
children in the tree. Typically the root node of the tree is an "empty" node so that it can point
to all members of the alphabet the trie is using to store.

Unlike other tree-based data structures like the AVL tree, the trie is not necessarily balanced. 
It is totally dependent on the contents of the tree.Nodes in the trie can hold either single
members of the alphabet or the entire word so far. 
"""

######################## PERFORMANCE ###################################
"""
The time complexity of making a trie depends heavily on the representation of the language being stored in the trie.

m = length of the longest word
n = number of words in the trie
a = length of the word you are searching for

| Trie Operation |    Worst   |
|----------------|------------|
| Create         | O(m.n)     |
| Lookup         | O(a.n)     |
| Insert         | O(a.n)     |
| Delete         | O(a.n)     |
"""

######################## APPLICATIONS ###################################

"""
Some good applications of tries include: 
- Word validation
- Autocomplete on a phone
- Matching algorithms
- Sorting (similar to radix sort)
"""

# REFERENCE FOR CODE: https://brilliant.org/wiki/tries/


class Node:
    def __init__(self):
        self.key = None
        self.value = None
        self.children = {}


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word, value):
        currentWord = word
        currentNode = self.root
        while len(currentWord) > 0:
            if currentWord[0] in currentNode.children:
                # iterate currentNode if we find it
                currentNode = currentNode.children[currentWord[0]]
                # move on to the next letter
                currentWord = currentWord[1:]
            else:
                # If the current letter is not in this currentNode's children
                # create a new node
                newNode = Node()
                newNode.key = currentWord[0]
                # if this is the last letter set newNode value
                # note this is similar to using a boolean to mark the end of the word
                # ie. words that exist will have a value
                if len(currentWord) == 1:
                    newNode.value = value
                currentNode.children[currentWord[0]] = newNode
                currentNode = newNode
                currentWord = currentWord[1:]

    def lookup(self, word):
        currentWord = word
        currentNode = self.root
        while len(currentWord) > 0:
            # if the current letter is in this node's children
            # move on to that node
            if currentWord[0] in currentNode.children:
                currentNode = currentNode.children[currentWord[0]]
                currentWord = currentWord[1:]
            # if we can't find the current letter in this node's children
            # the word is not in the trie
            else:
                return "Not in trie"
        # if we have run out of letters and the current node has no value
        # then the word is not in the trie
        if currentNode.value == None:
            return "None"
        # only nodes with values are valid words in the trie
        return currentNode.value

    def printAllNodes(self):
        # Breadth First Search Traversal of the trie
        # ie. we are making use of a queue
        nodes = [self.root]
        while len(nodes) > 0:
            for letter in nodes[0].children:
                nodes.append(nodes[0].children[letter])
            print(nodes.pop(0).key)


def makeTrie(words):
    trie = Trie()
    for word, value in words.items():
        trie.insert(word, value)
    return trie


if __name__ == "__main__":
    trie = makeTrie({'hello': 5, 'hat': 7, 'her': 1})
    trie.lookup('nope')
    print(trie.lookup('hello'))
    trie.printAllNodes()
