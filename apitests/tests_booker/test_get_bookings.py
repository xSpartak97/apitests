from apitests.utilities.requestsUtility import RequestsUtility
import logging as logger
import allure
import pytest
import pdb
import random


@allure.feature('Get bookings')
@pytest.mark.tcid1
def test_get_booking():
    logger.info("TEST: Returns the ids of all the bookings that exist within the API.")

    # call helper
    req_helper = RequestsUtility()

    # call api
    rs_api = req_helper.get(endpoint='booking')

    assert rs_api


@allure.feature('Get bookings')
@pytest.mark.tcid2
def test_get_booking_by_id():
    logger.info("TEST: Returns a specific booking based upon the booking id provided")

    # call helper
    req_helper = RequestsUtility()

    # call api to get random booking id
    rs_api = req_helper.get(endpoint='booking')
    booking_id = random.choice(rs_api)['bookingid']

    # call api to get booking by id
    rs_api2 = req_helper.get(endpoint=f'booking/{booking_id}')

    assert rs_api2