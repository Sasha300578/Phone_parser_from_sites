import requests
import re
from pprint import pprint

def find_phone_numbers(url):
    """
    Функция для поиска номеров телефонов на заданном веб-сайте.

    Параметры:
    url (str): URL адрес сайта для поиска.

    Возвращает:
    list: Список найденных номеров телефонов.
    """
    # Отправляем HTTP-запрос к сайту
    response = requests.get(url)
    phone_numbers = []

    try:
        # Отправляем HTTP-запрос к сайту
        response = requests.get(url)
        phone_numbers = []

        if response.status_code == 200:
            # Используем регулярные выражения для поиска номеров телефонов
            pattern = re.compile(r'(?:\+7|8)\s?\(?\d{3}\)?\s?\d{3}-?\d{2}-?\d{2}')
            phone_numbers = pattern.findall(response.text)
        else:
            print(f"Ошибка: Статус ответа {response.status_code}.")
        return set(phone_numbers)
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при выполнении HTTP-запроса: {e}")
        return set()


if __name__ == "__main__":
    # url = "https://hands.ru/company/about/"
    url = input('Введите url: ')
    try:
        phone_numbers = find_phone_numbers(url)
        if(len(phone_numbers) == 0):
            print("Номера не найдены")
        else:
            print("Найденные номера телефонов:", phone_numbers)
    except:
        print("Произошла ошибка...")

