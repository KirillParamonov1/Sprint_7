from Sprint_7.scooter_api import ScooterAPI
import Sprint_7.data
import allure


class TestCreateCourier:
    @allure.title('Проверка первичной регистрации курьера с заполнением всех обязательных полей')
    def test_success_create_courier(self, registered_delivery_payload):
        created_courier = ScooterAPI.create_courier(registered_delivery_payload)

        assert (created_courier.status_code == 201 and created_courier.json()["ok"] ==
                Sprint_7.data.MESSAGE_CREATE_COURIER)

    @allure.title('Проверка повторной регистрации курьера с заполнением всех обязательных полей')
    def test_create_dublicate_courier(self):
        created_courier_1 = ScooterAPI.create_courier(Sprint_7.data.FOR_DUBLICATE_COURIER)
        created_courier_2 = created_courier_1

        assert (created_courier_2.status_code == 409 and created_courier_2.json()['message'] ==
                Sprint_7.data.MESSAGE_CREATE_DUPLICATE_COURIER)

    @allure.title('Проверка первичной регистрации курьера при не заполнении полей')
    def test_create_courier_without_date(self):
        created_courier = ScooterAPI.create_courier_without_date()

        assert (created_courier.status_code == 400 and created_courier.json()['message'] ==
                Sprint_7.data.MESSAGE_CREATE_COURIER_WITHOUT_DATE)