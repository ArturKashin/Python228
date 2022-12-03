class Customer:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f'{self.name} баланс {self.balance}'

    def record_payment(self, amount_paid):
        assert amount_paid > 0, "Сумма пополнения должна быть > 0!"
        self.balance += amount_paid

    def record_call(self, call_type, minutes):
        if call_type == "Г":
            self.balance += minutes * 5
        elif call_type == "М":
            self.balance -= minutes * 1
