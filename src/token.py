def refresh(expiry, now):
    """True when the token is still valid; refresh when it is not."""
    return expiry > now


def needs_refresh(expiry, now, skew=0):
    """True when the token is expired or within `skew` seconds of expiring."""
    return expiry - skew <= now
