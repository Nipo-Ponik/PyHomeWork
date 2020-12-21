class Client(object):

    def __init__(self, name, date, size):
        self.__name__ = self.__class__.__name__
        self._name = name
        self._date = date
        self._size = size

    def get_name(self):
        return self._name

    def get_date(self):
        return self._date

    def get_size(self):
        return self._size
