from src.token import refresh, needs_refresh


def test_not_expired():
    assert refresh(100, 50) is True


def test_expired_needs_refresh():
    assert needs_refresh(100, 150) is True


def test_skew_window():
    assert needs_refresh(100, 95, skew=10) is True


def test_fresh_token_no_refresh():
    assert needs_refresh(100, 50) is False
