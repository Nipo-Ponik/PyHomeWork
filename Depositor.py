from Client import Client


class Depositor(Client):

    def __init__(self, name, date, size, percentage):
        super().__init__(name, date, size)
        self._percentage = percentage

    def get_percentage(self):
        return self._percentage
