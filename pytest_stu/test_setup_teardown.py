


import pytest



def setup_module():
    print("这是一个setup_module方法")

def teardown_module():
    print("这是一个teardown_module方法")

def setup_function():
    print("这是一个setup_function方法")

def teardown_function():
    print("这是一个teardown_function方法")



class Test_class:

    def test_one(self):
        print("开始执行test_one方法")
        assert 1 == 1


def test_func():
    print("开始执行test_func方法")

if __name__ == '__main__':
    pytest.main(["-s"])