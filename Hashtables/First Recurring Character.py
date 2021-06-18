# O(N^2) time complexity
def func(mylist):

    for i in range(0, len(mylist)):
        for j in range(i + 1, len(mylist)):
            if mylist[i] == mylist[j]:
                return mylist[i]
    return 0


# O(N) time complexity
def hashtable(mylist):
    mydict = {}
    for i in range(0, len(mylist)):
        if mylist[i] in mydict:
            # return the index of where you encountered the number previously
            return mylist[i]
        else:
            mydict[mylist[i]] = i
    return 0


mylist = [2, 1, 1, 2, 3, 4, 5]
x = hashtable(mylist)
print(x)
