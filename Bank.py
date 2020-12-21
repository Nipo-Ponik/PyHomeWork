from Organsization import Organization
from Creditor import Creditor
from Depositor import Depositor
from random import randint, choice


base = []


def generate_base():
    names = ['Alex', 'Yuno', 'Yuki', 'Ara', 'Lily']

    for i in range(randint(1, 5)):
        base.append(Creditor(choice(names), randint(10000000, 99999999), randint(10000, 999999), randint(5, 150), randint(10000, 999999)))
    for i in range(randint(1, 5)):
        base.append(Depositor(choice(names), randint(10000000, 99999999), randint(10000, 999999), randint(5, 150)))
    for i in range(randint(1, 5)):
        base.append(Organization(choice(names), randint(10000000, 99999999), randint(10000, 999999), randint(100000, 999999)))

def print_base():
    for i in base:
        st = ''
        st += 'Type: ' + str(i.__name__)
        st += ', Name: ' + str(i.get_name())
        st += ', Date: ' + str(i.get_date())
        st += ', Size: ' + str(i.get_size())
        if type(i) == Organization:
            st += ', Number: ' + str(i.get_number())
        else:
            st += ', Percentage: ' + str(i.get_percentage())
        print(st)


def search_by_date(date: int):
    out = []
    for i in base:
        print(i.get_date())
        if i.get_date() == date:
            out.append(i)
    return out


generate_base()
print_base()
print(search_by_date(int(input('Input date: '))))
