from apitests.utilities.requestsUtility import RequestsUtility
import logging as logger
import allure
import pytest
import pdb


@pytest.mark.tcid1
def test_get_booking():
    logger.info("TEST: Returns the ids of all the bookings that exist within the API.")

    # call helper
    req_helper = RequestsUtility()

    rs_api = req_helper.get(endpoint='booking')

    assert rs_api
