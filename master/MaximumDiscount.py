def MaximumDiscount(N, price):
    result = 0

    price = sorted(price, reverse=True) #reverse - descending sort

    for item in range(N - 1):
        if (item + 1) % 3 == 0:
            result += price[item]

    return result