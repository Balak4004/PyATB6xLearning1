


import pytest
import allure

@allure.title("Verify 2-2 is equal to 0 ")
@allure.description("smoke test case with check 2-2 equal 0")
@pytest.mark.poitive
def test_method1():
    print("test 1")
    assert 2-2 == 0

@allure.title("Verify 3-3 is equal to 0 ")
@allure.description("smoke test case with check 3-3 equal 0")
@pytest.mark.poitive
def test_method2():
    print("test 2")
    assert 3-3 == 0

@pytest.mark.skip(reason="Not working")
def test_method3():
    print("test 3")
    assert 0-0 != 0