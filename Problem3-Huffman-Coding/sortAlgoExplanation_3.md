Task
The task is to implement a data compression algorithm using Huffman Coding, which involves both encoding and decoding phases. This algorithm is a lossless compression method that efficiently represents data by creating a binary tree based on the frequency of characters in a given message.

Explanation
As a unique binary code is being use to encode the data, Counter is imported as it is a dictionary that allows collected elements to be stored as integer values.
While deque is utilized to create a queue that is more flexible than a list to append and pop operations which is necessary as we are dealing with a priority queue.

The time complexity is O(n log n) because the code involves sorting the priority queue 'pq' multiple times, which has a size of n (number of unique characters in the input data). 
The sorting operation takes O(n log n) time complexity. Additionally, the traversal of the Huffman tree to assign codes and encode the data also contributes to the overall time complexity.