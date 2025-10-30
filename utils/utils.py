from faker import Faker

from random import randint


def customer_to_delete(customers: list[str]) -> str:
    lengths = [len(cust) for cust in customers]
    mean_length = round(sum(lengths) / len(lengths))
    cust_to_delete = min(customers, key=lambda x: abs(len(x) - mean_length))
    return cust_to_delete


def generate_last_name() -> str:
    fake = Faker()
    return fake.last_name()


def generate_post_code() -> str:
    digits = [str(randint(0, 9)) for x in range(10)]
    return "".join(digits)


def generate_first_name(post_code: str) -> str:
    letter_codes = [int(post_code[i:i+2]) for i in range(0, 10, 2)]
    letter_list = [
                chr(ord('a') + code % 26) for code in letter_codes
        ]
    return "".join(letter_list)


# print(type(generate_post_code()))
# print(generate_first_name("0001252667"))
# print(generate_last_name())
# lister = ["Albus", "Neville", "Voldemort"]
# print(customer_to_delete(lister))
