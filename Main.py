from Card import Card
from Operation import Operation


operations = []

card = Card(5000, 498, 11)
turns = 0

if card.block:
    print('Карта заблокированна')
else:
    inp = int(input('Введите код/пароль: '))
    for i in range(2):
        if inp != card.key:
            turns += 1
            print('Неверный код/пароль')
            inp = int(input('Введите код/пароль: '))
        if turns == 2 and inp != card.key:
            card.block = True
            print('Карта заблокированна')
    if inp == card.key:
        while(True):
            inp = input('1 - посмотреть баланс\n'
                  '2 - пополнить баланс\n'
                  '3 - снять деньги\n'
                  '4 - показать последние операции')
            if inp.isnumeric() != True:
                print('Буквы не принимаются, только цифры от 1 до 3!')
            else:
                if int(inp) == 1:
                    operation = Operation.view_balance(card)
                    operations.append(operation)
                    card = operation.card
                    print(card.balance)
                elif int(inp) == 2:
                    operation = Operation.add_balance(card, int(input('Введите сумму пополненя:')))
                    operations.append(operation)
                    card = operation.card
                    print(card.balance)
                elif int(inp) == 3:
                    inp = int(input('Введите сумму для снятия:'))
                    if inp > card.balance:
                        print('Сумма снятия больше баланса')
                    else:
                        operation = Operation.withdraw_balance(card, inp)
                        operations.append(operation)
                        card = operation.card
                        print(card.balance)
                elif int(inp) == 4:
                    if len(operations) <= 10:
                        for op in operations:
                            print(f'Номкр карты {op.card.number}, Тип операции {op.type}, Количество {op.amount}')
                    else:
                        for i in range(10):
                            print(f'Номкр карты {operations[i].card.number}, Тип операции {operations[i].type}, Количество {operations[i].amount}')