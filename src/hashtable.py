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
        # hash the key and convert to index
        index = self._hash_mod(key) # get index within range
        # get current value
        curr_val = self.storage[index]

        # if nothing currently indexed
        if curr_val is None:
            self.storage[index] = LinkedPair(key, value)
        # if there is a collision
        # add the new element to the linked list
        elif curr_val.next is None:
            curr_val.next = LinkedPair(key, value)
        else: 
            # if need to add to chain
            # but chain is already longer
            # or replace value
            while curr_val.next is not None:
                if curr_val.next.key == key:
                    print(f"replacing key : {key} with value : {value}")
                    curr_val.next.value = value
                    return # short out of the if statement
                else: # swap current value and move down chain
                    curr_val = curr_val.next
            # now we either replaced the value or 
            # moved down the chain to where the next
            # element in the linked list is none
            curr_val.next = LinkedPair(key, value)

        # # if there is a index collision
        # if self.storage[index] is not None:
        #     # handle collision here
        #     self.storage[index] = LinkedPair(key, value)
        #     self.storage[index].next = curr_val
        #     print(f"ERROR: overwriting data at {index}")
        
        # self.storage[index] = LinkedPair(key, value)



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        if self.storage[index] is None:
            print("Key not found")
            return

        self.storage[index] = None


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        curr_val = self.storage[index]

        # if nothing at curr_val index
        if curr_val is None:
            print(f"No value at key {key}")
            return None
        # traverse linked list
        else:
            while curr_val.next is not None:
                # look for key
                if curr_val.key is key:
                    print(f"value of key {key} is value {curr_val.value}")
                    return curr_val.value
                else: # swap and keep moving through linked list
                    curr_val = curr_val.next
            # at end of linked list, return value
            return curr_val.value


        # if self.storage[index] is not None:
        #     if self.storage[index].key == key:
        #         return self.storage[index].value
        #     else:
        #         print(f"WARNING: key doesnt match")
        #         return None
        # else:
        #     return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''

        # increase capacity
        self.capacity *= 2

        # create new storage with larger capacity
        new_storage = [None] * self.capacity

        # make a copy of prev storage
        prev_storage = self.storage

        # set storage as new_storage
        self.storage = new_storage

        # go through existing and old storage
        # and rehash all keys
        # traverse linked list

        for i in range(len(prev_storage)):
            # check item at each index
            if prev_storage[i] is not None:
                # if exists add it to a list
                curr_items = prev_storage[i]
                while curr_items:
                    self.insert(curr_items.key, curr_items.value)
                    curr_items = curr_items.next


        # for bucket_item in self.storage:
        #     if bucket_item is not None:
        #         new_index = self._hash_mod(bucket_item.key)
        #         new_storage[new_index] = LinkedPair(bucket_item.key, bucket_item.value)



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
