import pytest
@pytest.mark.dependency()
def test_c():
    assert 2==2

@pytest.mark.dependency(depends=["test_c"])
def test_d():
    pass