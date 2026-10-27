from src.token import refresh
def test_not_expired():
    assert refresh(100, 50) is True
