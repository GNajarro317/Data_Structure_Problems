Task
The task is to design a data structure for a Least Recently Used (LRU) cache. The cache will have a limited size and will need to efficiently handle two primary operations: get() and put().

Explanation
OrderedDict is imported as it provides a dictionary subclass that rememebrs the order entries were added. This is a valuable tool as the problem
requires us to know which value is not being called frequently so it could be removed from the cache memory as it reaches capacity.

The time complexity of the get and set operations in this LRU Cache implementation is O(1).
The get and set operations in the LRU_Cache class have a time complexity of O(1) because they directly access the cache using the key, 
and the operations like move_to_end, popitem, and setting a key in the cache are all constant time operations.