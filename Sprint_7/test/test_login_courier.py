import Sprint_7.helpers
from Sprint_7.scooter_api import ScooterAPI
import Sprint_7.data
import allure


class TestLoginCourier:

    @allure.title('Проверка авторизации курьера с заполнением всех обязательных полей')
    def test_login_courier_positive(self, get_new_data):
        payload = Sprint_7.helpers.register_new_courier_and_return_login_password(get_new_data)
        response = ScooterAPI.login_courier(payload)
        assert response.status_code == 200 and 'id' in response.json()

    @allure.title('Проверка авторизации курьера без заполнения обязательных полей')
    def test_login_courier_without_date(self):
        login_courier = ScooterAPI.login_courier(Sprint_7.data.LOGIN_COURIER_WITHOUT_DATE)

        assert (login_courier.status_code == 400 and login_courier.json()['message'] ==
                Sprint_7.data.MESSAGE_LOGIN_COURIER_WITHOUT_DATE)

    @allure.title('Проверка авторизации несуществующего курьера')
    def test_login_not_existing_courier(self):
        login_courier = ScooterAPI.login_courier(Sprint_7.data.FOR_NOT_EXISTING_COURIER)

        assert (login_courier.status_code == 404 and login_courier.json()['message'] ==
                Sprint_7.data.MESSAGE_NOT_EXISTING_COURIER)