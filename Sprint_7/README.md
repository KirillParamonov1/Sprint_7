# Sprint_7
Суть проекта: составить автоматизированные тесты для проверки api сайта: https://qa-scooter.praktikum-services.ru/

Структура проекта:
* allure_results - директория с отчетами allure
* test - директория, которая содержит тесты:
  * test_create_courier, ручка: post /api/v1/courier - тестирование создания курьера
  * test_create_order, ручка: post /api/v1/orders - тестирование создания заказа
  * test_login_courier, ручка: post /api/v1/courier/login - тестирование авторизации курьера в системе
  * test_order_list, ручка: get /api/v1/orders - тестирование получения списка заказов
* conftest -фикстуры
* data - содержит url, инофрмацию о системных сообщениях и запросах
* helpers - содержит методы для генирации данных для курьера
* scooter_api - содержит базовые методы для тестирования api в тестах