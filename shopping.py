def apply_discount(price, discount_percent):
    # BUG 3: Adds the discount instead of subtracting it
    discount = price * discount_percent / 100
    return round(price + discount, 2)


def get_item(items, index):
    # BUG 4: Incorrect boundary check
    if index > len(items):
        return None

    return items[index]