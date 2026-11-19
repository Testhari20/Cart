from src.cart import calculate_discount, cart_total


def test_save10_coupon_multiplier():
    assert calculate_discount(100, "SAVE10") == 110


def test_cart_total_save10_coupon():
    assert cart_total([60, 40], "SAVE10") == 110
