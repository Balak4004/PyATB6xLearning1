
import pytest
import allure

@allure.title("Verify create booking is working")
@allure.description("Verify create booking feature in this function")
@pytest.mark.poitive
def test_method1():
    print("test 1")
    assert 1+1 == 2

@allure.title("Verify create booking with invalid data")
@allure.description("Verify create booking feature for negative create booking")
@pytest.mark.negative
def test_method2():
    print("test 2")
    assert 1-1 == 2

@allure.title("Verify create booking with invalid data name")
@allure.description("Verify create booking feature for negative create booking name")
@pytest.mark.negative
def test_method3():
    print("test 3")
    assert 1*1 == 2