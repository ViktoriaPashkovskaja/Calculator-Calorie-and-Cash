import datetime as dt
from typing import List, Optional


class Calculator:
    """Создание класса Calculator"""
    def __init__(self, limit: float) -> None:
        self.limit = limit
        self.records: List = []

    def add_record(self, rec) -> None:
        self.records.append(rec)

    def get_today_stats(self) -> float:
        """Расчет расходов за день"""
        today_status = 0
        now = dt.date.today()
        for rec in self.records:
            if rec.date == now:
                today_status += rec.amount
        return today_status

    def get_week_stats(self):
        """Данные за неделю"""
        count_cash_week = 0
        today = dt.datetime.today().date()
        day_week_ago = (dt.datetime.today().date() - dt.timedelta(days=7))
        for rec in self.records:
            if today >= rec.date > day_week_ago:
                count_cash_week += rec.amount
        return count_cash_week


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        calories_amount = self.get_today_stats()
        calorr = self.limit - calories_amount
        if calorr > 0:
            print(f'Сегодня можно съесть что-нибудь ещё, '
                  f'но с общей калорийностью не более {calorr} кКал')

        else:
            print('Хватит есть!')


class CashCalculator(Calculator):
    """Калькулятор для денег"""
    USD_RATE = float(73.59)
    EURO_RATE = float(89.78)
    RUB_RATE = float(1)

    def get_today_cash_remained(self, currency):
        today_cash = self.get_today_stats()
        if currency == 'usd':
            curr = 'USD'
            balance = self.limit - today_cash
        elif currency == 'eur':
            curr = 'Euro'
            balance = self.limit - today_cash
        elif currency == 'rub':
            curr = 'руб'
            balance = self.limit - today_cash
        else:
            currency = ''
            print('Нет такой валюты')
        if today_cash < self.limit:
            money_days = 'На сегодня осталось ', str(balance), str(curr)
        elif today_cash == self.limit:
            money_days = 'Денег нет, держись'
        else:
            money_days = 'Денег нет, держись: твой долг - '
            f'{abs(balance)}{curr}'
        return money_days


class Record:
    """Класс для создания записей"""
    def __init__(self, amount: float,
                 comment: str, date: Optional[str] = None) -> None:
        self.amount = amount
        self.comment = comment
        date_format = '%d.%m.%Y'
        if date is None:
            self.date = dt.datetime.today().date()
        else:
            self.date = dt.datetime.strptime(date, date_format).date()
