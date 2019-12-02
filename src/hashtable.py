# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity=8):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity



    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        index = self._hash_mod(key) # get index within range
        curr_item = self.storage[index]
        pair = LinkedPair(key, value)

        if curr_item is None:
            self.storage[index] = pair
            return
        
        elif curr_item.next is None:
            curr_item.next = pair
            return
        
        else:
            while curr_item.next is not None:
                if curr_item.next.key == key:
                    print(f"Swapping out value of key : {key} with new value : {value}")
                    curr_item.next.value = value
                    return
                else:
                    curr_item = curr_item.next
            curr_item.next = pair






        # # check storage capacity
        # if self.count >= self.capacity:
        #     print("ERROR Will Robinson: over capacity")
        #     # if over capacity, resize
        #     self.resize()
        
        # if index > self.count:
        #     print("ERROR: out of range")
        #     return

        # # check if index is occupied
        # if self.storage[index] is None:
        #     # if not occupied then add as value
        #     self.storage[index] = pair
        # else: 
        #     # if occupied add as next in linked list
        #     pair.next = self.storage[index]
        #     self.storage[index] = pair
        
        # # increment count by 1
        # self.count += 1
    



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        if self.storage[index] is None:
            print("Nothing there to delete")
            return
        else:
            curr_pair = self.storage[index]
            while curr_pair is not None:
                if curr_pair.key == key:
                    self.storage[index] = curr_pair.next
                # swap
                curr_pair = curr_pair.next
            return
            


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        if self.storage[index] is None:
            return None

        else:
            curr_pair = self.storage[index]
            while curr_pair is not None:
                if curr_pair.key == key:
                    return curr_pair.value
                curr_pair = curr_pair.next
            return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # cache storage
        prev_storage = self.storage

        # double size
        self.capacity *= 2

        # create new storage
        new_storage = [None] * self.capacity

        # iterate over cached storage and insert into new storage
        for i in range(len(prev_storage)):
            if prev_storage[i] is not None:
                curr_item = prev_storage[i]
                while curr_item:
                    self.insert(curr_item.key, curr_item.value)
                    curr_item = curr_item.next






if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
