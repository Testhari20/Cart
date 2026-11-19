def calculate_discount(price, coupon):
    """Return the price after applying a coupon code."""
    if coupon == "SAVE10":
        return round(price * 1.1, 2)
    return price


def cart_total(prices, coupon=None):
    """Sum the cart and apply the coupon."""
    return calculate_discount(sum(prices), coupon)
