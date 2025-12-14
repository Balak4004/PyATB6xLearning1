


import pytest
import allure
import requests


@allure.title("TC#1 Verify the Post Request")
@allure.description("TC#1 Verify the create booking")
#@pytest.mark.crud
def test_create_booking_poitive_tc1():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    url = base_url + base_path
    headers = {
        "Content-Type" : "application/json"
    }
    payload = {
    "firstname" : "Jim",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}
    response_data = requests.post(url=url,headers=headers,json=payload)
    assert response_data.status_code == 200

    time = response_data.elapsed.total_seconds()
    assert time < 5

    response_data = response_data.json()
    print(response_data)

    # Booking Id>0 and first name is Jim

    bookingid = response_data["bookingid"]
    firstname = response_data["booking"]["firstname"]
    print(bookingid)
    print(firstname)

    assert bookingid is not None
    assert bookingid > 0
    assert type(bookingid) == int


    assert firstname == "Jim"
    assert type(firstname) == str

    lastname = response_data["booking"]["lastname"]
    totalprice = response_data["booking"]["totalprice"]
    depositpaid = response_data["booking"]["depositpaid"]
    assert lastname == "Brown"
    assert totalprice == 111
    assert depositpaid == True

    checkin = response_data["booking"]["bookingdates"]["checkin"]
    checkout = response_data["booking"]["bookingdates"]["checkout"]
    assert checkin == "2018-01-01"
    assert checkout == "2019-01-01"


    

@allure.title("TC#1 Verify the Post Request Negative ")
@allure.description("TC#1 Verify the create booking Negative")
#@pytest.mark.crud
def test_create_booking_negative_tc1():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    url = base_url + base_path
    headers = {"Content-Type" : "application/json"}
    payload = {}
    response = requests.post(url=url,headers=headers,json=payload)
    assert response.status_code == 500
    assert  response.text == "Internal Server Error"
