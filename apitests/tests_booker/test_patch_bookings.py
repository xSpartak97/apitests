import pdb

from apitests.utilities.requestsUtility import RequestsUtility
import logging as logger
import allure
import pytest
from faker import Faker
import random


@allure.feature('Patch Bookings')
@pytest.mark.tcid6
def test_patch_booking():
    logger.info("TEST: Updates a current booking with a partial payload")

    # call helpers
    req_helper = RequestsUtility()
    fake = Faker()

    # payload
    payload = {
        "firstname": f"{fake.first_name()}",
        "lastname": f"{fake.last_name()}"
    }

    # call api to get random booking id
    rs_api = req_helper.get(endpoint='booking')
    booking_id = random.choice(rs_api)['bookingid']

    # call api to partially update booking by id
    rs_api2 = req_helper.patch(endpoint=f'booking/{booking_id}',
                             payload=payload,
                             headers={'Content-Type': "application/json",
                                      'Accept': "application/json",
                                      'Authorization': "Basic YWRtaW46cGFzc3dvcmQxMjM="})
    assert rs_api2
