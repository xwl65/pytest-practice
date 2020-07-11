import pytest

@pytest.fixture(autouse=True)
def login():
    print("计算开始")
    yield
    print('计算结束')