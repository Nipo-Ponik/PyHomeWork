from Types import Types


class Operation(object):
    turns = 0

    def __init__(self, card, type, amount):
        self.card = card
        self.type = type
        self.amount = amount

    @staticmethod
    def view_balance(card):
        return Operation(card, Types.View.name, card.balance)

    @staticmethod
    def add_balance(card, amount):
        card.balance += amount
        return Operation(card, Types.Add.name, amount)

    @staticmethod
    def withdraw_balance(card, amount):
        if card.balance - amount > card.balance:
            print('Сумма снятия больше баланса')
            return Operation(card, Types.Withdraw.name, 0)
        else:
            card.balance -= amount
            return Operation(card, Types.Withdraw.name, amount)

    @staticmethod
    def check_key(card, user_key):
        if user_key == card.key:
            return True
        else:
            return False
