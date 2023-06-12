import pdb

from apitests.utilities.requestsUtility import RequestsUtility
import logging as logger
import allure
import pytest
from faker import Faker
import random


@pytest.fixture()
def post_token():
    req_helper = RequestsUtility()
    token = req_helper.post(endpoint='auth', payload={"username": "admin",
                                                      "password": "password123"})
    return token


@allure.feature('Update Bookings')
@pytest.mark.tcid5
def test_update_booking(post_token):
    logger.info("TEST: Updates a current booking")

    get_token = post_token['token']

    # call helpers
    req_helper = RequestsUtility()
    fake = Faker()

    # payload
    payload = {
        "firstname": f"{fake.first_name()}",
        "lastname": f"{fake.last_name()}",
        "totalprice": 111,
        "depositpaid": 1,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    # call api to get random booking id
    rs_api = req_helper.get(endpoint='booking')
    booking_id = random.choice(rs_api)['bookingid']

    # call api to update booking by id
    rs_api2 = req_helper.put(endpoint=f'booking/{booking_id}',
                             payload=payload,
                             headers={'Content-Type': "application/json",
                                      'Accept': "application/json",
                                      'Cookie': f"token={get_token}"})
    assert rs_api2
