from src.cart import calculate_discount

def test_save10_coupon_applies_correct_discount():
    """Verify that the SAVE10 coupon now correctly applies a 10% discount."""
    price = 200.0
    expected_price_after_discount = 180.0
    assert calculate_discount(price, "SAVE10") == expected_price_after_discount

def test_save10_coupon_with_decimal_price():
    """Verify discount calculation with a decimal price to check rounding."""
    price = 123.45
    expected_price_after_discount = round(123.45 * 0.9, 2) # 111.105 -> 111.11
    assert calculate_discount(price, "SAVE10") == expected_price_after_discount
