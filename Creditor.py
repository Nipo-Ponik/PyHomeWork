from Client import Client


class Creditor(Client):

    def __init__(self, name, date, size, percentage, remainder):
        super().__init__(name, date, size)
        self._percentage = percentage
        self._remainder = remainder

    def get_percentage(self):
        return self._percentage

    def get_remainder (self):
        return self._remainder
