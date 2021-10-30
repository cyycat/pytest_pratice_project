import pytest

def test_success():
    """this test succeeds"""
    assert True


def test_failure():
    """this test fails"""
    assert False


def test_skip():
    """this test is skipped"""
    pytest.skip('for a reason!')


def test_broken():
    raise Exception('oops')


if __name__ == '__main__':
    pytest.main(["-v","test_alluredemo.py"])

    # pytest --alluredir=