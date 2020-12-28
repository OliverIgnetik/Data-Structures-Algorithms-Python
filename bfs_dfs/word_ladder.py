from Graph import Graph


def buildGraph(wordFile):
    d = {}
    g = Graph()

    wfile = open(wordFile, 'r')
    # create buckets of words that differ by one letter
    for line in wfile:
        # ignore the \n delimeter
        word = line[:-1]
        # wildcard approach for letters
        # p_ll -> pull, poll, pill in the same bucket
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            print(bucket)
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]

        print('-'*10)
    # add vertices and edges for words in the same bucket
    for bucket in d.keys():
        # nested for loop to check connections
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                # no point connecting it to itself
                # only add words that are actually connected
                if word1 != word2:
                    g.addEdge(word1, word2)
    return g

    # build my graph
print('-'*50)
print('buckets of words')
print('-'*50)
g = buildGraph('words.txt')
print('\n')
print('-'*50)
print('graph')
print('-'*50)

for vertex in g:
    print(vertex)
    print(vertex.getConnections())
    print('\n')
