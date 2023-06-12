import pdb

from apitests.utilities.requestsUtility import RequestsUtility
import logging as logger
import allure
import pytest
import random
from json import JSONDecodeError


@allure.feature('Delete Bookings')
@pytest.mark.tcid7
def test_delete_booking(post_token):
    logger.info("TEST: Deletes a current booking")

    get_token = post_token['token']

    # call helpers
    req_helper = RequestsUtility()

    # call api to get random booking id
    rs_api = req_helper.get(endpoint='booking')
    booking_id = random.choice(rs_api)['bookingid']

    # call api to delete booking by id
    try:
        rs_api2 = req_helper.delete(endpoint=f'booking/{booking_id}',
                                    headers={
                                             'Cookie': f"token={get_token}"
                                    },
                                    expected_status_code=201)
        assert rs_api2

    except JSONDecodeError:
        pass

