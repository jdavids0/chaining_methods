class User:
    
    def __init__(self, name):
        self.name = name
        self.amount = 0
    
    def make_deposit(self, amount):
        self.amount += amount
        return self

    def make_withdrawal(self, amount):
        self.amount -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")
        return self

    def transfer_money (self, other_user, amount):
        self.amount -= amount
        other_user.amount +=amount
        self.display_user_balance()
        other_user.display_user_balance()
        return self

josh = User("Josh")
logan = User("Logan")
alex = User("Alex")

josh.make_deposit(200).make_deposit(400).make_deposit(50).make_withdrawal(200).display_user_balance()


logan.make_deposit(1000).make_deposit(200).make_withdrawal(150).make_withdrawal(500).display_user_balance()

alex.make_deposit(150).make_withdrawal(40).make_withdrawal(70).make_withdrawal(30).display_user_balance()

josh.transfer_money(alex, 50)

