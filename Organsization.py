from Telephone.PhoneDirectory import Phone_directory


class Organization(Phone_directory):

    def __init__(self, address, number, name, fax, contact):
        super().__init__(address, number)
        self._name = name
        self._fax= fax
        self._contact = contact

    def get_name(self):
        return self._name

    def get_fax(self):
        return self._fax

    def get_contact(self):
        return self._contact