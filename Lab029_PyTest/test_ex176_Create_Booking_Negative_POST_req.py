#Negative Test cases should return 400 not 500
# If Negative Test case returns 200 then its BUG

# Missing Mandatory field -- Missing first name

import pytest
import allure
import requests


@allure.title("TC#1 Verify the Post Request Negative ")
@allure.description("TC#1 Verify the create booking Negative")
#@pytest.mark.crud
def test_create_booking_negative_tc1():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    url = base_url + base_path
    headers = {"Content-Type" : "application/json"}
    payload = {
    #"firstname" : "Jim",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}
    response = requests.post(url=url,headers=headers,json=payload)
    print(response.status_code)
    #assert response.status_code == 500
    #assert  response.text == "Internal Server Error"
    assert response.status_code == 400, (
        f"BUG: server returned {response.status_code} instead of 400"
    )

# Invalid Data Type - total price
def test_create_booking_negative_tc2():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    url = base_url + base_path
    headers = {"Content-Type" : "application/json"}
    payload = {
    "firstname" : "Jim",
    "lastname" : "Brown",
    "totalprice" : "One",
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}
    response = requests.post(url=url,headers=headers,json=payload)
    response_json = response.json()
    print(response.status_code)
    assert response.status_code == 200
    assert "bookingid" in response_json

# Invalid Date Logic checkout < checkin
def test_create_booking_negative_tc3():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    url = base_url + base_path
    headers = {"Content-Type" : "application/json"}
    payload = {
    "firstname" : "Jim",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-10",
        "checkout" : "2019-01-06"
    },
    "additionalneeds" : "Breakfast"
}
    response = requests.post(url=url,headers=headers,json=payload)
    response_json = response.json()
    print(response.status_code)
    assert response.status_code == 200
    assert  "bookingid" in response_json

# Empty Payload
def test_create_booking_negative_tc4():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    url = base_url + base_path
    headers = {"Content-Type" : "application/json"}
    payload = {}
    response = requests.post(url=url,headers=headers,json=payload)
    print(response.status_code)
    #assert response.status_code == 500
    #assert  response.text == "Internal Server Error"
    assert response.status_code == 400, (
        f"BUG: server returned {response.status_code} instead of 400"
    )
