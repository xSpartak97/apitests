from apitests.utilities.requestsUtility import RequestsUtility
import logging as logger
import allure
import pytest


@allure.feature('Post bookings')
@pytest.mark.tcid3
def test_create_booking():
    logger.info("TEST: Creates a new booking in the API")

    # call helper
    req_helper = RequestsUtility()

    # payload
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": 1,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    # call api
    rs_api = req_helper.post(endpoint='booking', payload=payload)

    assert rs_api


@allure.feature('Post bookings')
@pytest.mark.tcid4
@pytest.mark.xfail
def test_invalid_create_booking():
    logger.info("TEST: Creates an invalid new booking in the API without firstname string.")

    # call helper
    req_helper = RequestsUtility()

    # payload
    payload = {
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": 1,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    # call api
    rs_api = req_helper.post(endpoint='booking', payload=payload, expected_status_code=500)

    assert rs_api
