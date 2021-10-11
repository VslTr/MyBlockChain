import hashlib  # модуль для работы с хэш функциями
import json


balance = 147000000
my_account = {
    "name": "VyacheslavTr",
    "balance": balance,
    "open_date": "12-05-2007"
}

def my_balance(): # Fore example
    code = hashlib.sha256(str(my_account['balance']).encode())
    # считаем хэш "hashlib.sha256" от баланса в строковом формате и декодируем в бинарные данные "encode()"
    # так функция подсчета хэш суммы "hashlib" работает только сбинарными данными
    print(f"{my_account['name']} balance: {code.hexdigest()}$") # при помощи hexdigest()
    # переводим в шестнадцатиричные данные
    # хэш от переменной "code" будет всегда одинаковый пока не изменится "balance"


if __name__ == "__main__":
    json_data = json.dumps(my_account) # при помощи "json.dumps" преобразуем словарь в текст
    binary_data = json_data.encode() # приводим к бинарным данным
    hash_data = hashlib.sha256(binary_data).hexdigest() # хэш сложной структуры - словаря "my_account"
    print(hash_data)
