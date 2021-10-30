import pytest

@pytest.fixture(scope="function")
def login():
    print("这是登陆1")
    yield
    print("退出登陆拉")


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "logout: mark test to run only on named environment"
    )