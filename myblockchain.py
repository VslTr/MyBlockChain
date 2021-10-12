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
    prev_block = blockchain[-1] # последний блок в блокчейне
    prev_hash = data_to_hash(prev_block) # считаем
    block = {
        "from": account_from,
        "to": account_to,
        "amount": amount,
        "prev_hash": prev_hash
    }  # создаем новый блок
    blockchain.append(block)  # добавляем новый блок в блокчейн

def data_to_hash(data):
    json_data = json.dumps(data, sort_keys=True)  # при помощи "json.dumps" преобразуем данные в текст
    # и сортируем по алфавиту
    binary_data = json_data.encode()  # приводим к бинарным данным
    return hashlib.sha256(binary_data).hexdigest()[:10]  # возвращаем хэш данных (первые 10 символов для простоты)

def add_block():
    add_new_block("User1", "User11", 2000)
    add_new_block("User1", "User12", 14)
    add_new_block("User1", "User13", 88)
    add_new_block("User1", "User14", 69420)
    
    add_new_block("User11", "User12", 1000)
    add_new_block("User12", "User13", 500)
    add_new_block("User12", "User14", 500)

def validation():
    pass

if __name__ == "__main__":
    add_block()
    print(blockchain)
    print(data_to_hash(blockchain))