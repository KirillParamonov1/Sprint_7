MAIN_URL = 'https://qa-scooter.praktikum-services.ru'
COURIER_CREATE = '/api/v1/courier'
COURIER_LOGIN = '/api/v1/courier/login'
ORDERS_GET_LIST = '/api/v1/orders'
ORDER_CANCEL = '/api/v1/orders/cancel'

FOR_DUBLICATE_COURIER = {
    "login": "ninja",
    "password": "1234",
    "firstName": "saske"
}


FOR_LOGIN_COURIER = {
    "login": "kirill",
    "password": "1234",
    "firstName": "test5"
}

FOR_NOT_EXISTING_COURIER =  {"login": "test", "password": "1234"}

LOGIN_COURIER_WITHOUT_DATE = {"login": "", "password": ""}

COURIER_LOGIN_AND_PASSWORD = {"login": "kirill", "password": "1234"}

MESSAGE_CREATE_COURIER = True
MESSAGE_CREATE_DUPLICATE_COURIER = 'Этот логин уже используется. Попробуйте другой.'
MESSAGE_CREATE_COURIER_WITHOUT_DATE = 'Недостаточно данных для создания учетной записи'
MESSAGE_LOGIN_COURIER_WITHOUT_DATE = 'Недостаточно данных для входа'
MESSAGE_NOT_EXISTING_COURIER = 'Учетная запись не найдена'


class Data:
    ORDER_DATE_1 = {
            "firstName": "Ivan",
            "lastName": "Ivanov",
            "address": "Lenina street, 12",
            "metroStation": 4,
            "phone": "+7 800 111 11 11",
            "rentTime": 5,
            "deliveryDate": "2024-07-01",
            "comment": "Comment",
            "color": ['BLACK']
        }

    ORDER_DATE_2 = {
        "firstName": "Ivan",
        "lastName": "Ivanov",
        "address": "Lenina street, 12",
        "metroStation": 4,
        "phone": "+7 800 111 11 11",
        "rentTime": 5,
        "deliveryDate": "2024-07-01",
        "comment": "Comment",
        "color": ['GRAY']
    }

    ORDER_DATE_3 = {
        "firstName": "Ivan",
        "lastName": "Ivanov",
        "address": "Lenina street, 12",
        "metroStation": 4,
        "phone": "+7 800 111 11 11",
        "rentTime": 5,
        "deliveryDate": "2024-07-01",
        "comment": "Comment",
        "color": ['BLACK', 'GRAY']
    }

    ORDER_DATE_4 = {
        "firstName": "Ivan",
        "lastName": "Ivanov",
        "address": "Lenina street, 12",
        "metroStation": 4,
        "phone": "+7 800 111 11 11",
        "rentTime": 5,
        "deliveryDate": "2024-07-01",
        "comment": "Comment",
        "color": []
    }