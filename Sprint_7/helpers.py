import requests
import random
import string
import allure
import data


@allure.step('Формирование тела запроса для создания курьера')
def get_courier_registration_body():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    return payload


@allure.step('Формирование тела запроса для создания курьера и возвращения логина и пароля')
def register_new_courier_and_return_login_password(get_new_data):
    payload = get_new_data
    courier_create_url = f'{data.MAIN_URL}{data.COURIER_CREATE}'
    response = requests.post(url=courier_create_url, data=payload)
    if response.status_code == 201:
        return payload