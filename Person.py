from Telephone.PhoneDirectory import Phone_directory


class Person(Phone_directory):

    def __init__(self, address, number, second_name):
        super().__init__(address, number)
        self._second_name = second_name

    def get_name(self):
        return self._second_name
