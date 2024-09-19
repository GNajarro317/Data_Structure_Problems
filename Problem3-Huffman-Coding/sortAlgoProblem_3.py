import sys
from collections import Counter, deque

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def huffman_encoding(data):
    if not data:
        return '', None

    # Determine the frequency of each character
    char_freq = Counter(data)

    # Build a priority queue of nodes
    pq = [Node(char, freq) for char, freq in char_freq.items()]
    pq.sort()

    # Handle the case of an empty string or a single character string
    if len(pq) == 0:
        return '', None
    elif len(pq) == 1:
        node = pq[0]
        codes = {node.char: '0'}
        encoded_data = '0' * node.freq
        return encoded_data, node

    # Build the Huffman tree
    while len(pq) > 1:
        left = pq.pop(0)
        right = pq.pop(0)
        parent = Node(None, left.freq + right.freq)
        parent.left = left
        parent.right = right
        pq.append(parent)
        pq.sort()

    # Assign codes to each character
    codes = {}
    def traverse(node, code=''):
        if node.char:
            codes[node.char] = code
        else:
            traverse(node.left, code + '0')
            traverse(node.right, code + '1')
    traverse(pq[0])

    # Encode the data
    encoded_data = ''.join(codes[char] for char in data)
    return encoded_data, pq[0]

def huffman_decoding(data, tree):
    if not data or not tree:
        return ''

    decoded_data = ''
    current_node = tree
    for bit in data:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right
        if current_node.char:
            decoded_data += current_node.char
            current_node = tree
    return decoded_data

if __name__ == "__main__":
    codes = {}

    # Test case 1: Normal input
    a_fine_sentence = "The name of the game"
    print("The size of the data is: {}".format(sys.getsizeof(a_fine_sentence)))
    print("The content of the data is: {}\n".format(a_fine_sentence))
    encoded_data, tree = huffman_encoding(a_fine_sentence)
    print("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    print("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    # Test case 2: large input
    large_string = "We're talking away I don't know what I'm to say I'll say it anyway Today is another day to find you Shyin' away Oh, I'll be comin' for your love, okay"
    print("The size of the data is: {}".format(sys.getsizeof(large_string)))
    print("The content of the data is: {}\n".format(large_string))
    encoded_data, tree = huffman_encoding(large_string)
    print("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    print("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    # Test case 3: String of the repeating characters
    data = "AAAAAAAAAA"
    print("The size of the data is: {}".format(sys.getsizeof(data)))
    print("The content of the data is: {}\n".format(data))
    encoded_data, tree = huffman_encoding(data)
    print("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    print("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    # Test case 4: Empty input
    empty_string = ""
    print("The size of the data is: {}".format(sys.getsizeof(empty_string)))
    print("The content of the data is: {}\n".format(empty_string))
    encoded_data, tree = huffman_encoding(empty_string)
    print("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    print("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
