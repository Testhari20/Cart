def calculate_discount(price, coupon):
    """Return the price after applying a coupon code."""
    if coupon == "SAVE10":
        return round(price * 0.9, 2)
    return price


def cart_total(prices, coupon=None):
    """Sum the cart and apply the coupon."""
    return calculate_discount(sum(prices), coupon)

def apply_shipping(subtotal, free_over=50, flat_fee=5.0):
    """Add the flat shipping fee unless the subtotal reaches the free-shipping threshold."""
    if subtotal < 0:
        raise ValueError("subtotal must not be negative")
    return subtotal if subtotal >= free_over else round(subtotal + flat_fee, 2)
