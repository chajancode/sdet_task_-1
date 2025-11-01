from random import randint

import allure
from faker import Faker

fake = Faker()


@allure.step(
        "Получение имени клиента для удаления на основе списка {customers}"
    )
def customer_to_delete(customers: list[str]) -> str:

    if not customers:
        raise ValueError("Список имён клиентов пуст")
    if not all(isinstance(cust, str) for cust in customers):
        raise TypeError("Все элементы списка должны быть типа str")

    lengths = [len(cust) for cust in customers]
    mean_length = round(sum(lengths) / len(lengths))

    cust_to_delete = min(customers, key=lambda x: abs(len(x) - mean_length))
    allure.attach(
        f"Имя клиента для удаления: {cust_to_delete}"
    )
    return cust_to_delete


@allure.step("Генерация значения для 'Last Name'")
def generate_last_name() -> str:
    last_name = fake.last_name()
    allure.attach(
        f"Значение для 'Last Name': {last_name}"
    )
    return last_name


@allure.step("Генерация значения для 'Post Code'")
def generate_post_code() -> str:
    digits = [str(randint(0, 9)) for x in range(10)]
    post_code = "".join(digits)
    allure.attach(
        f"Значение 'Post Code': {post_code}"
    )
    return post_code


@allure.step("Генерация значения для 'First Name'")
def generate_first_name(post_code: str) -> str:
    letter_codes = [int(post_code[i:i+2]) for i in range(0, 10, 2)]
    letter_list = [
                chr(ord('a') + code % 26) for code in letter_codes
        ]
    first_name = "".join(letter_list)
    allure.attach(
        f"Значение для 'First Name': {first_name}"
    )
    return first_name
