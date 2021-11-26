import json
import hashlib

class Hash():

    @staticmethod
    def hash_block(block):
        # Creates a SHA-256 hash of a block
        block = json.dumps(block, sort_keys=True, default=vars).encode()
        return hashlib.sha256(block).hexdigest()
