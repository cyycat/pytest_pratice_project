import pytest

@pytest.fixture(scope="module")
def login_r(request):
    user = request.param
    print(f"\n 打开首页准备登陆，登陆用户:{user}")
    return user


test_user_data = ["Tom", "Jerry"]
@pytest.mark.parametrize("login_r", test_user_data,indirect=True)
def test_login(login_r):
    a = login_r
    print(f"测试用例中login的返回值：{a}")

@pytest.mark.logout
def test_logout():
    print(f"这是test_logout")


if __name__ == '__main__':
    pytest.main(["-s", "-m=logout","test_mark_param.py"])