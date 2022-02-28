import datetime
import hashlib
# every block is an inst of the block class
class block:
    blockNo = 0
    data = None
    # pointer to the next block
    next = None
    hash = None
    nonce = 0
    # store the hash of the previous block to make the blockchain immutalble
    # thus in order to change a block we will have to change every subsequent 
    # block due to the previous hash
    previous_hash = 0x0
    timestamp = datetime.datetime.now()

    def __init__(self, data):
        self.data = data

    def hash(self):
        h = hashlib.sha256()
        h.update(
        str(self.nonce).encode('utf-8') +
        str(self.data).encode('utf-8') +
        str(self.previous_hash).encode('utf-8') +
        str(self.timestamp).encode('utf-8') +
        str(self.blockNo).encode('utf-8')
        )
        return h.hexdigest()

    def __str__(self):
        return "Block Hash: " + str(self.hash()) + "\nBlockNo: " + str(self.blockNo) + "\nBlock Data: " + str(self.data) + "\nHashes: " + str(self.nonce) + "\n--------------"

class Blockchain:
    # establishing hash finding difficulty
    diff = 20
    maxNonce = 2**32
    # increasing the difficulty
    target = 2 ** (256-diff)

    block = block("Genesis")
    dummy = head = block

    def add(self, block):

        block.previous_hash = self.block.hash()
        block.blockNo = self.block.blockNo + 1
        # adding a new block
        self.block.next = block
        self.block = self.block.next

    def mine(self, block):
        for n in range(self.maxNonce):
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1

blockchain = Blockchain()
# this will generate 10 random blocks
for n in range(10):
    blockchain.mine(block("Block " + str(n+1)))
# this will print out each block +1
while blockchain.head != None:
    print(blockchain.head)
    blockchain.head = blockchain.head.next