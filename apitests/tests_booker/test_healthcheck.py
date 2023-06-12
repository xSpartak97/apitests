from apitests.utilities.requestsUtility import RequestsUtility
import logging as logger
import pytest
from json import JSONDecodeError


@pytest.mark.health_check
def test_health_check():
    logger.info("TEST: A simple health check endpoint to confirm whether the API is up and running.")

    # call helper
    req_helper = RequestsUtility()

    # call api
    try:
        rs_api = req_helper.get(endpoint='ping', expected_status_code=201)
        assert rs_api
    except JSONDecodeError:
        pass
