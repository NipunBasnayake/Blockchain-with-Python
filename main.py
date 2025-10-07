import hashlib

class TestCoinBlock:
    def __init__(self, previouse_block_hash, transaction_list):
        self.previouse_block_hash = previouse_block_hash
        self.transaction_list = transaction_list
        self.block_data = "-".join(transaction_list) + "-" + previouse_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

        