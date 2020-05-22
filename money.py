import dataclasses


# 他国通貨オブジェクト
@dataclasses.dataclass(frozen=True)
class Money:
    amount: int
    currency: str

    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency)

    def add(self, added):
        if self.currency == added.currency:
            return Money(self.amount + added.amount, self.currency)
        else:
            # ドル換算で足し算を行う
            augend = Bank.exchange(self)
            added = Bank.exchange(added)
            return Money(augend.amount + added.amount, "USD")


# 銀行オブジェクト
class Bank:
    # 為替レート
    rates = {"CHF": 0.5}
    # 為替関数
    @classmethod
    def exchange(self, money):
        if money.currency == "USD":
            return money
        else:
            return Money(money.amount * self.rates[money.currency], "USD")
