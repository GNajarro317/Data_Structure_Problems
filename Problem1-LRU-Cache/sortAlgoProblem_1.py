from collections import OrderedDict 
# Maintains the order in which keys are added
class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.cache = OrderedDict()
        # Defines the cache in an orderly manner.

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        # Moves the key to the first position.
        return self.cache[key]

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last = False)
            # If the cache reaches capacity the least recently used key is removed.

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

## Test Case 1
our_cache = LRU_Cache(2)
our_cache.set(1, 1)
our_cache.set(2, 2)
print(our_cache.get(2))  # Output: 2

## Test Case 2
our_cache = LRU_Cache(2)
our_cache.set(1, 1)
our_cache.set(2, 2)
print(our_cache.get(200))  # Output: -1

# Test Case 3: Getting the same value over
our_cache.set(1, 1)
assert our_cache.get(1) == 1
assert our_cache.get(1) == 1
assert our_cache.get(1) == 1

# Test Case 4: Invalid values
try:
    our_cache.set(-1, 1)
except ValueError:
    pass
else:
    raise AssertionError("Expected ValueError for negative capacity")

# Test Case 5: High capacity
our_cache = LRU_Cache(100)
for i in range(100):
    our_cache.set(i, i)
for i in range(100):
    assert our_cache.get(i) == i
