from Telephone.Friend import Friend
from Telephone.Person import Person
from Telephone.Organsization import Organization
from random import randint, choice


base = []


def generate_base():
    names = ['Alex', 'Yuno', 'Yuki', 'Ara', 'Lily']

    for i in range(randint(1, 5)):
        base.append(Person(randint(1000, 9999), randint(100000000, 999999999), choice(names)))
    for i in range(randint(1, 5)):
        base.append(Friend(randint(1000, 9999), randint(100000000, 999999999), choice(names), randint(10000000, 99999999)))
    for i in range(randint(1, 5)):
        base.append(Organization(randint(1000, 9999), randint(100000000, 999999999), choice(names), randint(1000, 9999), randint(1000, 9999)))

def print_base():
    for i in base:
        st = ''
        st += 'Type: ' + str(i.__name__)
        st += ', Name: ' + str(i.get_name())
        st += ', Number: ' + str(i.get_number())
        st += ', Address: ' + str(i.get_address())
        print(st)


generate_base()
print_base()
