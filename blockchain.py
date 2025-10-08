import hashlib
import json
from time import time

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.pending_transactions = []

        self.new_block(
            previous_hash="Haha Blockchain Learning is really cool", proof=123
        )

    def new_block(self, proof, previous_hash=None):
        block = {
            "index": len(self.chain) + 1,
            "timestamp": time(),
            "transactions": self.pending_transactions,
            "proof": proof,
            "previous_hash": previous_hash or self.hash(self.chain[-1]),
        }
        self.pending_transactions = []
        self.chain.append(block)
        return block

    @property
    def last_block(self):
        return self.chain[-1]

    def new_transaction(self, sender, recipient, amount):
        self.pending_transactions.append(
            {"sender": sender, "recipient": recipient, "amount": amount}
        )
        return self.last_block["index"] + 1

    def hash(self, block):
        starting_object = json.dumps(block, sort_keys=True)
        block_string = starting_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()
        return hex_hash

# Example usage
blockchain = Blockchain()

t1 = blockchain.new_transaction("Nipun", "Sahil", "10 BTC")
t2 = blockchain.new_transaction("Sahil", "Nipun", "5 BTC")

blockchain.new_block(12345)

print(json.dumps(blockchain.chain, indent=4))
