class Card(object):

    def __init__(self, balance, key, number, block: bool = False):
        self.balance = balance
        self.key = key
        self.number = number
        self.block = block