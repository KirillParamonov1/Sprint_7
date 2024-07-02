import requests
import data
import allure


class ScooterAPI:
    @allure.step("Метод для создания курьера с заполнением полей")
    def create_courier(body):
        return requests.post(data.MAIN_URL + data.COURIER_CREATE, json=body)

    @allure.step("Метод для создания курьера без заполнения полей")
    def create_courier_without_date():
        return requests.post(data.MAIN_URL + data.COURIER_CREATE)

    @allure.step("Метод для входа курьера в аккаунт")
    def login_courier(body):
        return requests.post(data.MAIN_URL + data.COURIER_LOGIN, json=body)

    @allure.step("Метод для создания заказа")
    def create_order(body):
        return requests.post(data.MAIN_URL + data.ORDERS_GET_LIST, json=body)

    @allure.step("Метод для получения списка заказов")
    def get_order_list():
        return requests.get(data.MAIN_URL + data.ORDERS_GET_LIST)

    @allure.step("Метод для удаления курьера")
    def delete_courier(body):
        response = ScooterAPI.login_courier(body)
        courier_id = response.json().get("id")
        if courier_id:
            requests.delete(f'{data.MAIN_URL}/{courier_id}')