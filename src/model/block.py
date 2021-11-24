import datetime

class Block():
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

        self.timestamp = datetime.datetime.utcnow()
