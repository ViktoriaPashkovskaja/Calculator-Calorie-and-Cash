import datetime as dt
from typing import List, Optional

class Calculator:
    """Создание класса Calculator"""
    def __init__(self, limit: float)->None:#Создаем limit, функция ничего не возвращает
        self.limit = limit #создаем limit
        self.records:List = []#создаем список records, в котором будем хранить запись
        print(f'Ваш лимит:{limit}!') #выводим limit

    def add_record(self, rec)->None: #создаем rec, функция ничего не возвращает
        self.records.append(rec)# В список records добавляем то, что есть в rec
        print(f'Количество: {rec.amount}, с комментарием {rec.comment} на {rec.date} ') #выводим сумму, комментарий, дату

    def get_today_status(self)->float: #создаем функцию для расчета затрат за день, возвращаем float
        """Расчет расходов за день"""
        today_status:float = 0 #создаем переменную today_status для расчета затрат за день
        now = dt.date.today() #создаем переменную now, чтобы брать дату за сегодня
        
        for rec in self.records: #создаем цикл, берём то, что у нас в списке и передаем в переменную rec
            if rec.date == now:# Если переданная дата rec.date равна дате сегодняшней дате то...
                today_status += rec.amount #в today_status прибавляют затраты за сегодня rec.amount
    
        return today_status #вернули значение today_status
                
    def get_week_stats(self)->float: #создаем функцию для расчета затрат за последние 7 дней
        """Данные за неделю""" 
        count_cash_week:float = 0 #создаем переменную для сохранения затрат за 7 дней
        today = dt.datetime.today().date() #создаем переменную today для сохранения текущего дня
        day_week_ago = (dt.datetime.today().date() - dt.timedelta(days=7)) #создаем переменную day_week_ago для сохранения дней
       
        for rec in self.records:#Создаем цикл для учета затрат за неделю
            if today >= rec.date >= day_week_ago:#Если сегодня дата больше или равна переданной дате или переданная дата больше или равна продолжительности, разницы между датами
                count_cash_week += rec.amount#Подсчет затрат за неделю
        return count_cash_week#вернули значение count_cash_week       
    
class CaloriesCalculator(Calculator):#Создаем класс для определения остатка каллорий
    def get_calories_remained(self): #Создаем функцию для определения остатка каллорий
        calories_amount = self.get_today_status() #Создаем переменную для каллорий за сегодня
        if calories_amount < self.limit: #Если каллории больше или равно чем установлено
            print(f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {self.limit - calories_amount} кКал»')
        else:
            print('Хватит есть!')

class CashCalculator(Calculator): #Создаем класс для определения остатка денег
    """Калькулятор для денег. Показывает в трех валютах потраченные деньги за день и неделю"""   
    USD_RATE = float(73.59) #Создаем константу доллара
    EURO_RATE = float(89.78) #Создаем константу евро
    RUB_RATE = 1.0 #Создаем константу рубля
    
    def get_today_cash_remained(self, currency): #Создаем функцию get_today_cash_remained для расчета остатка денег на сегодня
        
        today_cash: float = self.get_today_status()#Создаем переменную today_cash для сохранения затрат за денб
 
        if currency == 'usd': #Проверяем валюту
            curr:str = 'USD' #Присваеваем валюту
            balance = round((self.limit - today_cash) / self.USD_RATE, 2) #Баланс в долларах в день
        elif currency == 'eur': #Проверяем валюту
            curr = 'EUR' #Присваеваем валюту
            balance = round((self.limit - today_cash) / self.EUR_RATE, 2) #Баланс в евро в день
        elif currency == 'rub': #Проверяем валюту
            curr = 'RUB' #Присваеваем валюту
            balance = round((self.limit - today_cash) / self.RUB_RATE, 2) #Баланс в рублях в день
        else:
            currency = '' #Нет валюты
            print('Нет такой валюты')
        
        if today_cash<self.limit: #Остаток на день, деньги остались
            money_days:float = 'На сегодня осталось ' + str(balance) + ' ' + curr
        elif today_cash == self.limit: #Остаток на день, деньги по 0
            money_days = 'Денег нет, держись'
        else: #Остаток на день, нет денег
            money_days = 'Денег нет, держись: твой долг - ' + str(balance) + ' ' + curr
        return money_days
    
class Record: #Класс для создания записей
    """Класс для создания записей"""
    def __init__(self, amount:float, comment:str, date:Optional[str] = None)->None: #Функция для создания записей
        self.amount = amount #Деньги или каллории
        self.comment = comment #Комментарии
        date_format = '%d.%m.%Y' #Формат даты
        if date is None: #Проверка даты, сегодняшняя или нет
            self.date = dt.datetime.today().date()
        else:
            self.date = dt.datetime.strptime(date, date_format).date()