from Aviary import Aviary
from random import randint, choice


class Monkey(object):

    def __init__(self, name, type):
        self.type = type
        self.name = name


def generate_monkeys(TYPES: list, amount = 1):
    NAMES = ['Jo', 'Ro', 'Momo', 'Ann']
    monkeys = []
    for i in range(amount):
        monkeys.append(Monkey(choice(NAMES), choice(TYPES)))
    return monkeys


TYPES = ['peace', 'fight', 'water']

aviaries = [Aviary(TYPES[0], True),  # peace, pool
            Aviary(TYPES[0]),  # peace
            Aviary(TYPES[1]),  # fight
            Aviary(TYPES[2])] # pool

day = 0

while(True):
    day += 1
    print(f'Day: {day}')

    monkeys = generate_monkeys(TYPES, randint(0, randint(1, 5)))

    if len(monkeys) > 0:
        for monkey in monkeys:
            if monkey.type == TYPES[0]: # peace
                aviaries[1].monkeys.append(monkeys.pop(monkeys.index(monkey)))
                print(f'Monkey {monkey.name} add to {aviaries[1].type} valuer')
            elif monkey.type == TYPES[1]: # fight
                aviaries[2].monkeys.append(monkeys.pop(monkeys.index(monkey)))
                print(f'Monkey {monkey.name} add to {aviaries[2].type} valuer')
            elif monkey.type == TYPES[2]: # fight
                s = [1, 3]
                t = choice(s)
                aviaries[t].monkeys.append(monkeys.pop(monkeys.index(monkey)))
                print(f'Monkey {monkey.name} add to {aviaries[t].type} valuer')
    else:
        print('There were no monkeys today')


    if input() == ' ':
        # for aviary in aviaries:
        #     monkeys = ''
        #     for i in range(len(aviary.monkeys)):
        #         monkeys += aviary.monkeys[i].name + f'({aviary.monkeys[i].type}), '
        #     print(f'{aviary.type} aviary: {monkeys}')
        #     monkeys = ''
        break

