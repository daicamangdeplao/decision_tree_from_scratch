class PiggyBank:
    # create __init__ and add_money methods
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_money(self, deposit_dollars, deposit_cents):
        self.dollars += deposit_dollars
        cents = self.cents + deposit_cents
        if cents >= 100:
            self.cents = cents % 100
            self.dollars = self.dollars + cents // 100
        else:
            self.cents = cents

    def print_account_statement(self):
        print(f"Current value: {self.dollars}.{self.cents}")
