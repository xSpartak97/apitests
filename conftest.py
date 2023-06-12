import pytest
from apitests.utilities.requestsUtility import RequestsUtility


@pytest.fixture()
def post_token():
    req_helper = RequestsUtility()
    token = req_helper.post(endpoint='auth', payload={"username": "admin",
                                                      "password": "password123"})
    return token