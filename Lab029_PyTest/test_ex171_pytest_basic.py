
import pytest

@pytest.mark.smoke
def test_method1():
    print("Hello World!!!")

    assert 5 == 5

@pytest.mark.smoke
def test_method2():
    print("Hello World!!!")

    assert 5 == 6

# pytest -v Verbose to get more information about test run result

@pytest.mark.regression
def test_method3():
    print("test 3")

    assert 1+1 == 2