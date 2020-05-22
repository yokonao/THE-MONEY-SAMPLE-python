import unittest
from money import Money, Bank


class TestMoney(unittest.TestCase):
    # 掛け算のテスト
    def test_multiplication(self):
        five = Money(5, "USD")
        self.assertEqual(Money(10, "USD"), five.times(2))
        self.assertAlmostEqual(Money(15, "USD"), five.times(3))

    # 足し算のテスト
    def test_addition(self):
        sum = Money(5, "USD").add(Money(5, "USD"))
        self.assertEqual(sum, Money(10, "USD"))
        sum = Money(5, "CHF").add(Money(5, "CHF"))
        self.assertEqual(sum, Money(10, "CHF"))
        sum = Money(5, "USD").add(Money(10, "CHF"))
        self.assertEqual(sum, Money(10, "USD"))
        sum = Money(10, "CHF").add(Money(5, "USD"))
        self.assertEqual(sum, Money(10, "USD"))

    # 通貨のテスト
    def test_currency(self):
        self.assertEqual("USD", Money(1, "USD").currency)
        self.assertEqual("CHF", Money(1, "CHF").currency)

    # 等価性のテスト
    def test_equality(self):
        self.assertTrue(Money(5, "USD") == Money(5, "USD"))
        self.assertFalse(Money(5, "USD") == Money(6, "USD"))
        self.assertFalse(Money(5, "USD") == Money(5, "CHF"))


class TestBank(unittest.TestCase):
    # 為替のテスト
    def test_exchange_amount(self):
        five_dollars = Bank.exchange(Money(5, "USD"))
        self.assertEqual(Money(5, "USD"), five_dollars)
        ten_francs = Bank.exchange(Money(10, "CHF"))
        self.assertEqual(Money(5, "USD"), ten_francs)
        eleven_francs = Bank.exchange(Money(11, "CHF"))
        self.assertEqual(Money(5.5, "USD"), eleven_francs)
