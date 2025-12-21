

import pytest
import allure
import requests

@allure.title("TC#1 Verify the GET Resquest")
@allure.description("TC#1 Verify the GET Resquest is successfull and status code is 200")
@pytest.mark.positive
def test_get_request():
    url = "https://restful-booker.herokuapp.com/booking/1"
    response_data = requests.get(url=url)
    print(response_data)
    assert response_data.status_code==200

@allure.title("TC#1 Verify the GET Resquest with invalid bookingid ")
@allure.description("TC#1  testcase checking booking id -1 and status code is 200")
@pytest.mark.positive
def test_get_request_negative():
    url = "https://restful-booker.herokuapp.com/booking/-1"
    response_data = requests.get(url=url)
    assert response_data.status_code==404