from Customer import Customer
from Item import Item
from Day import *
from random import randint


CHANCE = 53 #In percents
MAX_COST = 100 # 100,000
MIN_COST = 1 # 1,000
DAYS_FOR_BACK = 10
PERCENTS = 50
ITEMS = ['Ring', 'Guitar', 'Bracelet', 'Pullover', 'T-shirt', 'Phone', 'Lamp']
NAMES = ['John', 'Roy', 'Ron', 'Jek', 'Garry', 'Alex', 'Anna', 'Cristian', 'Elsa', 'Alan', 'Olaf']

day = 1
cash = 0
items = []
items_count = 0
day_customers = []

while(True):
    day_customers = []
    day += 1
    print('Day: ' + str(day))

    for i in range(randint(0, 5)):
        items.append(Item(ITEMS[randint(0, len(ITEMS) - 1)], randint(MIN_COST, MAX_COST) * 100, day))
        items_count += 1
        day_customers.append(Customer(items[0], day, NAMES[randint(0, len(NAMES) - 1)]))
        print(f'{day_customers[i]._name} brought a {items[len(items)-1]._name}: -{items[len(items)-1]._cost / 2}$')
        cash -= items[len(items)-1]._cost / 2

    for item in items:
        if item._day + DAYS_FOR_BACK < day and randint(0, round(100 / CHANCE)) == 0:
            print(f'{item._name} has sold: +{item._cost}$')
            cash += item._cost
            items.pop(items.index(item))
            items_count -= 1

    if len(day_customers) == 0:
        print('There were no customers today\n' +  'Cash: ' + str(cash) + '$')
    else:
        print('Cash: ' + str(cash) + '$')

    inp = input()
    if inp != '':
        break
