from time import time
from block import Block

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.transactions = []

        # Create first block on the chain (Genesis block)
        self.create_block()


    def create_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.transactions,
            'proof': proof,
            'previous_hash': previous_hash
        }

        self.transactions = []
        self.chain.append(block)

        return block


    def create_transaction(self, block: Block):
        self.transactions.append({
            'sender': block.sender,
            'recipient': block.recipient,
            'amount': block.amount,
        })
        
        # Returns the block that will receive the transaction
        return self.get_last_block['index'] + 1


    @property
    def get_last_block(self):
        return self.chain[-1]
    