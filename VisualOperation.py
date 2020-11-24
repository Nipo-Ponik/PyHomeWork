from Card import Card
from Operation import Operation
import tkinter

def key_check():
    if Operation.turns == 2:
        card.block = True
        Quit()
    else:

        if Operation.check_key(card, int(ent_key.get())):
            print(Operation.check_key(card, int(ent_key.get())))
            visible()
        else:
            Operation.turns += 1


def visible():
    print(Operation.check_key(card, int(ent_key.get())))
    lbl_key.pack_forget()
    ent_key.pack_forget()
    btn_next.pack_forget()

    lbl_view.pack()
    btn_view.pack()
    lbl_view.pack()
    btn_add.pack()
    ent_add.pack()
    btn_withdraw.pack()
    ent_withdraw.pack()
    btn_last.pack()
    lbl_last.pack()


def view_balance(card):
    print(str(card.balance))
    lbl_view.text = str(card.balance)


def add_balance():
    operation = Operation.add_balance(card, int(ent_add.get()))
    Card = operation.card
    Card.balance += operation.amount
    print(str(Card.balance))

def Quit():
    global root
    root.destroy()


operations = []

Card.key = 498
Card.number = 11
Card.balance = 5000

card = Card(5000, 498, 11)
turns = 0

root = tkinter.Tk()
root.geometry("400x400")

lbl_key = tkinter.Label(text="Введите код")
lbl_key.pack()
ent_key = tkinter.Entry(root)
ent_key.pack()
btn_next = tkinter.Button(root, command=key_check, text="Далее", width=50)
btn_next.pack()

lbl_view = tkinter.Label(root, width=50, text=0)
btn_view = tkinter.Button(root, command=view_balance(card), text="Посмотреть счёт", width=50) #.grid(row = 1, column = 2)

ent_add = tkinter.Entry(root, width=50)
btn_add = tkinter.Button(root, command=add_balance, text="Пополнить счёт", width=50)

ent_withdraw = tkinter.Entry(root, width=50)
btn_withdraw = tkinter.Button(root, command=key_check, text="Снять деньги", width=50)

lbl_last = tkinter.Entry(root, width=50)
btn_last = tkinter.Button(root, command=key_check, text="Показать последние операции", width=50)

root.mainloop()


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