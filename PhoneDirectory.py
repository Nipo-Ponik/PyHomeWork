class Phone_directory(object):

    def __init__(self, address, number):
        self.__name__ = self.__class__.__name__
        self._address = address
        self._number = number

    def get_number(self):
        return self._number

    def get_address(self):
        return self._number
