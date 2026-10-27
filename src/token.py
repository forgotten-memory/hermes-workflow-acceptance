def refresh(expiry, now):
    # BUG: should refresh when already expired too
    return expiry > now
