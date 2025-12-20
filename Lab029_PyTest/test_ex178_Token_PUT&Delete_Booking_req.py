


import pytest
import allure
import requests

def get_token():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/auth"
    url = base_url + base_path
    headers = {"Content-Type" : "application/json"}
    payload = {
    "username" : "admin",
    "password" : "password123"
    }

    response_data = requests.post(url=url,headers=headers,json=payload)
    print(response_data)

    assert response_data.status_code == 200
    response_data_json = response_data.json()
    token = response_data_json["token"]
    return token

def get_booking_id():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    url = base_url + base_path
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response_data = requests.post(url=url, headers=headers, json=payload)
    response_data_json = response_data.json()
    booking_id = response_data_json["bookingid"]
    return booking_id

def test_put_update_booking():
    token = get_token()
    booking_id = get_booking_id()
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(booking_id)
    url = base_url + base_path
    cookie = "token=" + token
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }
    payload = {
        "firstname": "Amit",
        "lastname": "Roy",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.put(url=url, headers=headers,json=payload)
    assert response.status_code == 200
    assert response.json()["firstname"] == "Amit"
    assert response.json()["lastname"] == "Roy"

def test_delete_booking():
    token = get_token()
    booking_id = get_booking_id()
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(booking_id)
    url = base_url + base_path
    Cookie = "token=" + token
    headers = {
        "Content-Type": "application/json",
        "Cookie": Cookie
    }

    response = requests.delete(url=url,headers=headers)
    assert response.status_code == 201
    assert response.text == "Created"



