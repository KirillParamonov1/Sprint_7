from Sprint_7.scooter_api import ScooterAPI
import allure


class TestOrderList:
    @allure.title('Проверка получения списка заказов')
    def test_get_order_list(self):
        order_list = ScooterAPI.get_order_list()

        assert order_list.status_code == 200 and 'orders' in order_list.json()