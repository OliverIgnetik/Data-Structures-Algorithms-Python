class HashTable(object):

    def __init__(self, size):

        # Set up size and slots and data
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        # Note, we'll only use integer keys for ease of use with the Hash Function
        # Get the hash value
        hashvalue = self.hashfunction(key, len(self.slots))
        # If slot is Empty
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            # If key already exists, replace old value
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            # Otherwise, find the next available slot
            else:
                initial_slot = hashvalue
                nextslot = self.rehash(hashvalue, len(self.slots))
                # Get to the next slot - linear probing
                # stop when the next slot has no key or the next slot is equal to the current key
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))
                    if nextslot == initial_slot:
                        raise KeyError(
                            'Hashtable is full, linear probing revealed no empty slots')
                # Set new key, if NONE
                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                # Otherwise replace old value
                else:
                    self.data[nextslot] = data

    def hashfunction(self, key, size):
        # Remainder Method
        return key % size

    def rehash(self, oldhash, size):
        # For finding next possible positions
        return (oldhash+1) % size

    def get(self, key):

        # Getting items given a key

        # Set up variables for our search
        startslot = self.hashfunction(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = startslot

        # Until we discern that its not empty or found (and haven't stopped yet)
        while self.slots[position] != None and not found and not stop:

            if self.slots[position] == key:
                found = True
                data = self.data[position]

            else:
                position = self.rehash(position, len(self.slots))
                # after the rehash if we end up on startslot again stop
                # and return data
                if position == startslot:
                    stop = True
        return data

    # Special Methods for use with Python indexing
    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


h = HashTable(5)
# Put our first key in
h[1] = 'one'
h[2] = 'two'
h[3] = 'three'
h[4] = 'four'
h[5] = 'five'
h[6] = 'six'

print(h[1])
h[1] = 'new_one'
print(h[1])
