from Telephone.PhoneDirectory import Phone_directory


class Friend(Phone_directory):

    def __init__(self, address, number, second_name, born_date):
        super().__init__(address, number)
        self._second_name = second_name
        self._born_date = born_date

    def get_name(self):
        return self._second_name

    def get_born_date(self):
        return self._born_date