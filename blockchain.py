import hashlib
import json
from time import time

class Blockchain(object):
    def __init__:
        self.chain=[]
        self.penfing_transactions=[]
    
        self.new_block(previous_hash='Haha Blockchain Learinig is really cool',proof=123)

    def new_block(self,proof,previous_hash=None):
        blobk = {
            'index':len(self.chain)+1,
            'timestamp':time(),
            'transactions':self.pending_transactions,
            'proof':proof,
            'previous_hash':previous_hash or self.hash(self.chain[-1])
        }
        self.pending_transactions=[]
        self.chain.append(block)
        return block
    
    