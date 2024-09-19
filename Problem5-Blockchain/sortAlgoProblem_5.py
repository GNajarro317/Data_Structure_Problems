import hashlib
import time

class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = (str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.add_block("Genesis Block", "0")

    def add_block(self, data, previous_hash):
        timestamp = time.time()
        block = Block(timestamp, data, previous_hash)
        self.chain.append(block)
        return block

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            if current_block.hash != current_block.calc_hash() or current_block.previous_hash != previous_block.hash:
                return False
        return True

# Test Case 1: Adding a new block to the blockchain
blockchain = Blockchain()
blockchain.add_block("Transaction 1", blockchain.chain[-1].hash)
blockchain.add_block("Transaction 2", blockchain.chain[-1].hash)
print(blockchain.is_valid())  # Output: True

# Test Case 2: Tampering with the data in a block
blockchain = Blockchain()
block1 = blockchain.add_block("Transaction 1", blockchain.chain[-1].hash)
block1.data = "Tampered data"
print(blockchain.is_valid())  # Output: False

# Test Case 3: Creating an empty block
blockchain = Blockchain()
blockchain.add_block("", blockchain.chain[-1].hash)
print(blockchain.is_valid())  # Output: True

# Test Case 4: Creating blocks with the same timestamp
blockchain = Blockchain()
block1 = blockchain.add_block("Transaction 1", blockchain.chain[-1].hash)
block2 = blockchain.add_block("Transaction 2", blockchain.chain[-1].hash)
block2.timestamp = block1.timestamp
print(blockchain.is_valid())  # Output: False

# Test Case 5: Creating blocks with the same data and previous hash
blockchain = Blockchain()
block1 = blockchain.add_block("Transaction 1", blockchain.chain[-1].hash)
block2 = blockchain.add_block("Transaction 1", blockchain.chain[-1].hash)
print(blockchain.is_valid())  # Output: False