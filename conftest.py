import pytest
@pytest.fixture(scope='function')
def cacl_begin_over():
    print("计算开始")
    yield
    print('计算结束')