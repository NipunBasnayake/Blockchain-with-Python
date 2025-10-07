import hashlib


class TestCoinBlock:
    def __init__(self, previouse_block_hash, transaction_list):
        self.previouse_block_hash = previouse_block_hash
        self.transaction_list = transaction_list
        self.block_data = "-".join(transaction_list) + "-" + previouse_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()


t1 = "Nipun sends 2.2 TC to Alice"
t2 = "Bob sends 4.1 TC to Alice"
t3 = "Alice sends 1.2 TC to Bob"
t4 = "Bob sends 3.2 TC to Nipun"
t5 = "Alice sends 2.3 TC to Nipun"
t6 = "Nipun sends 1.5 TC to Bob"

initial_block = TestCoinBlock("Initial String", [t1, t2])
print(initial_block.block_data)
print(initial_block.block_hash)

second_block = TestCoinBlock(initial_block.block_hash, [t3, t4])
print(second_block.block_data)
print(second_block.block_hash)

third_block = TestCoinBlock(second_block.block_hash, [t5, t6])
print(third_block.block_data)
print(third_block.block_hash)