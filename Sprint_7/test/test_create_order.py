from Sprint_7.scooter_api import ScooterAPI
import pytest
from Sprint_7.data import Data
import allure


class TestCreateOrder:

    @allure.title('Проверка создания заказа с разным набором стандартных цветов')
    @pytest.mark.parametrize("color", [(Data.ORDER_DATE_1), (Data.ORDER_DATE_2), (Data.ORDER_DATE_3), (Data.ORDER_DATE_4)])
    def test_create_order(self, color):
        create_order = ScooterAPI.create_order(color)

        assert create_order.status_code == 201 and "track" in create_order.json()