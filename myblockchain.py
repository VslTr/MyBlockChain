import hashlib  # модуль для работы с хэш функциями
import json


blockchain = [
    {
    "from": "",  # кто отправил
    "to": "",  # кому отправил
    "amount": 0.0  # сколько отправил
    }
]  # список "blockchain" содержит словарь транзакций


def add_new_block (account_from, account_to, amount):
    block = {
        "from": account_from,
        "to": account_to,
        "amount": amount
    }  # создаем новый блок
    blockchain.append(block)  # добавляем новый блок в блокчейн

def data_to_hash(data):
    json_data = json.dumps(data)  # при помощи "json.dumps" преобразуем данные в текст
    binary_data = json_data.encode()  # приводим к бинарным данным
    return hashlib.sha256(binary_data).hexdigest()  # возвращаем хэш данных


if __name__ == "__main__":
    add_new_block("Bill", "Vyacheslav", 100000)
    print(blockchain)