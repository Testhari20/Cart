from src.cart import calculate_discount, cart_total


def test_coupon_reduces_price():
    assert calculate_discount(100, "SAVE10") == 90


def test_unknown_coupon_keeps_price():
    assert calculate_discount(100, "NOPE") == 100


def test_cart_total_applies_coupon():
    assert cart_total([60, 40], "SAVE10") == 90
