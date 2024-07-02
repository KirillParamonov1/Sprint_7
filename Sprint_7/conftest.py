import pytest
import helpers
import random
import string
from scooter_api import ScooterAPI


@pytest.fixture
def registered_delivery_payload():

    random_suffix = ''.join(random.choices(string.ascii_lowercase, k=5))
    login = f"{helpers.get_courier_registration_body()['login']}_{random_suffix}"
    payload = helpers.get_courier_registration_body()
    payload['login'] = login
    yield payload
    ScooterAPI.delete_courier(payload)


@pytest.fixture
def get_new_data():
    payload = helpers.get_courier_registration_body()
    yield payload