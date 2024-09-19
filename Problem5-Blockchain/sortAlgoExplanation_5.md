Task
The task is to create a simplified blockchain implementation using my knowledge of linked lists and hashing. A blockchain is a sequential chain of records (blocks), where each block contains important information about its connection to the previous block.

Explanation
The Time module is imported as the blockchain deals with timestamps and the module is able to provide time related functions such as time() which returns the time in seconds.
This is utilized in the add_block function as timestamp is an argument along with datat and the previous hash of a block.

The time complexity of this is O(n) The is_valid method iterates through the chain of blocks once, comparing each block's hash and previous_hash with the calculated hash. 
Therefore, the time complexity is O(n) where n is the number of blocks in the chain.